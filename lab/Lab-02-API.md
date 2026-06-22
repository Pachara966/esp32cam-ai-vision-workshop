# Lab 02 — REST API และ Backend Server
### ทำความเข้าใจการสื่อสารระหว่าง Client และ Server ผ่าน HTTP API

---

## วัตถุประสงค์ / Objectives

หลังจาก Lab นี้นักเรียนจะสามารถ:

- รัน FastAPI backend server ได้
- ส่งไฟล์รูปภาพไปยัง API และรับผลลัพธ์กลับมาได้
- เข้าใจโครงสร้าง HTTP Request / Response
- ทดสอบ API ด้วย Web UI ที่มีให้

> **ไม่ต้องใช้กล้อง ESP32-CAM** ใน Lab นี้ — เราจะใช้ Mock Provider แทน

---

## สิ่งที่ต้องเตรียม / Prerequisites

- Python 3.10 หรือสูงกว่าติดตั้งแล้ว (พิมพ์ `python --version` เพื่อตรวจสอบ)
- โฟลเดอร์ `code/server/` จาก repository นี้

---

## ขั้นตอน / Steps

### ขั้นที่ 1 — สร้าง Virtual Environment

เปิด Terminal (Command Prompt หรือ PowerShell) ไปที่โฟลเดอร์ `code/server/`:

```bash
cd code/server
python -m venv .venv
```

เปิดใช้งาน virtual environment:

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

เมื่อเปิดใช้งานแล้วจะเห็น `(.venv)` นำหน้า prompt

---

### ขั้นที่ 2 — ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

รอจนดาวน์โหลดและติดตั้งเสร็จ (ครั้งแรกอาจใช้เวลา 1-2 นาที)

---

### ขั้นที่ 3 — ตั้งค่า Environment Variables

คัดลอกไฟล์ `.env.example` แล้วตั้งชื่อใหม่เป็น `.env`:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

เปิดไฟล์ `.env` แล้วตรวจสอบว่าบรรทัดแรกเป็น:

```
VISION_PROVIDER=mock
```

ยังไม่ต้องใส่ API key — Mock Provider ไม่ต้องการ

---

### ขั้นที่ 4 — รัน Backend Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

ถ้าสำเร็จจะเห็น:

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process...
INFO:     Application startup complete.
```

---

### ขั้นที่ 5 — เปิด Web UI

เปิดเบราว์เซอร์ไปที่:

```
http://localhost:8000
```

จะเห็นหน้าเว็บ "ESP32-CAM AI Vision Workshop"

---

### ขั้นที่ 6 — ทดสอบ API ด้วยการ Upload รูป

1. คลิกปุ่ม **"📁 Upload Image"**
2. เลือกไฟล์รูปภาพ JPEG หรือ PNG จากโน้ตบุ๊ก
3. ดูผลลัพธ์ที่แสดงในส่วน "ผลการวิเคราะห์"

ผลที่ได้จาก Mock Provider จะมีรูปแบบประมาณ:

```
[Mock Provider — ไม่ใช้ API จริง]

ได้รับภาพขนาด 45.2 KB
Prompt ที่ได้รับ: "อธิบายสิ่งที่เห็นในภาพนี้..."

ผลการวิเคราะห์จำลอง: ภาพนี้มีวัตถุสีสันสดใส 3 ชิ้น ดูเหมือนจะอยู่ในสภาพดี
```

---

### ขั้นที่ 7 — ทำความเข้าใจ API (อ่านโค้ด)

เปิดไฟล์ `main.py` แล้วดูโครงสร้าง:

```python
# Route สำหรับ upload รูป
@app.post("/analyze-upload")
async def analyze_upload(file: UploadFile, prompt: str):
    image_bytes = await file.read()   # รับไฟล์รูป
    provider = get_provider()         # เลือก AI provider
    result = provider.analyze(image_bytes, prompt)  # ส่งให้ AI วิเคราะห์
    return {"result": result}
```

**คำถามเพื่อทบทวนความเข้าใจ:**
1. HTTP Method อะไรที่ใช้ส่งรูปภาพ? (GET หรือ POST?)
2. API return ข้อมูลในรูปแบบอะไร?
3. `provider.analyze()` รับ parameter อะไรบ้าง?

---

## เกณฑ์ความสำเร็จ / Success Criteria

- [ ] รัน server แล้วเห็น `Application startup complete`
- [ ] เปิด `http://localhost:8000` แล้วเห็นหน้าเว็บ
- [ ] Upload รูปแล้วได้รับผลจาก Mock Provider
- [ ] เข้าใจว่า HTTP POST ต่างจาก GET อย่างไร

---

## ศึกษาเพิ่มเติม / Explore

ลองเรียก API โดยตรงด้วย curl (ถ้ามี):

```bash
curl -X GET http://localhost:8000/prompts
curl -X GET http://localhost:8000/health
```

หรือเปิด interactive API docs ที่:
```
http://localhost:8000/docs
```

---

## สิ่งที่ได้เรียนรู้ / What You Learned

- FastAPI สร้าง HTTP API server ด้วย Python ได้รวดเร็ว
- REST API ใช้ HTTP Methods (GET, POST) แยกประเภทการร้องขอ
- Mock Provider ช่วยให้ทดสอบ pipeline ได้โดยไม่ต้องใช้ API จริง
- Virtual Environment แยก dependencies ของโปรเจกต์ออกจากกัน
