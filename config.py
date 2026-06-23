# ============================================================
#  ShivaClips - Config
# ============================================================
import os, json

APP_NAME    = "ShivaClips"
APP_VERSION = "2.0"
LOGO_FILE   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "felfena.png")

# Dil (install.bat lang.json yazar, i18n.py okur)
from i18n import LANG  # "tr" veya "en"

BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")

_DEFAULTS = {
    "clip_before": 15,
    "fps":         20,
    "clip_hotkey": "f8",
    "auto_start":  False,
    "clips_dir":   os.path.join(BASE_DIR, "clips"),
}

def _load():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                return {**_DEFAULTS, **json.load(f)}
        except Exception:
            pass
    return _DEFAULTS.copy()

def save_settings(d: dict):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

_cfg = _load()

CLIP_BEFORE     = int(_cfg["clip_before"])
CLIP_AFTER      = 0
FPS             = int(_cfg["fps"])
CLIP_HOTKEY     = str(_cfg["clip_hotkey"])
AUTO_START      = bool(_cfg["auto_start"])
CLIPS_DIR       = str(_cfg["clips_dir"])
HOTKEY_COOLDOWN = 2.0
RESOLUTION      = (1920, 1080)
FOURCC          = "mp4v"

ASSETS_DIR = os.path.join(BASE_DIR, "assets")
TEMP_DIR   = os.path.join(BASE_DIR, "temp")
LOGS_DIR   = os.path.join(BASE_DIR, "logs")

for _d in [CLIPS_DIR, ASSETS_DIR, TEMP_DIR, LOGS_DIR]:
    os.makedirs(_d, exist_ok=True)

# ── Tema: Ultra Modern Deep Space + Indigo/Violet ────────────────
THEME = {
    # Arka planlar (OLED Dark & Deep Space)
    "bg":      "#09090B",   # Zinc 950 - ana arka plan
    "bg2":     "#09090B",   # Sidebar
    "bg3":     "#18181B",   # Zinc 900 - card bg
    "bg4":     "#27272A",   # Zinc 800 - hover / acik alan

    # Kartlar
    "card":    "#18181B",   # Zinc 900
    "card2":   "#27272A",   # Zinc 800

    # Kenarlıklar (Çok ince ve şeffaf hissi için)
    "border":  "#27272A",   # Zinc 800
    "border2": "#3F3F46",   # Zinc 700

    # Accent — Indigo & Violet
    "accent":  "#4F46E5",   # Indigo 600
    "accent2": "#6366F1",   # Indigo 500 (ana vurgu)
    "accent3": "#818CF8",   # Indigo 400
    "glow":    "#A5B4FC",   # Indigo 300 (parlak)
    "dim_acc": "#312E81",   # Indigo 900 (badge bg)

    # Metin
    "text":    "#FAFAFA",   # Zinc 50 - temiz beyaz
    "dim":     "#A1A1AA",   # Zinc 400 - soluk gri
    "muted":   "#52525B",   # Zinc 600 - çok soluk gri

    # Durum
    "green":   "#10B981",   # Emerald 500
    "green2":  "#34D399",   # Emerald 400
    "red":     "#F43F5E",   # Rose 500
    "red2":    "#FB7185",   # Rose 400
    "orange":  "#F59E0B",   # Amber 500
    "orange2": "#FBB140",

    # Sabit
    "white":   "#FFFFFF",
    "black":   "#000000",
}
T = THEME  # kısa alias
