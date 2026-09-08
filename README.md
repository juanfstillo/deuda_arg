# Mora Crediticia en Argentina — Diseño Regulatorio y Distribución de Responsabilidad

Proyecto de investigación (Juan Stillo & Julián) sobre economía política de la mora en créditos en Argentina. Pensado para presentación en cátedra y posterior escalado a ponencia de congreso.

## Pregunta de investigación

¿A quién protege el diseño regulatorio del crédito en Argentina: al sistema financiero o al deudor?

Sub-preguntas:

1. ¿Por qué se endeudan los hogares? (perfil de deuda, % sobre ingreso, evolución 2023–hoy)  
2. ¿Por qué no pagan? (mora por tipo de entidad, por segmento de ingreso)  
3. ¿El diseño regulatorio (eliminación del tope de interés, fin de las LEFIs, asimetría bancos/fintech) protege al sistema financiero o al deudor?

## Marco teórico

- Captura regulatoria (Stigler, Peltzman)  
- Blame avoidance / framing de responsabilidad (Weaver)  
- Policy feedback

## Stack técnico

- Python 3.11+  
- JupyterLab (análisis exploratorio, reproducible)  
- pandas (manipulación de series)  
- requests (acceso a API BCRA)  
- matplotlib / seaborn (visualización)  
- Poetry (manejo de dependencias)  
- git (versionado, coautoría)

## Estructura del proyecto

mora-credito-ar/

├── README.md

├── pyproject.toml              \# dependencias (Poetry)

├── data/

│   ├── raw/                    \# series descargadas del BCRA sin tocar

│   └── processed/              \# datasets ya limpios/unificados

├── notebooks/

│   ├── 01\_exploracion\_bcra.ipynb

│   ├── 02\_mora\_bancos\_vs\_fintech.ipynb

│   └── 03\_deuda\_sobre\_ingreso.ipynb

├── src/

│   ├── \_\_init\_\_.py

│   ├── bcra\_api.py             \# funciones para pegarle a la API del BCRA

│   └── clean.py                \# funciones de limpieza reutilizables

├── docs/

│   ├── marco\_teorico.md

│   ├── planteo\_catedra.md

│   └── bibliografia.md

└── outputs/

    ├── figuras/                \# gráficos finales para paper/slides

    └── paper/                  \# borrador del texto (o subcarpeta si usan LaTeX)

## Setup inicial

\# clonar / crear repo

git init mora-credito-ar

cd mora-credito-ar

\# poetry

poetry init

poetry add pandas requests matplotlib seaborn jupyterlab

\# activar entorno

poetry shell

jupyter lab

## Fuentes de datos

- **BCRA — API Central de Deudores (v1.0)**: consulta puntual por CUIT/CUIL/CDI (deuda actual, histórica, cheques rechazados). **No** expone mora agregada por entidad o tipo de cartera — sirve solo para lookups individuales.
- **BCRA — Anexo estadístico del Informe sobre Bancos**: mora agregada por grupo de entidades y tipo de cartera (consumo/comercial). Se publica como Excel descargable manualmente (sin API JSON) en https://www.bcra.gob.ar/catalogo_de_datos/anexo-estadistico-del-informe-sobre-bancos/ — se guarda en `data/raw/` y se parsea con `src/clean.py`.
- **BCRA — API Principales Variables / Estadísticas Monetarias (v4.0)**: tasas activas, spread, reservas, series históricas. Sin autenticación.
- **INDEC / EPH**: ingreso de hogares, para calcular deuda como % del ingreso.  
- **Fintechs**: reportes públicos si existen (comparar contra bancos tradicionales).

## Próximos pasos

- [x] Confirmar endpoints de la API del BCRA y armar `bcra_api.py`
- [ ] Descargar Anexo estadístico del Informe sobre Bancos (mora por entidad/cartera) 2023–hoy
- [ ] Descargar series de tasas 2023–hoy vía `bcra_api.py`
- [ ] Cruzar con datos de ingreso (EPH) para % deuda/ingreso  
- [ ] Primer notebook exploratorio: mora bancos vs. fintech  
- [ ] Cerrar bibliografía del marco teórico

