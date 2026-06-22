import os
from google import genai
from google.genai import types
from .base import VisionProvider


class GeminiProvider(VisionProvider):
    """Google Gemini Vision provider (google-genai SDK)."""

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set. "
                "Set it in your .env file or environment variables."
            )
        self.client = genai.Client(api_key=api_key)
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    def analyze(self, image_bytes: bytes, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
                prompt,
            ],
        )
        return response.text
