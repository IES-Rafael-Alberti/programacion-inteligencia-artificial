# 🧪 Actividad opcional: Construcción de tu propio dataset con fuentes abiertas

**Objetivo:** Construir un dataset original utilizando fuentes de datos reales y abiertas (API, portales open data, CSV públicos…), centrado en un ámbito diferente al de las películas.

---

## 🔎 Temáticas sugeridas

Puedes elegir **cualquier fuente de datos** que permita automatizar la recogida de información y que no sea el dominio cinematográfico. Algunas ideas:

| Tema               | Fuente sugerida                                                                | Observaciones                          |
| ------------------ | ------------------------------------------------------------------------------ | -------------------------------------- |
| Clima              | Open-Meteo API, WeatherAPI, MeteoStat                                          | Gratis, sin login (algunas)            |
| Calidad del aire   | OpenAQ, BreezoMeter (limitado)                                                 | Algunos países más cubiertos que otros |
| Energía eléctrica  | REE (Red Eléctrica Española), ESIOS API                                        | REE requiere token gratuito            |
| Transporte público | Datos abiertos municipales (EMT, TMB, etc.)                                    | En formato GTFS o JSON                 |
| Consumo energético | ENTSO-E, portales energéticos autonómicos                                      | Tiempos, demanda, generación           |
| Salud / COVID      | [https://ourworldindata.org/covid-data](https://ourworldindata.org/covid-data) | CSV descargable                        |

---

## 📦 Instrucciones generales

1. **Elegir la fuente de datos** y consultar si se accede vía API, CSV o web scraping
2. **Documentar** qué datos ofrece, de qué país/ciudad, y en qué formato
3. **Obtener los datos** automáticamente con código en Python:

   * Si es API: usar `requests`, `httpx`, etc.
   * Si es archivo abierto: automatizar descarga/lectura
4. **Procesar los datos**: dejar limpio, ordenado y preparado en CSV/Parquet
5. (Opcional) **Servir el dataset** con FastAPI como hicimos en la actividad principal
6. **Documentar** el proceso: qué se ha usado, qué dificultades surgieron, posibles mejoras

---

## 📁 Estructura mínima del proyecto

```
mi_dataset_custom/
├── data/                    # Dataset final
├── src/
│   └── mi_dataset_custom/
│       ├── fetch.py         # Código para obtener los datos
│       ├── clean.py         # Código para limpieza y transformación
│       └── build.py         # Script principal
├── pyproject.toml
└── README.md
```

---

## 🧠 Evaluación

* ✔️ Claridad y originalidad en la elección de datos
* ✔️ Correcta obtención y almacenamiento de los datos
* ✔️ Código ordenado y documentado
* ✔️ Explicación razonada del proceso seguido
* ✔️ Calidad del dataset final generado

---
