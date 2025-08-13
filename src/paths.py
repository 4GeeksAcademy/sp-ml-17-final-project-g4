from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1] # Project root (1 level up from src/)
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

for d in (RAW_DIR, INTERIM_DIR, PROCESSED_DIR): # Ensure folders exist
    d.mkdir(parents=True, exist_ok=True)