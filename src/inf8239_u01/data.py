"""Descarga reproducible y carga del dataset UCI #697."""
import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

UCI_URL = ("https://archive.ics.uci.edu/static/public/697/"
           "predict+students+dropout+and+academic+success.zip")
MIRROR_URL = ("https://raw.githubusercontent.com/omar-kabeer/"
              "forecasting-academic-trajectories/main/src/data/data.csv")
DEFAULT_PATH = "data/raw/dataset.csv"
TARGET = "Target"


def _read_bytes(url: str) -> bytes:
    if not url.startswith(("https://", "http://")):
        raise ValueError("La fuente debe ser una URL HTTP(S)")
    with urllib.request.urlopen(url, timeout=60) as resp:
        return resp.read()


def _parse(raw: bytes) -> pd.DataFrame:
    if raw[:2] == b"PK":  # archivo ZIP
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            name = next(n for n in zf.namelist() if n.lower().endswith(".csv"))
            raw = zf.read(name)
    return pd.read_csv(io.BytesIO(raw), sep=";", encoding="utf-8-sig")


def clean_columns(frame: pd.DataFrame) -> pd.DataFrame:
    """Elimina espacios y tabulaciones de los nombres de columna."""
    frame = frame.copy()
    frame.columns = [c.strip() for c in frame.columns]
    return frame


def download_dataset(url: str = UCI_URL, destination: str = DEFAULT_PATH,
                     fallback: str | None = MIRROR_URL) -> Path:
    """Descarga el dataset (ZIP o CSV) y lo guarda como CSV con separador coma."""
    try:
        frame = _parse(_read_bytes(url))
    except Exception as exc:
        if not fallback:
            raise
        print(f"Fuente principal no disponible ({exc}); usando espejo.")
        frame = _parse(_read_bytes(fallback))
    frame = clean_columns(frame)
    if frame.empty:
        raise ValueError("El dataset descargado está vacío")
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)
    return path


def load_data(path: str = DEFAULT_PATH) -> pd.DataFrame:
    return clean_columns(pd.read_csv(path))
