from abc import ABC, abstractmethod


class VisionProvider(ABC):
    """Abstract base for all Vision AI providers."""

    @abstractmethod
    def analyze(self, image_bytes: bytes, prompt: str) -> str:
        """Analyze image_bytes with the given prompt; return the AI's text response."""
        ...
