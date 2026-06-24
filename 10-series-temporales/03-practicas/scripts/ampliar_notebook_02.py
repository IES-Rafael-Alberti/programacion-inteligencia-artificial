"""Amplía el notebook 02 con los apartados del markdown que faltaban.

El script inserta celdas nuevas antes de "Actividades" y no duplica contenido si
ya encuentra el marcador de ampliación.
"""

from __future__ import annotations

import json
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "02_obtencion_procesamiento_datos.ipynb"
MARKER = "## 8. Entender y documentar el dataset temporal"


def md(source: str, cell_id: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": cell_id,
        "metadata": {},
        "source": textwrap.dedent(source).strip() + "\n",
    }


def code(source: str, cell_id: str) -> dict:
    return {
        "cell_type": "code",
        "id": cell_id,
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": textwrap.dedent(source).strip() + "\n",
    }


def extra_cells() -> list[dict]:
    return [
        md(
            """
            ## 8. Entender y documentar el dataset temporal

            Antes de transformar los datos conviene responder preguntas básicas: qué representa cada fila, cuál es la columna temporal, cuál es la variable objetivo, si hay una única serie o varias, y si existen huecos o duplicados.
            """,
            "nb02-extra-001",
        ),
        code(
            """
            resumen_dataset = pd.DataFrame({
                "pregunta": [
                    "¿Qué representa cada fila?",
                    "Columna temporal",
                    "Variable objetivo",
                    "Frecuencia esperada",
                    "Número de series",
                    "Fechas duplicadas",
                    "Valores perdidos en consumo",
                ],
                "respuesta": [
                    "Una lectura horaria de consumo eléctrico sintético",
                    "timestamp",
                    "consumo_kwh",
                    "1 hora",
                    "1 serie agregada",
                    int(df.index.duplicated().sum()),
                    int(df["consumo_kwh"].isna().sum()),
                ],
            })

            resumen_dataset
            """,
            "nb02-extra-002",
        ),
        md(
            """
            ## 9. Preparar un modelo de datos

            Para forecasting suele ayudar pensar en una estructura estándar: una columna temporal, una variable objetivo, un identificador si hay varias series y variables externas si existen.
            """,
            "nb02-extra-003",
        ),
        code(
            """
            modelo_datos = pd.DataFrame({
                "columna": ["timestamp", "consumo_kwh", "temperatura", "es_festivo", "campaña", "ola_calor"],
                "rol": ["tiempo", "objetivo", "variable externa", "evento conocido", "evento conocido", "evento simulado"],
                "uso": [
                    "ordenar, indexar y filtrar",
                    "analizar y predecir",
                    "explicar efecto de frío/calor",
                    "capturar festivos",
                    "capturar campañas planificadas",
                    "capturar eventos extremos simulados",
                ],
            })

            modelo_datos
            """,
            "nb02-extra-004",
        ),
        md(
            """
            ## 10. Operaciones básicas con fechas en pandas

            Repasamos `pd.to_datetime`, el accesor `.dt`, `DatetimeIndex`, slicing por fechas y creación de secuencias temporales.
            """,
            "nb02-extra-005",
        ),
        code(
            """
            ejemplo_fechas = pd.DataFrame({
                "fecha_texto": ["01/01/2026", "02/01/2026", "03/01/2026"],
                "ventas": [120, 135, 128],
            })

            ejemplo_fechas["fecha"] = pd.to_datetime(ejemplo_fechas["fecha_texto"], dayfirst=True)
            ejemplo_fechas["dia_semana"] = ejemplo_fechas["fecha"].dt.day_name()
            ejemplo_fechas["mes"] = ejemplo_fechas["fecha"].dt.month
            ejemplo_fechas["es_fin_de_semana"] = ejemplo_fechas["fecha"].dt.dayofweek >= 5

            ejemplo_fechas
            """,
            "nb02-extra-006",
        ),
        code(
            """
            ejemplo_indexado = ejemplo_fechas.set_index("fecha")

            seleccion = {
                "dia_concreto": ejemplo_indexado.loc["2026-01-02", "ventas"],
                "rango_fechas": ejemplo_indexado.loc["2026-01-01":"2026-01-03", "ventas"].sum(),
                "fechas_diarias": list(pd.date_range("2026-01-01", periods=3, freq="D")),
                "fechas_horarias": list(pd.date_range("2026-01-01", periods=3, freq="h")),
            }

            seleccion
            """,
            "nb02-extra-007",
        ),
        md(
            """
            ## 11. Tratamiento de valores perdidos en un ejemplo pequeño

            Antes de imputar el dataset realista, conviene ver las estrategias sobre una serie pequeña y controlada.
            """,
            "nb02-extra-008",
        ),
        code(
            """
            fechas = pd.date_range(start="2026-01-01", periods=15, freq="D")
            ventas = [120, 135, np.nan, 140, 150, 160, np.nan, 138, 155, 170, 165, np.nan, 172, 180, 178]

            ejemplo_na = pd.DataFrame({"ventas": ventas}, index=fechas)
            ejemplo_na["ffill"] = ejemplo_na["ventas"].ffill()
            ejemplo_na["media"] = ejemplo_na["ventas"].fillna(ejemplo_na["ventas"].mean())
            ejemplo_na["interpolacion"] = ejemplo_na["ventas"].interpolate()

            ejemplo_na
            """,
            "nb02-extra-009",
        ),
        code(
            """
            fig, ax = plt.subplots(figsize=(12, 4))
            ax.plot(ejemplo_na.index, ejemplo_na["ventas"], marker="o", label="original")
            ax.plot(ejemplo_na.index, ejemplo_na["ffill"], linestyle="--", label="ffill")
            ax.plot(ejemplo_na.index, ejemplo_na["interpolacion"], linestyle="--", label="interpolación")
            ax.set_title("Comparación de imputaciones sencillas")
            ax.legend()
            plt.show()
            """,
            "nb02-extra-010",
        ),
        md(
            """
            ## 12. Formatos compacto, largo y ancho

            El formato largo suele ser el más cómodo para series temporales. El formato ancho puede ser útil para comparar varias series en paralelo.
            """,
            "nb02-extra-011",
        ),
        code(
            """
            formato_largo = df_largo[["timestamp", "id_contador", "consumo"]].copy()
            formato_ancho = formato_largo.pivot_table(
                index="timestamp",
                columns="id_contador",
                values="consumo",
                aggfunc="mean",
            )

            formato_largo.head(), formato_ancho.head()
            """,
            "nb02-extra-012",
        ),
        md(
            """
            ## 13. Forzar intervalos regulares con `asfreq`

            A veces una fecha perdida está oculta: no hay fila para ese instante. `asfreq` crea explícitamente esos huecos.
            """,
            "nb02-extra-013",
        ),
        code(
            """
            ejemplo_irregular = pd.DataFrame({
                "fecha": ["2026-01-01", "2026-01-02", "2026-01-04", "2026-01-05"],
                "ventas": [120, 135, 150, 160],
            })

            ejemplo_irregular["fecha"] = pd.to_datetime(ejemplo_irregular["fecha"])
            ejemplo_irregular = ejemplo_irregular.set_index("fecha")
            ejemplo_regular = ejemplo_irregular.asfreq("D")

            ejemplo_regular
            """,
            "nb02-extra-014",
        ),
        md(
            """
            ## 14. Convertir un dataset de contadores en formato temporal

            Cuando hay varias series, el orden correcto suele ser por identificador y timestamp. Después podemos comprobar duplicados y forzar frecuencia por serie.
            """,
            "nb02-extra-015",
        ),
        code(
            """
            lecturas_contadores = pd.concat([
                formato_largo.assign(id_contador="C001"),
                formato_largo.assign(id_contador="C002", consumo=formato_largo["consumo"] * 0.85),
            ], ignore_index=True)

            lecturas_contadores = lecturas_contadores.sort_values(["id_contador", "timestamp"])
            duplicados_contadores = lecturas_contadores.duplicated(subset=["id_contador", "timestamp"]).sum()

            serie_c001 = (
                lecturas_contadores[lecturas_contadores["id_contador"] == "C001"]
                .set_index("timestamp")
                .asfreq("30min")
            )

            duplicados_contadores, serie_c001.head()
            """,
            "nb02-extra-016",
        ),
        md(
            """
            ## 15. Mapear información adicional con `merge`

            Podemos enriquecer lecturas temporales con metadatos de sensores, contadores, tiendas o clientes.
            """,
            "nb02-extra-017",
        ),
        code(
            """
            metadata = pd.DataFrame({
                "id_contador": ["C001", "C002"],
                "barrio": ["Centro", "Norte"],
                "tipo_vivienda": ["piso", "casa"],
            })

            lecturas_enriquecidas = lecturas_contadores.merge(metadata, on="id_contador", how="left")
            lecturas_enriquecidas.head()
            """,
            "nb02-extra-018",
        ),
        md(
            """
            ## 16. Guardar y cargar datos procesados

            Después de procesar un dataset conviene guardarlo. CSV es universal; Parquet suele ser más eficiente, pero necesita una dependencia adicional (`pyarrow` o `fastparquet`).
            """,
            "nb02-extra-019",
        ),
        code(
            """
            from pathlib import Path

            ruta_csv_demo = Path("datos/lecturas_enriquecidas_demo.csv")
            lecturas_enriquecidas.to_csv(ruta_csv_demo, index=False)

            lecturas_recargadas = pd.read_csv(ruta_csv_demo)
            lecturas_recargadas["timestamp"] = pd.to_datetime(lecturas_recargadas["timestamp"])

            lecturas_recargadas.head()
            """,
            "nb02-extra-020",
        ),
        code(
            """
            ruta_parquet_demo = Path("datos/lecturas_enriquecidas_demo.parquet")

            try:
                lecturas_enriquecidas.to_parquet(ruta_parquet_demo, index=False)
                lecturas_parquet = pd.read_parquet(ruta_parquet_demo)
                resultado_parquet = f"Parquet guardado: {ruta_parquet_demo}"
            except ImportError as exc:
                resultado_parquet = f"Parquet no disponible en este entorno: {exc.__class__.__name__}"

            resultado_parquet
            """,
            "nb02-extra-021",
        ),
        md(
            """
            ## 17. Huecos largos en los datos

            Un hueco aislado y un hueco largo no deberían tratarse igual. En huecos largos, una interpolación lineal puede inventar una evolución demasiado simple.
            """,
            "nb02-extra-022",
        ),
        code(
            """
            np.random.seed(42)
            fechas = pd.date_range(start="2026-01-01", periods=60, freq="D")
            valores = 100 + np.sin(np.arange(60) * 2 * np.pi / 7) * 10 + np.random.normal(0, 3, 60)

            hueco_largo = pd.DataFrame({"ventas": valores}, index=fechas)
            hueco_largo.loc["2026-01-20":"2026-01-30", "ventas"] = np.nan
            hueco_largo["interpolacion"] = hueco_largo["ventas"].interpolate()
            hueco_largo["ffill"] = hueco_largo["ventas"].ffill()

            fig, ax = plt.subplots(figsize=(12, 4))
            ax.plot(hueco_largo.index, hueco_largo["ventas"], marker="o", label="original")
            ax.plot(hueco_largo.index, hueco_largo["interpolacion"], label="interpolación")
            ax.plot(hueco_largo.index, hueco_largo["ffill"], label="ffill", linestyle="--")
            ax.set_title("Hueco largo: comparar estrategias simples")
            ax.legend()
            plt.show()
            """,
            "nb02-extra-023",
        ),
        md(
            """
            ## 18. Perfil medio horario y media por hora-día

            En datos horarios, podemos imputar usando el comportamiento típico de cada hora o de cada combinación de día de semana y hora.
            """,
            "nb02-extra-024",
        ),
        code(
            """
            comparacion_imputacion = imputacion[["consumo_kwh", "ffill", "interpolacion", "perfil_hora_dia"]].copy()
            comparacion_imputacion["perfil_horario"] = comparacion_imputacion["consumo_kwh"]

            perfil_horario = comparacion_imputacion.groupby(comparacion_imputacion.index.hour)["consumo_kwh"].mean()

            for idx in comparacion_imputacion[comparacion_imputacion["perfil_horario"].isna()].index:
                comparacion_imputacion.loc[idx, "perfil_horario"] = perfil_horario.loc[idx.hour]

            comparacion_imputacion.isna().sum()
            """,
            "nb02-extra-025",
        ),
        code(
            """
            zona_hueco = comparacion_imputacion.loc["2026-03-28":"2026-04-03"]

            fig, ax = plt.subplots(figsize=(14, 4))
            ax.plot(zona_hueco.index, zona_hueco["consumo_kwh"], marker="o", label="original")
            ax.plot(zona_hueco.index, zona_hueco["perfil_horario"], label="perfil horario", linestyle="--")
            ax.plot(zona_hueco.index, zona_hueco["perfil_hora_dia"], label="perfil hora-día", linestyle="--")
            ax.set_title("Perfil horario frente a perfil hora-día")
            ax.legend()
            plt.show()
            """,
            "nb02-extra-026",
        ),
        md(
            """
            ## 19. Interpolación estacional

            Si hay un patrón semanal, una opción simple es usar valores equivalentes de ciclos anteriores, por ejemplo el valor de 7 días antes.
            """,
            "nb02-extra-027",
        ),
        code(
            """
            ventas_estacional = hueco_largo.copy()
            ventas_estacional["lag_7"] = ventas_estacional["ventas"].shift(7)
            ventas_estacional["imputacion_estacional"] = ventas_estacional["ventas"].fillna(ventas_estacional["lag_7"])
            ventas_estacional["imputacion_combinada"] = (
                ventas_estacional["ventas"]
                .fillna(ventas_estacional["lag_7"])
                .interpolate()
                .ffill()
            )

            ventas_estacional.loc["2026-01-17":"2026-02-03"]
            """,
            "nb02-extra-028",
        ),
        code(
            """
            muestra_estacional = ventas_estacional.loc["2026-01-17":"2026-02-03"]

            fig, ax = plt.subplots(figsize=(12, 4))
            ax.plot(muestra_estacional.index, muestra_estacional["ventas"], marker="o", label="original")
            ax.plot(muestra_estacional.index, muestra_estacional["imputacion_estacional"], label="lag 7", linestyle="--")
            ax.plot(muestra_estacional.index, muestra_estacional["imputacion_combinada"], label="combinada", linestyle="--")
            ax.set_title("Interpolación estacional con patrón semanal")
            ax.legend()
            plt.show()
            """,
            "nb02-extra-029",
        ),
        md(
            """
            ## 20. Ideas clave

            - Preparar fechas correctamente es imprescindible antes de modelar.
            - `DatetimeIndex` facilita slicing, remuestreo y detección de huecos.
            - `asfreq` hace visibles timestamps perdidos.
            - El formato largo suele ser el más cómodo para análisis temporal.
            - La imputación depende del tipo de hueco y del patrón de la serie.
            - Los metadatos pueden enriquecer el análisis cuando hay varias series.
            """,
            "nb02-extra-030",
        ),
    ]


def main() -> None:
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    if any(MARKER in cell.get("source", "") for cell in nb["cells"]):
        print("El notebook 02 ya contiene la ampliación; no se modifica.")
        return

    insert_at = next(
        (
            i
            for i, cell in enumerate(nb["cells"])
            if cell.get("cell_type") == "markdown" and cell.get("source", "").lstrip().startswith("## Actividades")
        ),
        len(nb["cells"]),
    )
    nb["cells"][insert_at:insert_at] = extra_cells()
    NOTEBOOK.write_text(json.dumps(nb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Notebook ampliado: {NOTEBOOK.name}")


if __name__ == "__main__":
    main()
