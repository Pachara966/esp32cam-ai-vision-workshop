from .base import VisionProvider


class MockProvider(VisionProvider):
    """Returns a canned response — no API key needed. Great for Lab 02."""

    def analyze(self, image_bytes: bytes, prompt: str) -> str:
        kb = len(image_bytes) / 1024
        return (
            f"[Mock Provider — ไม่ใช้ API จริง]\n\n"
            f"ได้รับภาพขนาด {kb:.1f} KB\n"
            f"Prompt ที่ได้รับ: \"{prompt}\"\n\n"
            f"ผลการวิเคราะห์จำลอง: ภาพนี้มีวัตถุสีสันสดใส 3 ชิ้น "
            f"ดูเหมือนจะอยู่ในสภาพดี ไม่พบความผิดปกติ\n\n"
            f"[Mock result] Image received ({kb:.1f} KB). "
            f"Simulated analysis: 3 colorful objects detected, all in good condition."
        )
