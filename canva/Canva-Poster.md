# Canva Poster — ESP32-CAM AI Vision Workshop
### Workshop Poster Design Spec (A3 Portrait: 297 × 420 mm)

---

## Color Palette
| Role | Hex | Usage |
|------|-----|-------|
| Background | `#0D1B2A` | Full background |
| Primary Accent | `#00C8FF` | Headlines, borders, icons |
| Secondary Accent | `#FF7043` | Badges, call-to-action |
| White | `#FFFFFF` | Main text |
| Light | `#D0E4F5` | Body text |
| Gray | `#88A0B8` | Supporting text |

## Fonts
- **Thai:** Kanit Bold / Kanit Regular (Google Fonts — free)
- **English / Tech:** Inter Bold / Inter Regular (Google Fonts — free)
- **Code snippets:** Courier New or JetBrains Mono

---

## Layout Zones (top to bottom)

### Zone 1 — Header Bar (top 12%)
- Background: `#00C8FF` (full-width strip)
- Left logo area: RMUTT emblem / logo (placeholder — insert actual logo)
- Center: Text `"Workshop"` in white, Kanit Bold 14pt
- Right: Date placeholder `"[วันที่ / Date]"` in white, Inter 12pt

---

### Zone 2 — Title Block (12%–40%)
- Background: `#0D1B2A`
- **Main title TH (large):**
  ```
  การพัฒนากล้องอัจฉริยะ
  ด้วย ESP32-CAM
  และปัญญาประดิษฐ์
  ```
  Font: Kanit Bold, 42pt, White `#FFFFFF`

- **Subtitle EN (medium):**
  ```
  ESP32-CAM AI Vision Workshop
  From IoT Camera to Intelligent Image Analysis
  ```
  Font: Inter Bold, 20pt, Cyan `#00C8FF`

- **Decorative element:** Thin cyan horizontal line separating TH/EN titles

---

### Zone 3 — Key Info Boxes (40%–58%)
Three equal-width boxes side by side:

| Box 1 📅 | Box 2 📍 | Box 3 👥 |
|-----------|-----------|-----------|
| วันที่ / Date | สถานที่ / Venue | สำหรับ / For |
| `[วันที่]` | `[ห้อง / ชั้น]` | นักเรียนมัธยมศึกษา |
| Background: `#1E2D3D` | Background: `#1E2D3D` | Background: `#1E2D3D` |
| Border top: `#FF7043` | Border top: `#00C8FF` | Border top: `#FF7043` |

---

### Zone 4 — 4 Module Icons (58%–76%)
Four equal columns, each:
- Icon (large emoji or vector icon)
- Module number badge (orange circle)
- Short label TH + EN

| Lab 01 | Lab 02 | Lab 03 | Lab 04 |
|--------|--------|--------|--------|
| 📷 | ⚙️ | 🤖 | 🚀 |
| ESP32-CAM | REST API | AI Vision | Mini Project |
| กล้อง AI | Backend | วิเคราะห์ภาพ | โปรเจกต์ |

---

### Zone 5 — Tech Logos Row (76%–85%)
Horizontal row, centered, logos with white background pill:
- `Arduino` | `Python` | `FastAPI` | `Gemini` | `Claude`

Label below: "Technology Stack" — Inter 11pt, Gray

---

### Zone 6 — Footer (85%–100%)
- Background: `#FF7043` strip
- Left: QR Code placeholder `[QR → GitHub Repo]`
- Center: `"สมัครได้ที่ / Register at: [URL]"` — Kanit 13pt, White
- Right: RMUTT + Faculty name

---

## Canva Tips
- ใช้ Background color `#0D1B2A` เป็นพื้นหลังหลัก
- เพิ่ม subtle texture: noise overlay 5% opacity สำหรับ tech feel
- ใส่ grid dots pattern (white, 3% opacity) เป็น background texture
- Icons: ใช้ Canva Elements → search "circuit", "camera", "AI robot"
- Export: PDF Print (300 dpi) สำหรับพิมพ์ / PNG 150 dpi สำหรับ social
