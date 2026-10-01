# Ficha del dataset

## Problema
- **Dominio:** educación superior (permanencia estudiantil).
- **Unidad de análisis:** un estudiante de grado matriculado (una fila por estudiante).
- **Decisión apoyada:** al cierre del 1.er semestre, identificar estudiantes en riesgo de abandono para priorizar tutorías, orientación y apoyo financiero.
- **Momento de predicción:** fin del 1.er semestre.
- **Target:** `Target` — situación al final de la duración normal de la carrera: `Dropout` (abandono), `Enrolled` (sigue matriculado), `Graduate` (graduado).
- **Tipo de tarea:** clasificación multiclase (3 clases, desbalanceadas).
- **Métrica principal:** F1-macro. **Clase prioritaria:** `Dropout` (se reporta su recall).
- **Error más costoso:** clasificar como `Graduate` o `Enrolled` a un estudiante que abandonará (no recibe apoyo a tiempo).
- **Usuario de la solución:** oficina de bienestar estudiantil / coordinación académica.

## Procedencia
- **Fuente:** UCI Machine Learning Repository, dataset #697.
- **Ficha:** https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success
- **Descarga directa:** https://archive.ics.uci.edu/static/public/697/predict+students+dropout+and+academic+success.zip
- **Autores:** V. Realinho, M. Vieira Martins, J. Machado, L. Baptista (Instituto Politécnico de Portalegre, Portugal).
- **Donación:** 12-12-2021. **Licencia:** Creative Commons Attribution 4.0 (CC BY 4.0), uso académico permitido con atribución.
- **Cita:** Realinho, V., Machado, J., Baptista, L., & Martins, M. V. (2022). Predicting Student Dropout and Academic Success. *Data*, 7(11), 146.
- **Tamaño:** 4,424 filas × 36 predictores + target. Sin valores ausentes según la ficha.

## Comparación de candidatos
| Criterio | Candidato A (seleccionado): Students' Dropout (UCI #697) | Candidato B: Online Shoppers Purchasing Intention (UCI #468) |
|---|---|---|
| Procedencia | UCI, Instituto Politécnico de Portalegre | UCI, Sakar & Kastro (2018) |
| Licencia | CC BY 4.0 | CC BY 4.0 |
| Filas/columnas | 4,424 × 36 | 12,330 × 17 |
| Target y clases | Dropout / Enrolled / Graduate | Revenue: sí / no (15.5 % / 84.5 %) |
| Ausentes | Ninguno | Ninguno |
| Riesgo de fuga | Alto si no se controla: variables del 2.º semestre posteriores al momento de predicción | Medio-alto: `PageValues` y duraciones son agregados de fin de sesión |

**Justificación:** se selecciona el candidato A porque la decisión (alerta temprana de abandono) es clara, el tamaño es compatible con CPU y exige un análisis explícito de disponibilidad temporal de las variables.

## Aprobación
Ver `docs/aprobacion_dataset.md`.
