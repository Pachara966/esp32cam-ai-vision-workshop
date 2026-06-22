"""Bilingual mini-project prompt presets.

Each preset has:
  - id: short identifier used in API / UI
  - name_th: Thai display name
  - name_en: English display name
  - prompt: the full bilingual prompt sent to the Vision AI
"""

PRESETS = [
    {
        "id": "waste",
        "name_th": "จำแนกขยะ",
        "name_en": "Waste Classification",
        "prompt": (
            "วิเคราะห์ภาพนี้และจำแนกขยะที่มองเห็นออกเป็นประเภท:\n"
            "- ขยะรีไซเคิล (กระดาษ, พลาสติก, โลหะ, แก้ว)\n"
            "- ขยะอินทรีย์ (เศษอาหาร, ใบไม้)\n"
            "- ขยะทั่วไป (ที่ไม่สามารถรีไซเคิลได้)\n"
            "- ขยะอันตราย (แบตเตอรี่, หลอดไฟ)\n\n"
            "Analyze this image and classify the visible waste into categories:\n"
            "- Recyclable (paper, plastic, metal, glass)\n"
            "- Organic (food scraps, leaves)\n"
            "- General waste (non-recyclable)\n"
            "- Hazardous (batteries, bulbs)\n\n"
            "ระบุจำนวน ประเภท และคำแนะนำในการทิ้งอย่างถูกต้อง "
            "/ State the count, category, and correct disposal advice."
        ),
    },
    {
        "id": "plant",
        "name_th": "วิเคราะห์สุขภาพต้นไม้",
        "name_en": "Plant Health Analysis",
        "prompt": (
            "วิเคราะห์สุขภาพของต้นไม้ในภาพนี้:\n"
            "- สีของใบ (เขียวสด / เหลือง / น้ำตาล / มีจุด)\n"
            "- สัญญาณโรคหรือแมลง\n"
            "- ความชื้นของดิน (ถ้ามองเห็น)\n"
            "- ระดับสุขภาพโดยรวม (ดี / ปานกลาง / ต้องการการดูแล)\n\n"
            "Analyze the plant health in this image:\n"
            "- Leaf color (healthy green / yellow / brown / spotted)\n"
            "- Signs of disease or pests\n"
            "- Soil moisture (if visible)\n"
            "- Overall health rating (Good / Fair / Needs Care)\n\n"
            "ให้คำแนะนำในการดูแล / Provide care recommendations."
        ),
    },
    {
        "id": "count",
        "name_th": "นับจำนวนวัตถุ",
        "name_en": "Object Counting",
        "prompt": (
            "นับจำนวนวัตถุทุกชิ้นในภาพนี้อย่างละเอียด:\n"
            "- ระบุประเภทของวัตถุแต่ละชนิด\n"
            "- นับจำนวนของแต่ละประเภท\n"
            "- รวมจำนวนทั้งหมด\n\n"
            "Count all objects visible in this image:\n"
            "- Identify each type of object\n"
            "- Count the quantity of each type\n"
            "- Provide a total count\n\n"
            "ตอบในรูปแบบ: [ประเภท]: [จำนวน] / Answer as: [type]: [count]"
        ),
    },
    {
        "id": "classroom",
        "name_th": "ตรวจสอบห้องเรียน",
        "name_en": "Classroom Monitoring",
        "prompt": (
            "วิเคราะห์สภาพห้องเรียนในภาพนี้:\n"
            "- จำนวนคนที่มองเห็น (ถ้ามี)\n"
            "- ระดับความเป็นระเบียบของห้อง (ดี / พอใช้ / ต้องปรับปรุง)\n"
            "- อุปกรณ์ที่มองเห็น (โต๊ะ เก้าอี้ กระดาน คอมพิวเตอร์ ฯลฯ)\n"
            "- สภาพแสงสว่าง\n"
            "- ข้อสังเกตพิเศษ\n\n"
            "Analyze the classroom shown in this image:\n"
            "- Number of people visible (if any)\n"
            "- Room organization level (Good / Fair / Needs Improvement)\n"
            "- Visible equipment (desks, chairs, board, computers, etc.)\n"
            "- Lighting conditions\n"
            "- Special observations"
        ),
    },
    {
        "id": "desk",
        "name_th": "ประเมินความเป็นระเบียบของโต๊ะ",
        "name_en": "Desk Cleanliness Inspection",
        "prompt": (
            "ประเมินความเป็นระเบียบและความสะอาดของโต๊ะในภาพ:\n"
            "- ระดับความเป็นระเบียบ (1-5 ดาว)\n"
            "- สิ่งของที่วางบนโต๊ะ\n"
            "- จุดที่ต้องปรับปรุง\n"
            "- คะแนนความสะอาดโดยรวม\n\n"
            "Evaluate the tidiness and cleanliness of the desk in this image:\n"
            "- Organization rating (1-5 stars)\n"
            "- Items visible on the desk\n"
            "- Areas that need improvement\n"
            "- Overall cleanliness score\n\n"
            "ให้คำแนะนำเพื่อปรับปรุง / Provide improvement suggestions."
        ),
    },
]

# Quick lookup by id
PRESETS_BY_ID = {p["id"]: p for p in PRESETS}
