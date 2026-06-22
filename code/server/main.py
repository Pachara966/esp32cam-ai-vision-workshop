"""ESP32-CAM AI Vision Workshop — FastAPI Backend

Routes:
  GET  /              → serve static/index.html
  GET  /prompts       → list preset prompts
  POST /analyze       → fetch JPEG from ESP32-CAM /capture, then analyze
  POST /analyze-upload → analyze an uploaded JPEG (no hardware needed)
"""

import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

load_dotenv()

from vision import get_provider
from prompts import PRESETS

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="ESP32-CAM AI Vision Workshop", version="1.0.0")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


# ---------------------------------------------------------------------------
# Root
# ---------------------------------------------------------------------------

@app.get("/")
async def root():
    return FileResponse(str(STATIC_DIR / "index.html"))


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

@app.get("/prompts")
async def list_prompts():
    return JSONResponse(content=PRESETS)


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    return {"status": "ok", "vision_provider": os.getenv("VISION_PROVIDER", "mock")}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_provider(image_bytes: bytes, prompt: str) -> tuple[str, str]:
    """Instantiate provider and analyze. Returns (provider_name, result_text).
    Converts all provider/API exceptions into HTTPException 502 with a
    student-friendly Thai/English message."""
    try:
        provider = get_provider()
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    try:
        result = provider.analyze(image_bytes, prompt)
    except Exception as exc:
        name = type(exc).__name__
        msg = str(exc)
        # Quota / rate limit
        if any(k in msg.lower() for k in ("quota", "rate", "429", "resource_exhausted")):
            raise HTTPException(
                status_code=429,
                detail=(
                    "API quota exceeded / เกิน quota ของ API — "
                    "รอ 1 นาทีแล้วลองใหม่ หรือเปลี่ยนเป็น VISION_PROVIDER=mock ชั่วคราว"
                ),
            )
        # Auth / key problems
        if any(k in msg.lower() for k in ("api_key", "auth", "401", "403", "permission", "invalid")):
            raise HTTPException(
                status_code=401,
                detail=(
                    "API key invalid or missing / API key ไม่ถูกต้องหรือไม่ได้ตั้งค่า — "
                    "ตรวจสอบค่าใน .env"
                ),
            )
        # Model not found
        if any(k in msg.lower() for k in ("not found", "404", "no longer available")):
            raise HTTPException(
                status_code=502,
                detail=f"Model not found / โมเดลไม่พร้อมใช้งาน: {msg[:200]}",
            )
        # Generic fallback
        raise HTTPException(
            status_code=502,
            detail=f"AI provider error ({name}): {msg[:300]}",
        )

    return type(provider).__name__, result


# ---------------------------------------------------------------------------
# Analyze via ESP32-CAM
# ---------------------------------------------------------------------------

class AnalyzeRequest(BaseModel):
    cam_url: str = ""
    prompt: str = "อธิบายสิ่งที่เห็นในภาพนี้ / Describe what you see in this image."


@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    cam_url = req.cam_url.strip() or os.getenv("CAM_URL", "")
    if not cam_url:
        raise HTTPException(
            status_code=400,
            detail="cam_url is required (or set CAM_URL in .env)",
        )

    capture_url = cam_url.rstrip("/") + "/capture"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(capture_url)
            resp.raise_for_status()
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=502,
            detail=(
                f"Cannot reach ESP32-CAM at {capture_url} — "
                f"ตรวจสอบ IP และ Wi-Fi: {exc}"
            ),
        )
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"ESP32-CAM returned HTTP {exc.response.status_code}",
        )

    provider_name, result = _run_provider(resp.content, req.prompt)
    return {
        "provider": provider_name,
        "cam_url": cam_url,
        "image_size_bytes": len(resp.content),
        "result": result,
    }


# ---------------------------------------------------------------------------
# Analyze via file upload
# ---------------------------------------------------------------------------

@app.post("/analyze-upload")
async def analyze_upload(
    file: UploadFile = File(...),
    prompt: str = Form(
        default="อธิบายสิ่งที่เห็นในภาพนี้ / Describe what you see in this image."
    ),
):
    if file.content_type not in ("image/jpeg", "image/png", "image/webp"):
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}. Use JPEG, PNG, or WebP.",
        )

    image_bytes = await file.read()
    provider_name, result = _run_provider(image_bytes, prompt)
    return {
        "provider": provider_name,
        "filename": file.filename,
        "image_size_bytes": len(image_bytes),
        "result": result,
    }
