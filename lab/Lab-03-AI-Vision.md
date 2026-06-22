# Lab 03 — AI Vision with Real API
### ต่อ Vision AI จริงและวิเคราะห์ภาพจาก ESP32-CAM

---

## วัตถุประสงค์ / Objectives

หลังจาก Lab นี้นักเรียนจะสามารถ:

- ตั้งค่า API key ของ Gemini Vision หรือ Claude Vision ได้
- สั่งให้ backend ดึงภาพจาก ESP32-CAM แล้วส่งวิเคราะห์ด้วย AI จริงได้
- ทดสอบและปรับแต่ง Prompt เพื่อให้ได้ผลลัพธ์ที่ดีขึ้นได้

---

## สิ่งที่ต้องเตรียม / Prerequisites

- ทำ Lab 01 (ESP32-CAM ทำงานแล้ว มี IP address)
- ทำ Lab 02 (Backend server รันได้แล้ว)
- API Key จาก Google AI Studio **หรือ** Anthropic Console

---

## ขั้นที่ 1 — รับ API Key

**ตัวเลือก A — Google Gemini (แนะนำสำหรับผู้เริ่มต้น)**

1. ไปที่ https://aistudio.google.com/app/apikey
2. คลิก **"Create API key"**
3. คัดลอก API key (ขึ้นต้นด้วย `AIza...`)

**ตัวเลือก B — Anthropic Claude**

1. ไปที่ https://console.anthropic.com/
2. สร้าง account แล้วไปที่ **API Keys**
3. คลิก **"Create Key"** แล้วคัดลอก

---

## ขั้นที่ 2 — ตั้งค่า .env

เปิดไฟล์ `code/server/.env` แล้วแก้ไข:

**ถ้าใช้ Gemini:**

```env
VISION_PROVIDER=gemini
GEMINI_API_KEY=AIza_ใส่_key_ของคุณ_ที่นี่
```

**ถ้าใช้ Claude:**

```env
VISION_PROVIDER=claude
ANTHROPIC_API_KEY=sk-ant-ใส่_key_ของคุณ_ที่นี่
```

> **ความปลอดภัย:** ไม่แชร์ API key ให้ผู้อื่น และอย่า commit ไฟล์ `.env` ขึ้น GitHub

---

## ขั้นที่ 3 — Restart Backend Server

หยุด server (กด `Ctrl+C`) แล้วรันใหม่:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

ตรวจสอบว่า `Provider` ใน UI เปลี่ยนเป็น `gemini` หรือ `claude`
(หรือดูที่ `http://localhost:8000/health`)

---

## ขั้นที่ 4 — วิเคราะห์ภาพจาก ESP32-CAM

1. เปิด Web UI ที่ `http://localhost:8000`
2. ใส่ IP address ของ ESP32-CAM จาก Lab 01 ใน "ESP32-CAM URL":
   ```
   http://192.168.x.xx
   ```
3. ใส่ prompt (หรือเลือก preset)
4. คลิก **"📷 Capture & Analyze"**

Backend จะ:
1. ดึง JPEG จาก `http://<IP>/capture`
2. ส่งภาพ + prompt ไปยัง Gemini/Claude
3. รับผลการวิเคราะห์กลับมาแสดง

---

## ขั้นที่ 5 — ทดลอง Prompt Engineering

ลองเปลี่ยน prompt และสังเกตผลลัพธ์:

**Prompt แบบกว้าง (ผลลัพธ์ทั่วไป):**
```
อธิบายสิ่งที่เห็นในภาพ
```

**Prompt แบบเจาะจง (ผลลัพธ์แม่นยำกว่า):**
```
มีวัตถุกี่ชิ้นในภาพ? ระบุชื่อและสีของแต่ละชิ้น
```

**Prompt แบบกำหนด format ผลลัพธ์:**
```
วิเคราะห์ภาพและตอบในรูปแบบ JSON:
{"objects": [...], "count": 0, "notes": "..."}
```

**คำถามทดลอง:**
- Prompt ที่ยาวกว่าให้ผลดีกว่าเสมอหรือไม่?
- การระบุภาษาที่ต้องการตอบกลับมาช่วยได้อย่างไร?
- ลองชี้กล้องไปที่สิ่งต่างๆ แล้วดูว่า AI อธิบายได้ถูกต้องแค่ไหน

---

## เกณฑ์ความสำเร็จ / Success Criteria

- [ ] ตั้งค่า API key ใน `.env` ได้สำเร็จ
- [ ] กดปุ่ม Capture & Analyze แล้วได้ผลจาก AI จริง (ไม่ใช่ Mock)
- [ ] ลองปรับ prompt อย่างน้อย 3 แบบ และเปรียบเทียบผล
- [ ] สามารถอธิบายได้ว่า prompt ส่งผลต่อคำตอบของ AI อย่างไร

---

## สิ่งที่ได้เรียนรู้ / What You Learned

- Vision AI models สามารถวิเคราะห์รูปภาพจริงได้ผ่าน API
- Prompt Engineering คือทักษะสำคัญในการใช้ AI ให้มีประสิทธิภาพ
- Backend ทำหน้าที่เป็นตัวกลาง ดึงภาพจาก IoT device และส่งต่อให้ AI
- API key คือ "กุญแจ" ที่ต้องเก็บรักษาให้ปลอดภัย
