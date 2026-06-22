# Course Overview — ESP32-CAM AI Vision Workshop
### ภาพรวมหลักสูตร Workshop กล้อง AI ด้วย ESP32-CAM

---

## Learning Outcomes / ผลการเรียนรู้ที่คาดหวัง

เมื่อสิ้นสุด Workshop นักเรียนจะสามารถ:

1. **ติดตั้งและใช้งาน ESP32-CAM** — ต่อสายกับ MB board, flash firmware, เชื่อมต่อ Wi-Fi และดู live stream ในเบราว์เซอร์ได้
2. **อธิบาย REST API** — บอกความแตกต่างระหว่าง GET และ POST, อธิบาย request/response cycle ได้
3. **รัน Python Backend** — สร้าง virtual environment, ติดตั้ง dependencies, รัน FastAPI server ได้
4. **ใช้ Vision AI API** — ตั้งค่า API key, ส่งภาพให้ AI วิเคราะห์, อ่านและตีความผลลัพธ์ได้
5. **เขียน Prompt** — ออกแบบ prompt ที่เจาะจงเพื่อให้ AI ตอบในรูปแบบที่ต้องการได้
6. **สร้าง Mini Project** — นำความรู้ทั้งหมดมาสร้างระบบ AI Vision ที่ใช้งานได้จริงในหัวข้อที่สนใจ

---

## Workshop Schedule / ตารางเวลา Workshop

> Workshop 1 วัน (ประมาณ 6 ชั่วโมง รวมพัก)

| เวลา | กิจกรรม | Lab |
|------|---------|-----|
| 08:30–09:00 | ลงทะเบียน, รับอุปกรณ์, เปิดเครื่อง | — |
| 09:00–09:30 | บรรยาย: AI + IoT + Computer Vision คืออะไร | — |
| 09:30–10:30 | **Lab 01** — ติดตั้ง ESP32-CAM, Flash Firmware, ดู Live Stream | Lab 01 |
| 10:30–10:45 | พัก ☕ | — |
| 10:45–11:45 | **Lab 02** — รัน Backend Server, ทดสอบ API ด้วย Mock Provider | Lab 02 |
| 11:45–12:45 | พักกลางวัน 🍱 | — |
| 12:45–13:00 | บรรยาย: Prompt Engineering เบื้องต้น | — |
| 13:00–14:15 | **Lab 03** — ต่อ Vision AI จริง, วิเคราะห์ภาพจาก ESP32-CAM | Lab 03 |
| 14:15–14:30 | พัก | — |
| 14:30–15:45 | **Lab 04** — สร้าง Mini Project ของตัวเอง | Lab 04 |
| 15:45–16:00 | นำเสนอผลงาน, ถ่ายรูป, มอบใบประกาศ | — |

---

## Module Descriptions / รายละเอียดแต่ละ Module

### Module 1 — ESP32-CAM & IoT
**Lab 01 · เวลา: ~60 นาที**

นักเรียนจะได้เรียนรู้ว่า IoT (Internet of Things) คืออะไร และ ESP32-CAM ทำหน้าที่อะไร
ลงมือต่อสายกับ MB board, เขียน Wi-Fi credentials, flash firmware, และเปิด live stream

**เป้าหมาย:** กล้อง ESP32-CAM ส่ง live video ได้ และ endpoint `/capture` ทำงาน

---

### Module 2 — REST API & Backend Server
**Lab 02 · เวลา: ~60 นาที**

เรียนรู้หลักการ REST API — HTTP Method, Request, Response, JSON
รัน FastAPI backend บน laptop, ใช้ Mock Provider เพื่อเข้าใจ data flow โดยไม่ต้องใช้ API key

**เป้าหมาย:** เข้าใจว่าข้อมูล (ภาพ + prompt) เดินทางจาก client → server → AI → กลับมา UI อย่างไร

---

### Module 3 — Generative AI Vision
**Lab 03 · เวลา: ~75 นาที**

ต่อ API key จริง (Gemini หรือ Claude), เปลี่ยน `VISION_PROVIDER` ใน `.env`
ชี้กล้อง ESP32-CAM ไปที่สิ่งต่างๆ แล้วทดลองเปลี่ยน prompt สังเกตความแตกต่างของผลลัพธ์

**เป้าหมาย:** ส่งภาพจากกล้องจริงให้ AI วิเคราะห์ได้ และเข้าใจว่า prompt ส่งผลต่อคำตอบอย่างไร

---

### Module 4 — AI Vision Mini Project
**Lab 04 · เวลา: ~75 นาที**

เลือกหัวข้อโปรเจกต์ที่สนใจ 1 อย่าง เขียน/ปรับ prompt ให้เหมาะกับ use case
ทดสอบซ้ำจนพอใจ แล้วเตรียมนำเสนอให้เพื่อนและอาจารย์ฟัง

**เป้าหมาย:** มีระบบ AI Vision ที่ใช้งานได้จริงในชีวิตประจำวันอย่างน้อย 1 อย่าง

---

## Technology Stack

```
Hardware                Software               AI Services
─────────────          ─────────────          ─────────────────────
ESP32-CAM              Arduino IDE 2.x        Gemini 2.5 Flash
ESP32-CAM-MB           Python 3.10+           Claude Haiku 4.5
Notebook / PC          FastAPI + Uvicorn      (Mock Provider สำหรับ Lab 02)
Wi-Fi 2.4 GHz          google-genai SDK
                       anthropic SDK
```

---

## Workshop Flow Diagram

```
นักเรียน
   │
   ├─► [Lab 01] Flash ESP32-CAM
   │         │
   │         └─► Wi-Fi Connected → /capture endpoint ready
   │
   ├─► [Lab 02] Run FastAPI Backend
   │         │
   │         └─► localhost:8000 → Mock AI → เข้าใจ API flow
   │
   ├─► [Lab 03] Connect Real Vision AI
   │         │
   │         └─► ESP32-CAM → /capture → Backend → Gemini/Claude → Result
   │
   └─► [Lab 04] Mini Project
             │
             └─► Custom Prompt → Demo → นำเสนอ 🎉
```

---

## Prerequisites for Students / สิ่งที่นักเรียนควรรู้มาก่อน

- ใช้คอมพิวเตอร์เบื้องต้นได้ (เปิด-ปิดโปรแกรม, copy-paste)
- เคยเห็น/ได้ยินคำว่า AI มาบ้าง
- **ไม่จำเป็น** ต้องเขียนโปรแกรมมาก่อน

## Prerequisites for Instructors / สิ่งที่ผู้สอนต้องเตรียม

- ทดสอบ full workflow ก่อนวัน Workshop อย่างน้อย 1 วัน
- เตรียม API key (Gemini แนะนำ) สำรองไว้ให้นักเรียนที่ key ไม่ผ่าน
- ดู [Instructor-Guide.md](Instructor-Guide.md) สำหรับ checklist ครบถ้วน
