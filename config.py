import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or ""
FLASH_MODEL = os.getenv("GEMINI_FLASH_MODEL", "gemini-1.5-flash")
PRO_MODEL = os.getenv("GEMINI_PRO_MODEL", "gemini-1.5-pro")
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
# ... rest of your settings