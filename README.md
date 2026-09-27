# INF-8239 · Unidad 01 — Modelos avanzados, reducción dimensional y Green AI

**Estudiante:** Melvin Humberto Rivas Genao

## Entorno
- **Plataforma:** Google Colab (runtime Linux, CPU), aprobado por el docente en lugar de VS Code + `.venv` local.
- **Sistema operativo y hardware:** ver `reports/entorno.txt` (se genera automáticamente).
- **Versiones exactas de paquetes:** `requirements-lock.txt`.

## Estructura
```
data/raw/      datos descargados (no se versionan)
docs/          ficha del dataset y diccionario
notebooks/     notebooks de laboratorio
reports/       tablas, figuras y registro del entorno
src/inf8239_u01/  código reutilizable
tests/         pruebas con pytest
```

## Cómo reproducir
1. Abrir `notebooks/00_verificacion.ipynb` en Google Colab.
2. Guardar un token de GitHub en *Secrets* con el nombre `GITHUB_TOKEN`.
3. Ejecutar todas las celdas en orden.

Comandos usados:
```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m pytest -q
git add . && git commit -m "..." && git push
```
