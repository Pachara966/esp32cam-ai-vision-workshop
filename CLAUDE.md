# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

This is an ESP32-CAM AI Vision workshop developed for Rajamangala University of Technology Thanyaburi (RMUTT). The workshop teaches participants to use ESP32-CAM hardware with AI-based image recognition and computer vision.

## Project Structure

This repository uses a hybrid layout — concept's top-level folders with code nested under `code/`:

```
├── README.md
├── LICENSE
├── .gitignore
├── code/
│   ├── firmware/
│   │   └── CameraWebServer/        # Arduino sketch (CameraWebServer.ino, camera_pins.h, secrets.example.h)
│   └── server/                     # FastAPI backend
│       ├── main.py                 # API routes
│       ├── vision/                 # Provider-agnostic Vision AI (mock / gemini / claude)
│       ├── prompts.py              # Bilingual preset prompts
│       ├── static/                 # Web UI (index.html, app.js)
│       ├── requirements.txt
│       └── .env.example
├── lab/                            # Bilingual lab manuals (Labs 01–04 + Troubleshooting)
├── docs/                           # Curriculum docs (placeholder)
├── slides/                         # Presentation slides (placeholder)
├── images/                         # Workshop photos & diagrams (placeholder)
├── canva/                          # Canva templates (placeholder)
└── resources/                      # Datasheets & links
```

## Development Environment

**Firmware (ESP32-CAM):**
- Toolchain: Arduino IDE 2.x
- Board: AI Thinker ESP32-CAM (select in Tools → Board)
- Flash via ESP32-CAM-MB board (CH340 USB-to-Serial) — the ESP32-CAM has no built-in USB

**AI/ML Backend (Python/FastAPI):**
- Use a virtual environment: `python -m venv .venv && .venv\Scripts\activate`
- Install deps: `pip install -r requirements.txt`
- Run server: `uvicorn main:app --reload --host 0.0.0.0`
- Copy `.env.example` → `.env`; set `VISION_PROVIDER` to `mock`, `gemini`, or `claude`

**Secrets — never commit:**
- `code/server/.env` (API keys) — listed in `.gitignore`
- `code/firmware/CameraWebServer/secrets.h` (Wi-Fi credentials) — listed in `.gitignore`
- Only `secrets.example.h` and `.env.example` are committed

## Key Hardware Notes

- GPIO0 must be pulled LOW during flash; remove the jumper after flashing to run normally
- The camera module is on a fixed pin mapping — do not reassign CAMERA_* pins in firmware
- Default stream port is typically `81`, web UI on port `80`
