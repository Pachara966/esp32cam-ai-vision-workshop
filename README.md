# ESP32-CAM AI Vision Workshop

> **สร้างระบบกล้อง AI ด้วย ESP32-CAM และ Generative AI**
> **Build Intelligent Camera Systems with ESP32-CAM and Generative AI**

Workshop ระยะสั้น 1 วัน สำหรับนักเรียนมัธยมศึกษา มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี (RMUTT)
*One-day hands-on workshop for high-school students at Rajamangala University of Technology Thanyaburi (RMUTT)*

---

## ภาพรวม / Overview

Workshop นี้สอนให้นักเรียนรู้จักกับ:

- **Internet of Things (IoT)** — เชื่อมต่ออุปกรณ์กับอินเทอร์เน็ต
- **Computer Vision** — ให้คอมพิวเตอร์ "มองเห็น" และวิเคราะห์ภาพ
- **REST API** — การสื่อสารระหว่างอุปกรณ์และบริการบนคลาวด์
- **Generative AI** — ใช้โมเดล AI ที่ทันสมัยวิเคราะห์และอธิบายภาพ
- **Prompt Engineering** — ออกแบบคำสั่งให้ AI ทำงานได้ตรงตามต้องการ

นักเรียนจะสร้างระบบกล้อง AI ที่สามารถมองเห็น วิเคราะห์ นับ และตอบคำถามเกี่ยวกับภาพได้จริงภายใน 1 วัน

---

## Learning Objectives

Participants will learn how to:

- Configure ESP32-CAM hardware and connect to Wi-Fi
- Capture images and serve them via HTTP
- Send image data through REST APIs
- Use Vision AI models (Gemini Vision / Claude Vision) for image analysis
- Design effective prompts for different analysis tasks
- Build AI-powered mini projects from a real use-case idea

แนวทางการสอน: **Learning by Doing** + **Project-Based Learning** (ไม่มีการสอบ)

---

## Workshop Modules

| Module | หัวข้อ | เนื้อหา |
|--------|--------|---------|
| **Lab 01** | ESP32-CAM & IoT | ติดตั้งกล้อง เชื่อม Wi-Fi ดูภาพ live stream |
| **Lab 02** | REST API | รัน backend server ทดสอบ API ด้วยรูปตัวอย่าง |
| **Lab 03** | AI Vision | ต่อ API key จริง วิเคราะห์ภาพจากกล้อง ESP32 |
| **Lab 04** | Mini Project | เลือกโปรเจกต์ ปรับ prompt สร้างระบบ AI ของตัวเอง |

---

## Technology Stack

**Hardware**
- ESP32-CAM (AI Thinker module)
- ESP32-CAM-MB (USB flashing board)
- Notebook / PC
- Wi-Fi Network (2.4 GHz)

**Software**
- Arduino IDE 2.x
- Python 3.10+
- FastAPI + Uvicorn
- `google-generativeai` / `anthropic` SDK

**AI Services**
- Google Gemini Vision API (`gemini-2.0-flash`)
- Anthropic Claude Vision API (`claude-haiku-4-5`)

---

## Repository Structure

```
esp32cam-ai-vision-workshop/
├── code/
│   ├── firmware/CameraWebServer/   # ESP32-CAM Arduino sketch
│   └── server/                     # FastAPI backend + Vision AI providers
├── lab/                            # Bilingual lab manuals (Labs 01–04 + Troubleshooting)
├── docs/                           # Curriculum & reference docs
├── slides/                         # Presentation slides (Canva/PowerPoint)
├── images/                         # Workshop photos & diagrams
├── canva/                          # Canva poster, banner, certificate templates
└── resources/                      # Datasheets, links, cheat sheets
```

---

## Mini Project Ideas

นักเรียนสามารถเลือกโปรเจกต์ที่สนใจ:

1. **Waste Classification** — จำแนกประเภทขยะ (รีไซเคิล / ทั่วไป / อินทรีย์)
2. **Plant Health Analysis** — วิเคราะห์สุขภาพต้นไม้จากใบและสี
3. **Object Counting** — นับจำนวนวัตถุในภาพ
4. **Classroom Monitoring** — ตรวจสอบสภาพห้องเรียน (มีคน / ว่าง / สกปรก)
5. **Desk Cleanliness Inspection** — ประเมินความเป็นระเบียบของโต๊ะทำงาน

---

## Workshop Flow

```
ESP32-CAM
    │ (Wi-Fi)
    ▼
/capture endpoint  ──► FastAPI Backend
                            │
                            ▼
                    Vision AI (Gemini / Claude)
                            │
                            ▼
                    Web UI — แสดงภาพ + ผลวิเคราะห์
```

---

## Quick Start (Instructor)

```bash
# 1. Clone repo
git clone https://github.com/pachara-s/esp32cam-ai-vision-workshop.git
cd esp32cam-ai-vision-workshop

# 2. Flash firmware (Lab 01)
#    Open code/firmware/CameraWebServer/CameraWebServer.ino in Arduino IDE
#    Copy secrets.example.h → secrets.h and fill Wi-Fi credentials
#    Select board: AI Thinker ESP32-CAM, then Upload

# 3. Run backend
cd code/server
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env                             # edit VISION_PROVIDER and API keys
uvicorn main:app --reload --host 0.0.0.0

# 4. Open browser → http://localhost:8000
```

ดูรายละเอียดเพิ่มเติมใน [`lab/Lab-01-Camera-Server.md`](lab/Lab-01-Camera-Server.md)

---

## License

**Educational Use Only**
เนื้อหานี้จัดทำเพื่อการศึกษาใน Workshop ของ RMUTT เท่านั้น
