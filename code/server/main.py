"""ESP32-CAM AI Vision Workshop — FastAPI Backend

Routes:
  GET  /              → serve static/index.html
  GET  /prompts       → list preset prompts
  POST /analyze       → fetch JPEG from ESP32-CAM /capture, then analyze
  POST /analyze-upload → analyze an uploaded JPEG (no hardware needed)
"""

import os
from contextlib import asynccontextmanager
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


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

app = FastAPI(title="ESP32-CAM AI Vision Workshop", version="1.0.0")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


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
# Analyze via ESP32-CAM
# ---------------------------------------------------------------------------

class AnalyzeRequest(BaseModel):
    cam_url: str = ""   # e.g. "http://192.168.1.50"
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
            detail=f"Cannot reach ESP32-CAM at {capture_url}: {exc}",
        )
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"ESP32-CAM returned {exc.response.status_code}",
        )

    image_bytes = resp.content
    provider = get_provider()
    result = provider.analyze(image_bytes, req.prompt)

    return {
        "provider": type(provider).__name__,
        "cam_url": cam_url,
        "image_size_bytes": len(image_bytes),
        "result": result,
    }


# ---------------------------------------------------------------------------
# Analyze via file upload (no hardware needed — perfect for Lab 02)
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
    provider = get_provider()
    result = provider.analyze(image_bytes, prompt)

    return {
        "provider": type(provider).__name__,
        "filename": file.filename,
        "image_size_bytes": len(image_bytes),
        "result": result,
    }


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    vision_provider = os.getenv("VISION_PROVIDER", "mock")
    return {"status": "ok", "vision_provider": vision_provider}
