#include "esp_camera.h"
#include <WiFi.h>
#include "esp_http_server.h"
#include "camera_pins.h"
#include "secrets.h"   // copy from secrets.example.h — never commit secrets.h

// ------------------------------------------------------------
// Camera configuration
// ------------------------------------------------------------
static camera_config_t camera_config = {
  .pin_pwdn       = PWDN_GPIO_NUM,
  .pin_reset      = RESET_GPIO_NUM,
  .pin_xclk       = XCLK_GPIO_NUM,
  .pin_sccb_sda   = SIOD_GPIO_NUM,
  .pin_sccb_scl   = SIOC_GPIO_NUM,
  .pin_d7         = Y9_GPIO_NUM,
  .pin_d6         = Y8_GPIO_NUM,
  .pin_d5         = Y7_GPIO_NUM,
  .pin_d4         = Y6_GPIO_NUM,
  .pin_d3         = Y5_GPIO_NUM,
  .pin_d2         = Y4_GPIO_NUM,
  .pin_d1         = Y3_GPIO_NUM,
  .pin_d0         = Y2_GPIO_NUM,
  .pin_vsync      = VSYNC_GPIO_NUM,
  .pin_href       = HREF_GPIO_NUM,
  .pin_pclk       = PCLK_GPIO_NUM,

  .xclk_freq_hz   = 20000000,
  .ledc_timer     = LEDC_TIMER_0,
  .ledc_channel   = LEDC_CHANNEL_0,

  .pixel_format   = PIXFORMAT_JPEG,
  .frame_size     = FRAMESIZE_VGA,   // 640x480 — good balance for AI analysis
  .jpeg_quality   = 12,              // 0=highest quality, 63=lowest
  .fb_count       = 2,
  .grab_mode      = CAMERA_GRAB_WHEN_EMPTY,
};

// ------------------------------------------------------------
// HTTP handler: GET /capture  → single JPEG frame
// ------------------------------------------------------------
static esp_err_t capture_handler(httpd_req_t *req) {
  camera_fb_t *fb = esp_camera_fb_get();
  if (!fb) {
    httpd_resp_send_500(req);
    return ESP_FAIL;
  }

  httpd_resp_set_type(req, "image/jpeg");
  httpd_resp_set_hdr(req, "Content-Disposition", "inline; filename=capture.jpg");
  // Allow the Python backend on the same LAN to fetch frames
  httpd_resp_set_hdr(req, "Access-Control-Allow-Origin", "*");

  esp_err_t res = httpd_resp_send(req, (const char *)fb->buf, fb->len);
  esp_camera_fb_return(fb);
  return res;
}

// ------------------------------------------------------------
// HTTP handler: GET /stream  → MJPEG stream (port 81)
// ------------------------------------------------------------
#define PART_BOUNDARY "frame"
static const char *STREAM_CONTENT_TYPE =
    "multipart/x-mixed-replace;boundary=" PART_BOUNDARY;
static const char *STREAM_BOUNDARY = "\r\n--" PART_BOUNDARY "\r\n";
static const char *STREAM_PART =
    "Content-Type: image/jpeg\r\nContent-Length: %u\r\n\r\n";

httpd_handle_t stream_httpd = NULL;

static esp_err_t stream_handler(httpd_req_t *req) {
  camera_fb_t *fb  = NULL;
  esp_err_t   res  = ESP_OK;
  char        part_buf[64];

  httpd_resp_set_type(req, STREAM_CONTENT_TYPE);
  httpd_resp_set_hdr(req, "Access-Control-Allow-Origin", "*");

  while (true) {
    fb = esp_camera_fb_get();
    if (!fb) { res = ESP_FAIL; break; }

    res = httpd_resp_send_chunk(req, STREAM_BOUNDARY, strlen(STREAM_BOUNDARY));
    if (res == ESP_OK) {
      size_t hlen = snprintf(part_buf, sizeof(part_buf), STREAM_PART, fb->len);
      res = httpd_resp_send_chunk(req, part_buf, hlen);
    }
    if (res == ESP_OK)
      res = httpd_resp_send_chunk(req, (const char *)fb->buf, fb->len);

    esp_camera_fb_return(fb);
    if (res != ESP_OK) break;
  }
  return res;
}

// ------------------------------------------------------------
// HTTP handler: GET /  → simple status page (port 80)
// ------------------------------------------------------------
static esp_err_t index_handler(httpd_req_t *req) {
  String ip = WiFi.localIP().toString();
  String html =
    "<html><head><meta charset='utf-8'><title>ESP32-CAM</title></head><body>"
    "<h2>ESP32-CAM is online</h2>"
    "<p>IP: " + ip + "</p>"
    "<p><a href='http://" + ip + ":81/stream'>Live Stream (port 81)</a></p>"
    "<p><a href='/capture'>Single Capture (/capture)</a></p>"
    "</body></html>";
  httpd_resp_set_type(req, "text/html");
  return httpd_resp_sendstr(req, html.c_str());
}

// ------------------------------------------------------------
// Start web server on port 80 (UI) and port 81 (stream)
// ------------------------------------------------------------
static httpd_handle_t camera_httpd = NULL;

void startCameraServer() {
  // Port 80 — status page + /capture
  httpd_config_t config80     = HTTPD_DEFAULT_CONFIG();
  config80.server_port        = 80;
  config80.ctrl_port          = 32768;

  httpd_uri_t index_uri = {"/",        HTTP_GET, index_handler,   NULL};
  httpd_uri_t capture_uri = {"/capture", HTTP_GET, capture_handler, NULL};

  if (httpd_start(&camera_httpd, &config80) == ESP_OK) {
    httpd_register_uri_handler(camera_httpd, &index_uri);
    httpd_register_uri_handler(camera_httpd, &capture_uri);
  }

  // Port 81 — MJPEG stream
  httpd_config_t config81 = HTTPD_DEFAULT_CONFIG();
  config81.server_port    = 81;
  config81.ctrl_port      = 32769;

  httpd_uri_t stream_uri = {"/stream", HTTP_GET, stream_handler, NULL};

  if (httpd_start(&stream_httpd, &config81) == ESP_OK) {
    httpd_register_uri_handler(stream_httpd, &stream_uri);
  }
}

// ------------------------------------------------------------
// setup / loop
// ------------------------------------------------------------
void setup() {
  Serial.begin(115200);
  Serial.println("\nESP32-CAM Workshop — booting…");

  // Initialise camera
  esp_err_t err = esp_camera_init(&camera_config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed: 0x%x\n", err);
    Serial.println("Check power supply and camera ribbon cable, then reset.");
    return;
  }
  Serial.println("Camera OK");

  // Connect to Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    if (millis() - start > 15000) {
      Serial.println("\nWi-Fi timeout. Check WIFI_SSID and WIFI_PASSWORD in secrets.h.");
      return;
    }
  }
  Serial.println("\nWi-Fi connected!");
  Serial.print("Camera IP:  http://");
  Serial.println(WiFi.localIP());
  Serial.print("Stream URL: http://");
  Serial.print(WiFi.localIP());
  Serial.println(":81/stream");
  Serial.print("Capture URL: http://");
  Serial.print(WiFi.localIP());
  Serial.println("/capture");

  startCameraServer();
  Serial.println("HTTP server started.");
}

void loop() {
  delay(10000);  // nothing to do — the HTTP server runs on its own tasks
}
