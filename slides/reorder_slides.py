"""
reorder_slides.py
จัดเรียง index_v2.html ใหม่:
  Section 1 → Lab 01 → Section 2 → Lab 02 → Section 3 → Lab 03 → Lab 04 → Mini Projects → Closing
"""
import re
from pathlib import Path

src = Path(__file__).parent / "index_v2.html"
content = src.read_text(encoding="utf-8")

# Split on each major divider comment (<!-- ═══...  )
# Each block starts with the divider and ends just before the next one
parts = re.split(r'(?=<!-- ═{10,})', content)

# parts[0]  = <head> + CSS + <body><div class="reveal"><div class="slides">
# parts[1]  = SECTION 0 — OPENING        (slides 01-04)
# parts[2]  = SECTION 1 — IoT            (slides 05-09)
# parts[3]  = SECTION 2 — REST API       (slides 10-14)
# parts[4]  = SECTION 3 — AI VISION      (slides 15-22)
# parts[5]  = SECTION 4 — LAB 01         (slides 23-30)
# parts[6]  = SECTION 5 — LAB 02         (slides 31-37)
# parts[7]  = SECTION 6 — LAB 03         (slides 38-44)
# parts[8]  = SECTION 7 — LAB 04         (slides 45-49)
# parts[9]  = SECTION 8 — MINI PROJECTS  (slides 50-55)
# parts[10] = SECTION 9 — CLOSING        (slides 56-60) + </div></div></body></html>

print(f"Found {len(parts)} parts:")
for i, p in enumerate(parts):
    preview = p[:120].replace('\n', ' ').strip().encode('ascii', 'replace').decode()
    print(f"  [{i}] {preview[:100]}")

assert len(parts) == 11, f"Expected 11 parts, got {len(parts)}"

new_content = "".join([
    parts[0],   # head + CSS + opening tags
    parts[1],   # Opening (slides 01-04)
    parts[2],   # Section 1 — IoT (slides 05-09)
    parts[5],   # Lab 01 (slides 23-30)
    parts[3],   # Section 2 — REST API (slides 10-14)
    parts[6],   # Lab 02 (slides 31-37)
    parts[4],   # Section 3 — AI Vision (slides 15-22)
    parts[7],   # Lab 03 (slides 38-44)
    parts[8],   # Lab 04 (slides 45-49)
    parts[9],   # Mini Projects (slides 50-55)
    parts[10],  # Closing (slides 56-60) + closing tags
])

src.write_text(new_content, encoding="utf-8")
print("\nDone — index_v2.html reordered.")
