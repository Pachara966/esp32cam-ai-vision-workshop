import base64
import os
import anthropic
from .base import VisionProvider


class ClaudeProvider(VisionProvider):
    """Anthropic Claude Vision provider."""

    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY is not set. "
                "Set it in your .env file or environment variables."
            )
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = os.getenv("CLAUDE_MODEL", "claude-haiku-4-5")

    def analyze(self, image_bytes: bytes, prompt: str) -> str:
        image_data = base64.standard_b64encode(image_bytes).decode("utf-8")

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": image_data,
                            },
                        },
                        {"type": "text", "text": prompt},
                    ],
                }
            ],
        )
        return response.content[0].text
