# Troubleshooting Guide — ESP32-CAM AI Vision Workshop

คู่มือแก้ปัญหาที่พบบ่อย สำหรับผู้เข้าร่วมและผู้สอน

---

## ปัญหาการ Flash Firmware (Lab 01)

### ❌ Arduino IDE ไม่เห็น COM Port

**สาเหตุ:** ไดรเวอร์ USB-to-Serial (CH340 หรือ CP2102) ยังไม่ได้ติดตั้ง

**วิธีแก้:**
1. เปิด Device Manager (Windows) ดูว่ามีอุปกรณ์ที่มี `!` เหลืองไหม
2. ดาวน์โหลดและติดตั้งไดรเวอร์:
   - CH340: https://www.wch-ic.com/downloads/CH341SER_EXE.html
   - CP2102: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers
3. ถอดและเสียบสาย USB ใหม่
4. Restart Arduino IDE

---

### ❌ Upload ล้มเหลว — `A fatal error occurred: Failed to connect`

**สาเหตุ:** ESP32-CAM ไม่ได้อยู่ในโหมด Flash

**วิธีแก้:**
1. **กด IO0 button ค้างไว้** บน MB board
2. **กด RST** (reset) 1 ครั้ง แล้วปล่อย
3. **ยังคง IO0 ค้างไว้** จนกว่า Arduino IDE จะเริ่ม Upload
4. ปล่อย IO0

> หมายเหตุ: GPIO0 ต้องเป็น LOW ตอน boot เพื่อเข้าโหมด Flash

---

### ❌ `Camera init failed: 0x20001`

**สาเหตุ:** กล้องต่อไม่แน่น หรือสายแพ ribbon หลวม

**วิธีแก้:**
1. ถอด ESP32-CAM ออกจาก MB board แล้วเสียบใหม่ให้แน่น
2. ตรวจสอบว่า connector สายแพกล้องล็อคอยู่
3. ลอง RST button อีกครั้ง
4. ถ้ายังไม่หาย ลองใช้บอร์ดหรือกล้องสำรอง

---

### ❌ Brownout detected — ESP32 รีสตาร์ทซ้ำ

**สาเหตุ:** แหล่งจ่ายไฟไม่พอ (กล้องใช้ไฟสูงสุด ~300 mA)

**วิธีแก้:**
1. เปลี่ยนสาย USB ให้หนาขึ้น (ไม่ใช่สายชาร์จบาง)
2. ใช้ port USB ด้านหลังของ PC แทน USB Hub
3. ถ้าใช้ MB board ให้ตรวจสอบว่าต่อ USB ตรงกับ MB ไม่ใช่ ESP32

---

## ปัญหาการเชื่อมต่อ Wi-Fi (Lab 01)

### ❌ Wi-Fi ไม่เชื่อมต่อ — หมดเวลา 15 วินาที

**วิธีตรวจสอบ:**
1. เปิด Serial Monitor ดูข้อความ error
2. ตรวจสอบ `WIFI_SSID` และ `WIFI_PASSWORD` ใน `secrets.h`
   - ตัวพิมพ์เล็ก/ใหญ่สำคัญ
   - ห้ามมีช่องว่างที่หัวหรือท้าย
3. **ESP32-CAM รองรับเฉพาะ Wi-Fi 2.4 GHz** — ไม่รองรับ 5 GHz
4. ถ้าใช้ hotspot มือถือ ให้ตั้งเป็น 2.4 GHz

---

### ❌ เห็น IP แต่เข้าเว็บไม่ได้จากโน้ตบุ๊ก

**วิธีแก้:**
1. ตรวจสอบว่าโน้ตบุ๊กเชื่อมต่อ Wi-Fi เดียวกันกับ ESP32-CAM
2. ปิด Windows Firewall ชั่วคราว หรือเพิ่ม exception สำหรับ port 80 และ 81
3. ลอง ping IP ของ ESP32-CAM: `ping 192.168.x.xx`
4. ลองเปิดใน browser tab ใหม่โดยพิมพ์ IP ตรงๆ

---

## ปัญหา Backend Server (Lab 02)

### ❌ `ModuleNotFoundError` เมื่อรัน uvicorn

**วิธีแก้:**
1. ตรวจสอบว่า virtual environment เปิดอยู่ — ต้องเห็น `(.venv)` ใน terminal
2. ถ้าไม่มี ให้รัน:
   ```bash
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate # macOS/Linux
   ```
3. ติดตั้ง dependencies อีกครั้ง:
   ```bash
   pip install -r requirements.txt
   ```

---

### ❌ `Address already in use` — port 8000 ถูกใช้งานแล้ว

**วิธีแก้:**
1. ปิด terminal เก่าที่รัน server อยู่
2. หรือใช้ port อื่น:
   ```bash
   uvicorn main:app --reload --port 8001
   ```

---

### ❌ Backend รัน แต่กดปุ่ม Analyze แล้ว Error "Cannot reach ESP32-CAM"

**สาเหตุ:** Backend บน localhost ติดต่อ ESP32-CAM ไม่ได้ (คนละ subnet หรือ firewall)

**วิธีแก้:**
1. รัน server ด้วย `--host 0.0.0.0` (ไม่ใช่ default `127.0.0.1`)
2. ตรวจสอบ IP ของ ESP32-CAM ใน Serial Monitor อีกครั้ง
3. ทดสอบเปิด `http://<IP>/capture` จาก browser ก่อน — ถ้าได้รูปแสดงว่า ESP32 OK

---

## ปัญหา API Key (Lab 03)

### ❌ `GEMINI_API_KEY is not set`

**วิธีแก้:**
1. ตรวจสอบว่าไฟล์ `.env` อยู่ใน `code/server/` (ไม่ใช่ที่อื่น)
2. ตรวจสอบว่า key ไม่มีช่องว่างหรือ quote รอบๆ:
   ```
   GEMINI_API_KEY=AIzaSy...   ✅ ถูก
   GEMINI_API_KEY="AIzaSy..."  ❌ ผิด (มี quotes)
   ```
3. Restart server หลังแก้ไข `.env`

---

### ❌ API Error `429 Resource Exhausted` / `RATE_LIMIT_EXCEEDED`

**สาเหตุ:** เกิน quota ฟรีของ API

**วิธีแก้:**
1. รอ 1 นาทีแล้วลองใหม่
2. ใช้ Mock provider ชั่วคราวในระหว่างรอ: ตั้ง `VISION_PROVIDER=mock`
3. ถ้าทำ Lab เป็นกลุ่ม ให้ใช้ key เดียวกันผลัดกัน

---

### ❌ ผลการวิเคราะห์ไม่ตรงกับความเป็นจริง

**นี่คือปัญหาด้าน Prompt Engineering ไม่ใช่ bug**

**วิธีปรับปรุง:**
1. ระบุ task ให้ชัดเจนขึ้นใน prompt
2. บอกรูปแบบที่ต้องการตอบ
3. ลองเพิ่ม context ว่ากล้องอยู่ที่ไหนหรือมองอะไร
4. ตรวจสอบแสงสว่าง — ภาพมืดเกินไปทำให้ AI วิเคราะห์ผิดพลาด

---

## เคล็ดลับสำหรับผู้สอน / Instructor Tips

- **เตรียมสำรอง:** มี MB board และกล้องสำรองไว้อย่างน้อย 1-2 ชุด
- **Network:** ใช้ Wi-Fi AP แยกสำหรับ workshop — ป้องกัน VLAN isolation ของ Wi-Fi มหาวิทยาลัย
- **API Quota:** ถ้านักเรียนหลายคนใช้ key เดียวกัน ให้สลับกัน หรือใช้ Mock ระหว่างรอ
- **Power:** ใช้ USB Hub ที่มี adapter จ่ายไฟแยก ไม่ใช่ USB Hub แบบ bus-powered
- **ทดสอบก่อน:** ทดสอบ full workflow ก่อน workshop อย่างน้อย 1 วัน
