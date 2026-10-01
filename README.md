# INF-8239 · Unidad 01 — Modelos avanzados, reducción dimensional y Green AI

**Estudiante:** Melvin Humberto Rivas Genao

## Problema
Alerta temprana de abandono universitario al **cierre del 1.er semestre**.
- **Dataset:** Predict Students' Dropout and Academic Success — UCI #697, CC BY 4.0 (ver `docs/ficha_dataset.md`, aprobación en `docs/aprobacion_dataset.md`).
- **Target:** `Target` (Dropout / Enrolled / Graduate).
- **Exclusiones por fuga:** las 6 variables `Curricular units 2nd sem (...)`.
- **Métrica principal:** F1-macro; clase prioritaria `Dropout` (recall).
- **Partición:** 80/20 estratificada, `random_state=42` (`src/inf8239_u01/features.py`).

## Entorno
- Google Colab (Linux, CPU), autorizado por el docente en lugar de VS Code + `.venv`.
- Hardware: `reports/entorno.txt`. Versiones exactas: `requirements-lock.txt`.

## Estructura
```
data/raw/         dataset descargado (no se versiona)
docs/             ficha, aprobación y diccionario de datos
notebooks/        00 entorno · 01 SVM guiada · 02 dataset y SVM (E01) · 03 ensambles y Green AI (E02)
reports/          tablas CSV, figuras, modelos serializados y registro del entorno
src/inf8239_u01/  data.py · features.py · models.py · green.py
tests/            pruebas con pytest
```

## Reproducción
1. Abrir el notebook en Google Colab y definir el secreto `GITHUB_TOKEN`.
2. Ejecutar todas las celdas en orden. La descarga es automática:
```python
from inf8239_u01.data import download_dataset
download_dataset()   # UCI -> data/raw/dataset.csv
```
3. Pruebas:
```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m pytest -q
```
