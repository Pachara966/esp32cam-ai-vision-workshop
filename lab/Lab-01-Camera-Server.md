# Lab 01 — ESP32-CAM Camera Server
### การติดตั้งกล้อง ESP32-CAM และเชื่อมต่อ Wi-Fi

---

## วัตถุประสงค์ / Objectives

หลังจาก Lab นี้นักเรียนจะสามารถ:

- ต่อสายและตั้งค่า ESP32-CAM กับ MB board ได้
- อัปโหลดโค้ดเข้า ESP32-CAM ผ่าน Arduino IDE ได้
- เปิดดู Live Stream จากกล้องในเบราว์เซอร์ได้
- เรียก URL `/capture` เพื่อดึงภาพเดี่ยวได้

---

## อุปกรณ์ที่ต้องใช้ / Hardware Required

| อุปกรณ์ | จำนวน |
|---------|------|
| ESP32-CAM (AI Thinker) | 1 |
| ESP32-CAM-MB (flashing board) | 1 |
| สาย Micro-USB | 1 |
| โน้ตบุ๊ก + Arduino IDE 2.x | 1 |

---

## ขั้นตอน / Steps

### ขั้นที่ 1 — ต่อ ESP32-CAM เข้ากับ MB Board

1. ต่อโมดูล ESP32-CAM เข้ากับ slot บน ESP32-CAM-MB ให้แน่น
   (สังเกต: ด้านที่มีกล้องชี้ออกจาก board)
2. เสียบสาย Micro-USB จากโน้ตบุ๊กเข้าที่ MB board
3. กด **IO0** button บน MB board ค้างไว้ แล้วกด **RST** (reset) หนึ่งครั้ง
   — นี่คือโหมด Flash (GPIO0 → LOW)
4. ปล่อยปุ่ม IO0

> **หมายเหตุ:** GPIO0 ต้องเป็น LOW ตอน boot เพื่อเข้าโหมด Flash
> ถ้าไม่กด IO0 ESP32 จะ boot ปกติแทนที่จะรับ firmware ใหม่

---

### ขั้นที่ 2 — ติดตั้ง Arduino IDE และ ESP32 Board Package

1. ดาวน์โหลด Arduino IDE 2.x จาก https://arduino.cc/en/software
2. เปิด **File → Preferences** ใส่ URL ต่อไปนี้ใน "Additional boards manager URLs":
   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
3. ไปที่ **Tools → Board → Boards Manager** ค้นหา `esp32` แล้วติดตั้ง "esp32 by Espressif Systems"
4. เลือก **Tools → Board → ESP32 Arduino → AI Thinker ESP32-CAM**
5. เลือก Port ที่ถูกต้อง (Tools → Port → COM?)

---

### ขั้นที่ 3 — เตรียมโค้ด Firmware

1. เปิดโฟลเดอร์ `code/firmware/CameraWebServer/` ในไฟล์ explorer
2. **คัดลอก** ไฟล์ `secrets.example.h` แล้วตั้งชื่อใหม่เป็น `secrets.h`
3. เปิด `secrets.h` แล้วแก้ไขข้อมูล Wi-Fi:

```cpp
#define WIFI_SSID     "ชื่อ_WiFi_ของคุณ"
#define WIFI_PASSWORD "รหัสผ่าน_WiFi"
```

4. เปิดไฟล์ `CameraWebServer.ino` ใน Arduino IDE

---

### ขั้นที่ 4 — อัปโหลด Firmware

1. ตรวจสอบว่า ESP32-CAM อยู่ในโหมด Flash (ทำซ้ำขั้นที่ 1 ถ้าจำเป็น)
2. คลิกปุ่ม **Upload** (→) ใน Arduino IDE
3. รอจนเห็นข้อความ `Leaving... Hard resetting via RTS pin...`
4. กด **RST** บน MB board อีกครั้งเพื่อ boot firmware ใหม่
5. เปิด **Serial Monitor** (Tools → Serial Monitor) ตั้ง baud rate = `115200`

คาดว่าจะเห็นข้อความประมาณนี้:

```
Camera OK
Wi-Fi connected!
Camera IP:  http://192.168.x.xx
Stream URL: http://192.168.x.xx:81/stream
Capture URL: http://192.168.x.xx/capture
HTTP server started.
```

📝 **จดบันทึก IP address ไว้ — จะใช้ใน Lab ถัดๆ ไป**

---

### ขั้นที่ 5 — ทดสอบในเบราว์เซอร์

เปิดเบราว์เซอร์บนโน้ตบุ๊กที่เชื่อมต่อ Wi-Fi เดียวกัน:

| URL | ผลที่ควรเห็น |
|-----|------------|
| `http://<IP>/` | หน้าสถานะ ESP32-CAM |
| `http://<IP>:81/stream` | Live video stream |
| `http://<IP>/capture` | ดาวน์โหลด JPEG เดี่ยว |

---

## เกณฑ์ความสำเร็จ / Success Criteria

- [ ] เห็น Serial Monitor แสดง IP address
- [ ] เปิด `http://<IP>:81/stream` แล้วเห็น video สด
- [ ] เปิด `http://<IP>/capture` แล้วได้รูป JPEG

---

## ปัญหาที่พบบ่อย / Troubleshooting

| ปัญหา | วิธีแก้ |
|-------|---------|
| Upload ล้มเหลว / ไม่เจอ port | กด IO0 + RST ก่อน upload ทุกครั้ง |
| `Camera init failed` | ตรวจสอบว่าติดตั้งกล้องแน่นดี / ลอง RST |
| ไม่เชื่อม Wi-Fi | ตรวจ SSID/Password ใน `secrets.h` (Wi-Fi ต้องเป็น 2.4 GHz) |
| Brownout reset | สาย USB หรือ power supply ไม่แรงพอ ลองเปลี่ยนสาย |

ดูเพิ่มเติมใน [Troubleshooting-Guide.md](Troubleshooting-Guide.md)

---

## สิ่งที่ได้เรียนรู้ / What You Learned

- ESP32-CAM ทำงานเป็น HTTP Server ได้โดยตรง
- Port 80 = Web UI, Port 81 = MJPEG Stream
- `/capture` คือ endpoint ที่ backend จะใช้ดึงภาพใน Lab ต่อๆ ไป
- Firmware ที่ flash แล้วจะใช้ตลอด Workshop — ไม่ต้อง flash อีก
