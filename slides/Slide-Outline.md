# Slide Outline — ESP32-CAM AI Vision Workshop
### เนื้อหาทุก Slide (60 slides) สำหรับอ้างอิงและนำเข้า Canva

---

## SECTION 0 — OPENING

### Slide 01: Cover
- **Title EN:** ESP32-CAM AI Vision Workshop
- **Subtitle EN:** From IoT Camera to Intelligent Image Analysis
- **Title TH:** การพัฒนากล้องอัจฉริยะด้วย ESP32-CAM และปัญญาประดิษฐ์
- **Subtitle TH:** สำหรับการวิเคราะห์ภาพ
- **Org:** มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี (RMUTT)
- **Hashtag:** #ESP32CAM_AI_RMUTT
- *Design: dark navy, cyan top/bottom bar, orange side stripe*

### Slide 02: Workshop Overview
- **ในวันนี้เราจะสร้างอะไร?**
- Flow: 📷 ESP32-CAM → 📶 Wi-Fi → ⚙️ FastAPI Backend → 🤖 Vision AI → 📊 Result

### Slide 03: Learning Outcomes
1. ติดตั้งและใช้งาน ESP32-CAM — *Configure & Flash Firmware*
2. อธิบาย REST API — *Explain REST API & HTTP*
3. รัน Python Backend ด้วย FastAPI — *Run FastAPI Server*
4. ใช้ Vision AI API วิเคราะห์ภาพ — *Use Gemini / Claude Vision*
5. เขียน Prompt ที่เจาะจง — *Design Effective Prompts*
6. สร้าง AI Vision Mini Project — *Build a Real AI Project*

### Slide 04: Agenda
| เวลา | กิจกรรม |
|------|---------|
| 08:30–09:00 | ลงทะเบียน / รับอุปกรณ์ |
| 09:00–09:30 | Lecture: AI + IoT + Computer Vision |
| 09:30–10:30 | Lab 01 — ESP32-CAM |
| 10:30–10:45 | พัก ☕ |
| 10:45–11:45 | Lab 02 — REST API & Backend |
| 11:45–12:45 | พักกลางวัน 🍱 |
| 12:45–13:00 | Lecture: Prompt Engineering |
| 13:00–14:15 | Lab 03 — AI Vision |
| 14:15–14:30 | พัก |
| 14:30–15:45 | Lab 04 — Mini Project |
| 15:45–16:00 | นำเสนอผลงาน 🎉 |

---

## SECTION 1 — IoT & ESP32-CAM

### Slide 05: Section Header
- **Section 1** — IoT & ESP32-CAM
- อินเทอร์เน็ตของสรรพสิ่ง และกล้อง AI

### Slide 06: What is IoT?
- **IoT** = อุปกรณ์ที่เชื่อมต่ออินเทอร์เน็ตเพื่อส่ง/รับข้อมูล
- 🏠 Smart Home — หลอดไฟ, กล้องวงจรปิด, ล็อคประตู
- 🏭 Smart Factory — เซนเซอร์อุณหภูมิ, แรงสั่นสะเทือน
- 🌱 Smart Agriculture — กล้อง + AI วิเคราะห์โรคพืช

### Slide 07: ESP32-CAM Introduction
| Spec | Value |
|------|-------|
| CPU | ESP32 Dual-Core 240 MHz |
| RAM | 520 KB SRAM + 4 MB PSRAM |
| Flash | 4 MB |
| Camera | OV2640 2MP |
| Wi-Fi | 802.11 b/g/n 2.4 GHz |
| ราคา | ~150–250 บาท |

### Slide 08: Hardware Tour
- ส่วนประกอบ: OV2640 Camera, ESP32-WROVER SoC, GPIO0, 5V/GND, UART
- ⚠️ GPIO0 ต้องต่อ GND ขณะ flash
- ต่อผ่าน ESP32-CAM-MB (CH340)

### Slide 09: Wi-Fi & Networking Basics
- **SSID** — ชื่อ Wi-Fi → ใส่ใน secrets.h
- **Password** — รหัส Wi-Fi → ใส่ใน secrets.h
- **IP Address** — เช่น 192.168.1.50
- **Port** — Web UI: 80 • Stream: 81
- ⚠️ ใช้ 2.4 GHz เท่านั้น

---

## SECTION 2 — REST API & BACKEND

### Slide 10: Section Header
- **Section 2** — REST API & Backend
- การสื่อสารระหว่างอุปกรณ์กับ AI

### Slide 11: What is REST API?
- **ร้านอาหาร analogy:**
  - ลูกค้า = Client | พนักงาน = API | ครัว = Server
  - เมนู = Endpoints | ออเดอร์ = Request | อาหาร = Response

### Slide 12: HTTP GET vs POST
| GET | POST |
|-----|------|
| ขอดึงข้อมูล (Read) | ส่งข้อมูลไป (Send) |
| `GET /prompts` | `POST /analyze` |
| `GET /health` | `{ cam_url, prompt }` |
| ไม่มี body | มี JSON body |

### Slide 13: JSON Basics
```json
{
  "provider": "gemini",
  "filename": "photo.jpg",
  "image_size_bytes": 12480,
  "result": "ภาพแสดงโต๊ะทำงาน..."
}
```
- `{ }` = object | `[ ]` = array | key ใส่ `" "` เสมอ

### Slide 14: FastAPI Backend Overview
```
Browser → POST /analyze → FastAPI
                              ├── GET /capture → ESP32-CAM
                              └── AI Provider (mock/gemini/claude)
```
Routes: `/`, `/prompts`, `/analyze`, `/analyze-upload`, `/health`

---

## SECTION 3 — AI VISION

### Slide 15: Section Header
- **Section 3** — AI & Vision
- ปัญญาประดิษฐ์และการวิเคราะห์ภาพ

### Slide 16: What is AI?
- Rule-Based → กฎตายตัว IF-THEN
- Machine Learning → เรียนรู้จากตัวอย่าง
- **Generative AI** → สร้างคำตอบใหม่จากภาษาธรรมชาติ ← Workshop นี้

### Slide 17: Generative AI
- 📝 Text Generation — เขียนเรียงความ, สรุป, ตอบคำถาม
- 🖼️ Image Generation — Midjourney, DALL-E
- **👁️ Image Analysis — อธิบาย, จำแนก, นับ ← Workshop นี้!**
- 💻 Code Generation — เขียนโปรแกรมจาก requirements

### Slide 18: Vision AI
- 🔍 Object Detection — ระบุวัตถุ
- 🔢 Counting — นับจำนวน
- 🎨 Color / Scene — วิเคราะห์สี
- 📊 Classification — จำแนกประเภท
- 💚 Health Assessment — ประเมินสุขภาพ
- 📝 Text Reading (OCR) — อ่านตัวหนังสือ

### Slide 19: Gemini Vision (Google)
| | |
|---|---|
| Model | gemini-2.5-flash |
| API Key | aistudio.google.com (ฟรี) |
| Free Tier | 1,500 req/วัน |
| ENV | `VISION_PROVIDER=gemini` |
✅ แนะนำสำหรับ Workshop

### Slide 20: Claude Vision (Anthropic)
| | |
|---|---|
| Model | claude-haiku-4-5 |
| API Key | console.anthropic.com |
| Pricing | $1/M tokens input |
| ENV | `VISION_PROVIDER=claude` |
💡 เปลี่ยนได้ด้วย config เดียว

### Slide 21: Prompt Engineering
**สูตร:** `[Role] + [Task] + [Format] + [Language]`
- **Role** — "คุณคือผู้เชี่ยวชาญด้านสิ่งแวดล้อม"
- **Task** — "วิเคราะห์ขยะในภาพและจำแนกประเภท"
- **Format** — "ตอบเป็น bullet point"
- **Language** — "ภาษาไทย"

### Slide 22: AI Vision Workflow
```
👤 Web UI → POST /analyze → FastAPI
                 ├── GET /capture → 📷 ESP32-CAM
                 └── Vision Provider → 🤖 AI → JSON Result → 🌐 UI
```

---

## SECTION 4 — LAB 01

### Slide 23: Lab 01 Header
**LAB 01 — ESP32-CAM Camera Server**
- ติดตั้งกล้อง • Flash Firmware • ดู Live Stream
- เวลา: ~60 นาที

### Slide 24: Lab 01 Overview
✅ ต่อสาย ESP32-CAM + MB board
✅ ติดตั้ง Arduino IDE + ESP32 Board Package
✅ แก้ไข secrets.h
✅ Flash firmware
✅ ทดสอบ Live Stream + /capture

### Slide 25: Step 1 — Wire ESP32-CAM
- ESP32-CAM เสียบลง MB Board
- ⚠️ GPIO0 → GND ก่อน Upload
- หลัง Upload: ถอด jumper + กด RST

### Slide 26: Step 2 — Arduino IDE Setup
1. Preferences → Additional boards URL
2. Boards Manager → ติดตั้ง esp32
3. Board → AI Thinker ESP32-CAM
4. Port → COMx

### Slide 27: Step 3 — Edit secrets.h
```cpp
#define WIFI_SSID  "ชื่อ Wi-Fi"
#define WIFI_PASS  "รหัส Wi-Fi"
```
⚠️ secrets.h อยู่ใน .gitignore

### Slide 28: Step 4 — Flash Firmware
1. ตรวจ GPIO0 → GND
2. กด Upload
3. รอ "Writing at 0x..."
4. ถอด jumper → กด RST

### Slide 29: Step 5 — Find IP & Test
- Serial Monitor (115200 baud) → จด IP
- Browser: `http://<IP>` → Web UI
- Browser: `http://<IP>/capture` → JPEG
- Browser: `http://<IP>:81/stream` → Live

### Slide 30: Lab 01 Expected Result
✅ ESP32-CAM เชื่อม Wi-Fi สำเร็จ
✅ Serial Monitor แสดง IP
✅ Browser เปิดหน้า Web UI
✅ /capture ส่ง JPEG กลับ
✅ :81/stream แสดง Live Video

---

## SECTION 5 — LAB 02

### Slide 31: Lab 02 Header
**LAB 02 — REST API & Backend**
- รัน Backend • ทดสอบ API • Mock Provider
- เวลา: ~60 นาที

### Slide 32: Lab 02 Overview
✅ สร้าง Virtual Environment
✅ pip install dependencies
✅ ตั้งค่า .env (VISION_PROVIDER=mock)
✅ รัน uvicorn
✅ ทดสอบ upload รูป

### Slide 33: Step 1 — Create venv
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Slide 34: Step 2 — pip install
```bash
pip install -r requirements.txt
# fastapi, uvicorn, httpx, google-genai, anthropic...
```

### Slide 35: Step 3 — Configure .env
```env
VISION_PROVIDER=mock
GEMINI_API_KEY=your_key_here
CAM_URL=http://192.168.x.x
```

### Slide 36: Step 4 — Run Server
```bash
uvicorn main:app --reload --host 0.0.0.0
# → http://localhost:8000
# → /health: { "vision_provider": "mock" }
```

### Slide 37: Lab 02 Expected Result
✅ pip install ไม่มี error
✅ uvicorn รันที่ localhost:8000
✅ Web UI เปิดได้
✅ Upload รูป → mock response
✅ /health แสดง mock

---

## SECTION 6 — LAB 03

### Slide 38: Lab 03 Header
**LAB 03 — AI Vision Analysis**
- API Key จริง • ภาพจากกล้อง • Prompt Engineering
- เวลา: ~75 นาที

### Slide 39: Lab 03 Overview
✅ รับ Gemini API Key
✅ ตั้งค่า .env + restart
✅ Capture & Analyze ครั้งแรก
✅ ทดลอง prompt 3 แบบ

### Slide 40: Step 1 — Get API Key
1. aistudio.google.com
2. Sign in → Get API key → Create
3. วางใน .env: `GEMINI_API_KEY=AIza...`
- ⚠️ อย่าแชร์หรือ commit key

### Slide 41: Step 2 — Update .env & Restart
```env
VISION_PROVIDER=gemini
GEMINI_API_KEY=AIza...
CAM_URL=http://192.168.x.x
```
Restart: `Ctrl+C` แล้วรัน uvicorn ใหม่

### Slide 42: Step 3 — First Analysis
1. เปิด localhost:8000
2. กรอก cam_url
3. เลือก prompt
4. กด Capture & Analyze
5. รอ 2-5 วินาที → ดูผล

### Slide 43: Step 4 — Prompt Experiments
- Prompt A (กว้าง): "อธิบายสิ่งที่เห็นในภาพ"
- Prompt B (เจาะจง): "นับวัตถุแต่ละประเภท ตอบเป็น list"
- Prompt C (Role): "คุณคือผู้เชี่ยวชาญ ประเมิน 1-10"

### Slide 44: Lab 03 Expected Result
✅ /health แสดง gemini
✅ Gemini วิเคราะห์ภาพจริงสำเร็จ
✅ ทดลอง 3 prompt แตกต่างกัน
✅ เข้าใจว่า prompt ส่งผลต่อคำตอบ

---

## SECTION 7 — LAB 04

### Slide 45: Lab 04 Header
**LAB 04 — AI Vision Mini Project**
- เลือก Project • เขียน Prompt • สร้าง AI ของตัวเอง
- เวลา: ~75 นาที

### Slide 46: Lab 04 Overview
1. เลือกหัวข้อ
2. เขียน Prompt
3. ทดสอบ ≥ 3 ครั้ง
4. ปรับปรุง
5. นำเสนอ (2 นาที)

### Slide 47: Step 1 — Choose Project
- 🗑️ Waste Classification
- 🌿 Plant Health Analysis
- 🔢 Object Counting
- 🖥️ Desk Cleanliness
- 🔧 Equipment Detection
- 💡 หรือคิดขึ้นเองก็ได้!

### Slide 48: Step 2 — Write Prompt
```
คุณคือ [บทบาท]
วิเคราะห์ภาพนี้และ [task]
ตอบในรูปแบบ:
[หัวข้อ]: [ค่า]
สรุป: [ประโยค]
ตอบเป็นภาษาไทย
```

### Slide 49: Presentation Tips
- 🎯 Demo Live — ชี้กล้องจริง + กด Analyze
- 📝 แสดง Prompt — อธิบาย why
- 📊 แสดงผลลัพธ์ — AI ตอบอะไร
- 💡 สิ่งที่เรียนรู้ — takeaway

---

## SECTION 8 — MINI PROJECTS

### Slide 50: Section Header
- Mini Project Ideas — ไอเดียโปรเจกต์

### Slide 51–55: Per-Project Slides
*(แต่ละ slide มี prompt snippet + expected output — ดูใน generate_pptx.py)*
- 51: Waste Classification
- 52: Plant Health Analysis
- 53: Object Counting
- 54: Desk Cleanliness
- 55: Equipment Detection

---

## SECTION 9 — CLOSING

### Slide 56: Future Career Paths
- 🤖 AI Engineer
- 📡 IoT Developer
- 📊 Data Scientist
- 🤖 Robotics Engineer
- 🛡️ AI Safety Researcher
- 🚀 AI Product Manager

### Slide 57: Additional Resources
- Workshop GitHub: github.com/Pachara966/esp32cam-ai-vision-workshop
- Google AI Studio: aistudio.google.com
- Anthropic Console: console.anthropic.com
- FastAPI Docs: fastapi.tiangolo.com
- ESP32 Docs: docs.espressif.com
- ML Crash Course: developers.google.com/machine-learning/crash-course

### Slide 58: Summary
| Lab | สิ่งที่ทำ |
|-----|---------|
| Lab 01 | ติดตั้ง ESP32-CAM + Flash + Live Stream |
| Lab 02 | รัน FastAPI + ทำความเข้าใจ REST API |
| Lab 03 | เชื่อม Gemini Vision + Prompt Engineering |
| Lab 04 | สร้าง AI Vision Mini Project |

### Slide 59: Q&A
- Q&A / ถามได้เลยครับ

### Slide 60: Thank You
- ขอบคุณทุกคน! / Thank You!
- RMUTT | [ชื่อผู้สอน]
- github.com/Pachara966/esp32cam-ai-vision-workshop
- #ESP32CAM_AI_RMUTT
