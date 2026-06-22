import os
from .base import VisionProvider


def get_provider() -> VisionProvider:
    """Factory: reads VISION_PROVIDER env var and returns the correct provider.

    Supported values: mock (default), gemini, claude
    """
    name = os.getenv("VISION_PROVIDER", "mock").lower().strip()

    if name == "mock":
        from .mock_provider import MockProvider
        return MockProvider()

    if name == "gemini":
        from .gemini_provider import GeminiProvider
        return GeminiProvider()

    if name == "claude":
        from .claude_provider import ClaudeProvider
        return ClaudeProvider()

    raise ValueError(
        f"Unknown VISION_PROVIDER='{name}'. "
        "Choose one of: mock, gemini, claude"
    )
