import os
import google.generativeai as genai
from .base import VisionProvider


class GeminiProvider(VisionProvider):
    """Google Gemini Vision provider."""

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set. "
                "Set it in your .env file or environment variables."
            )
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        self.model = genai.GenerativeModel(model_name)

    def analyze(self, image_bytes: bytes, prompt: str) -> str:
        import google.generativeai as genai_types

        image_part = {"mime_type": "image/jpeg", "data": image_bytes}
        response = self.model.generate_content([prompt, image_part])
        return response.text
