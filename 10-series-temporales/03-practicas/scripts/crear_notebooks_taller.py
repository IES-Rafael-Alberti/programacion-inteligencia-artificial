"""Crea los notebooks del taller de series temporales.

Los notebooks se generan sin salidas para que el alumnado pueda ejecutarlos
paso a paso durante la sesión.
"""

from __future__ import annotations

import json
import re
import runpy
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
_CELL_COUNTER = 0


def cell_id(prefix: str) -> str:
    global _CELL_COUNTER
    _CELL_COUNTER += 1
    safe_prefix = re.sub(r"[^a-z0-9-]", "-", prefix.lower()).strip("-")[:20]
    return f"{safe_prefix}-{_CELL_COUNTER:04d}"


def md(source: str) -> dict:
    return {"cell_type": "markdown", "id": cell_id("markdown"), "metadata": {}, "source": textwrap.dedent(source).strip() + "\n"}


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "id": cell_id("code"),
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": textwrap.dedent(source).strip() + "\n",
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.x",
                "mimetype": "text/x-python",
                "codemirror_mode": {"name": "ipython", "version": 3},
                "pygments_lexer": "ipython3",
                "nbconvert_exporter": "python",
                "file_extension": ".py",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_notebook(filename: str, cells: list[dict]) -> None:
    path = ROOT / filename
    path.write_text(json.dumps(notebook(cells), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


COMMON_STYLE = """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["figure.figsize"] = (12, 4)
plt.rcParams["axes.titlesize"] = 14
"""


def build_01() -> list[dict]:
    return [
        md("""
        # Sesión 1: Introducción a las series temporales

        En este notebook vamos a construir series temporales sintéticas para entender tendencia, estacionalidad, ruido, memoria temporal y una primera predicción baseline.
        """),
        code(COMMON_STYLE),
        md("""
        ## 1. Una serie temporal sintética

        Primero construimos una serie diaria de ventas. Al ser sintética, conocemos sus componentes y podemos ver cómo se combinan.
        """),
        code("""
        np.random.seed(42)

        fechas = pd.date_range(start="2026-01-01", periods=180, freq="D")
        n = len(fechas)
        dias = np.arange(n)

        tendencia = np.linspace(50, 100, n)
        estacionalidad = 10 * np.sin(2 * np.pi * dias / 7)
        ruido = np.random.normal(loc=0, scale=5, size=n)
        ventas = tendencia + estacionalidad + ruido

        df = pd.DataFrame({
            "ventas": ventas,
            "tendencia": tendencia,
            "estacionalidad": estacionalidad,
            "ruido": ruido,
        }, index=fechas)

        df.head()
        """),
        code("""
        fig, ax = plt.subplots()
        ax.plot(df.index, df["ventas"], label="ventas", color="tab:blue")
        ax.set_title("Serie temporal sintética de ventas")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Ventas")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 2. Ver los componentes por separado

        Separar los componentes ayuda a interpretar qué está pasando en la serie observada.
        """),
        code("""
        fig, axes = plt.subplots(4, 1, figsize=(12, 8), sharex=True)
        columnas = ["ventas", "tendencia", "estacionalidad", "ruido"]

        for ax, columna in zip(axes, columnas):
            ax.plot(df.index, df[columna])
            ax.set_title(columna)

        plt.tight_layout()
        plt.show()
        """),
        md("""
        ## 3. Ruido blanco y ruido rojo

        El ruido blanco no tiene memoria. El ruido rojo sí depende parcialmente del valor anterior, por eso se ve más suave.
        """),
        code("""
        np.random.seed(42)
        ruido_blanco = np.random.normal(0, 1, 200)

        ruido_rojo = [0]
        for i in range(1, 200):
            ruido_rojo.append(0.8 * ruido_rojo[i - 1] + np.random.normal(0, 1))

        fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
        axes[0].plot(ruido_blanco, color="tab:gray")
        axes[0].set_title("Ruido blanco")
        axes[1].plot(ruido_rojo, color="tab:red")
        axes[1].set_title("Ruido rojo")
        plt.tight_layout()
        plt.show()
        """),
        md("""
        ## 4. Serie autorregresiva

        En una señal autorregresiva, el valor actual depende de valores anteriores. Esto introduce memoria temporal.
        """),
        code("""
        np.random.seed(42)
        serie_ar = [10]

        for i in range(1, 200):
            serie_ar.append(0.7 * serie_ar[i - 1] + np.random.normal(0, 2))

        fig, ax = plt.subplots()
        ax.plot(serie_ar)
        ax.set_title("Serie autorregresiva")
        ax.set_xlabel("Paso temporal")
        plt.show()
        """),
        md("""
        ## 5. Serie con tendencia, estacionalidad semanal y anual

        En datos reales los componentes aparecen mezclados. Aquí combinamos varias fuentes de variación.
        """),
        code("""
        np.random.seed(42)
        fechas = pd.date_range(start="2026-01-01", periods=365, freq="D")
        n = len(fechas)
        dias = np.arange(n)

        tendencia = np.linspace(100, 180, n)
        estacionalidad_semanal = 15 * np.sin(2 * np.pi * dias / 7)
        estacionalidad_anual = 25 * np.sin(2 * np.pi * dias / 365)
        ruido = np.random.normal(0, 8, n)
        serie = tendencia + estacionalidad_semanal + estacionalidad_anual + ruido

        df_larga = pd.DataFrame({"ventas": serie}, index=fechas)

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(df_larga.index, df_larga["ventas"])
        ax.set_title("Serie sintética con tendencia, estacionalidad y ruido")
        ax.set_ylabel("Ventas")
        plt.show()
        """),
        md("""
        ## 6. Estacionaria frente a no estacionaria

        Una serie no estacionaria puede cambiar su media o su varianza con el tiempo.
        """),
        code("""
        np.random.seed(42)
        cambio_media = np.concatenate([
            np.random.normal(50, 5, 100),
            np.random.normal(80, 5, 100),
        ])
        cambio_varianza = np.concatenate([
            np.random.normal(50, 2, 100),
            np.random.normal(50, 12, 100),
        ])

        fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
        axes[0].plot(cambio_media)
        axes[0].set_title("Cambio en la media")
        axes[1].plot(cambio_varianza)
        axes[1].set_title("Cambio en la varianza")
        plt.tight_layout()
        plt.show()
        """),
        md("""
        ## 7. Primera predicción baseline

        Un baseline sencillo sirve como referencia mínima: predecimos todo el test con el último valor conocido.
        """),
        code("""
        from sklearn.metrics import mean_absolute_error

        train = df.iloc[:-30]
        test = df.iloc[-30:]
        pred_naive = pd.Series(train["ventas"].iloc[-1], index=test.index)
        mae = mean_absolute_error(test["ventas"], pred_naive)

        fig, ax = plt.subplots()
        ax.plot(train.index, train["ventas"], label="train")
        ax.plot(test.index, test["ventas"], label="test")
        ax.plot(pred_naive.index, pred_naive, label="predicción naive", linestyle="--")
        ax.set_title(f"Predicción naive - MAE: {mae:.2f}")
        ax.legend()
        plt.show()
        """),
        md("""
        ## Actividades

        1. Cambia la amplitud de la estacionalidad semanal y observa la gráfica.
        2. Aumenta el ruido y comprueba cuándo la estructura deja de verse clara.
        3. Sustituye la predicción naive por la media de los últimos 7 días.
        """),
    ]


def build_02() -> list[dict]:
    return [
        md("""
        # Sesión 2: Obtención y procesamiento de datos temporales

        En este notebook trabajamos con fechas, índices temporales, huecos, imputación, remuestreo y formatos de datos.
        """),
        code(COMMON_STYLE),
        md("""
        ## 1. Cargar consumo realista

        Usaremos `datos/consumo_realista.csv`, que incluye huecos, outliers simulados, meteorología y eventos.
        """),
        code("""
        df = pd.read_csv("datos/consumo_realista.csv")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp").set_index("timestamp")

        df.head()
        """),
        code("""
        df.info()
        """),
        md("""
        ## 2. Comprobar frecuencia, duplicados y huecos

        `asfreq("h")` fuerza una frecuencia horaria. Si faltan timestamps, aparecerán explícitamente como filas vacías.
        """),
        code("""
        duplicados = df.index.duplicated().sum()
        df_regular = df.asfreq("h")
        valores_perdidos = df_regular["consumo_kwh"].isna().sum()

        duplicados, valores_perdidos, df_regular.index.freq
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(df_regular.index, df_regular["consumo_kwh"], label="consumo")
        ax.scatter(
            df_regular.index[df_regular["consumo_kwh"].isna()],
            np.repeat(df_regular["consumo_kwh"].min(), df_regular["consumo_kwh"].isna().sum()),
            color="tab:red",
            s=20,
            label="huecos",
        )
        ax.set_title("Consumo horario con huecos visibles")
        ax.set_ylabel("kWh")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 3. Variables temporales con el índice

        El índice temporal permite crear variables de calendario de forma directa.
        """),
        code("""
        df_regular["hora"] = df_regular.index.hour
        df_regular["dia_semana"] = df_regular.index.dayofweek
        df_regular["mes"] = df_regular.index.month
        df_regular["es_fin_de_semana"] = df_regular.index.dayofweek >= 5

        df_regular[["consumo_kwh", "hora", "dia_semana", "mes", "es_fin_de_semana"]].head()
        """),
        md("""
        ## 4. Selección por fechas

        Con `DatetimeIndex` podemos seleccionar días, semanas o meses completos con cadenas de texto.
        """),
        code("""
        semana = df_regular.loc["2026-02-01":"2026-02-07"]

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(semana.index, semana["consumo_kwh"], marker="o")
        ax.set_title("Consumo durante una semana")
        ax.set_ylabel("kWh")
        plt.show()
        """),
        md("""
        ## 5. Imputación simple de valores perdidos

        Comparamos tres estrategias: valor anterior, interpolación temporal y perfil medio por hora y día de semana.
        """),
        code("""
        imputacion = df_regular[["consumo_kwh"]].copy()
        imputacion["ffill"] = imputacion["consumo_kwh"].ffill()
        imputacion["interpolacion"] = imputacion["consumo_kwh"].interpolate(method="time")

        perfil_hora_dia = imputacion.groupby([imputacion.index.dayofweek, imputacion.index.hour])["consumo_kwh"].mean()
        imputacion["perfil_hora_dia"] = imputacion["consumo_kwh"]

        for idx in imputacion[imputacion["perfil_hora_dia"].isna()].index:
            clave = (idx.dayofweek, idx.hour)
            imputacion.loc[idx, "perfil_hora_dia"] = perfil_hora_dia.loc[clave]

        imputacion.isna().sum()
        """),
        code("""
        zona_hueco = imputacion.loc["2026-03-28":"2026-04-03"]

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(zona_hueco.index, zona_hueco["consumo_kwh"], marker="o", label="original")
        ax.plot(zona_hueco.index, zona_hueco["ffill"], label="ffill", linestyle="--")
        ax.plot(zona_hueco.index, zona_hueco["interpolacion"], label="interpolación", linestyle="--")
        ax.plot(zona_hueco.index, zona_hueco["perfil_hora_dia"], label="perfil hora-día", linestyle="--")
        ax.set_title("Comparación de estrategias de imputación")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 6. Remuestreo horario a diario

        `resample` permite cambiar la granularidad de la serie. Para consumo eléctrico suele tener sentido sumar el consumo diario.
        """),
        code("""
        consumo_limpio = imputacion["perfil_hora_dia"]
        consumo_diario = consumo_limpio.resample("D").sum()

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(consumo_diario.index, consumo_diario)
        ax.set_title("Consumo diario agregado")
        ax.set_ylabel("kWh/día")
        plt.show()
        """),
        md("""
        ## 7. Formato ancho y formato largo

        A veces los datos llegan con columnas que representan bloques horarios. `melt` los transforma a formato largo.
        """),
        code("""
        df_bloques = pd.DataFrame({
            "fecha": ["2026-01-01", "2026-01-02"],
            "id_contador": ["C001", "C001"],
            "h00_00": [0.31, 0.28],
            "h00_30": [0.29, 0.27],
            "h01_00": [0.34, 0.32],
            "h01_30": [0.40, 0.38],
        })

        df_largo = df_bloques.melt(
            id_vars=["fecha", "id_contador"],
            var_name="bloque",
            value_name="consumo",
        )

        mapa_bloques = {"h00_00": "00:00", "h00_30": "00:30", "h01_00": "01:00", "h01_30": "01:30"}
        df_largo["timestamp"] = pd.to_datetime(df_largo["fecha"] + " " + df_largo["bloque"].map(mapa_bloques))
        df_largo = df_largo.sort_values("timestamp")

        df_largo[["timestamp", "id_contador", "consumo"]]
        """),
        md("""
        ## Actividades

        1. Localiza cuántos huecos simulados hay en `consumo_realista.csv`.
        2. Compara `ffill`, interpolación y perfil horario sobre otro intervalo.
        3. Agrega el consumo por semana y representa la evolución.
        """),
    ]


def build_03() -> list[dict]:
    return [
        md("""
        # Sesión 3: Análisis y visualización de series temporales

        En este notebook exploramos una serie antes de modelarla: gráficos, estacionalidad, autocorrelación, descomposición y outliers.
        """),
        code(COMMON_STYLE + "\nfrom statsmodels.graphics.tsaplots import plot_acf\nfrom statsmodels.tsa.seasonal import seasonal_decompose, STL\nfrom sklearn.ensemble import IsolationForest"),
        md("""
        ## 1. Cargar la serie básica

        Usamos `consumo_basico.csv` para visualizar patrones sin huecos ni outliers artificiales.
        """),
        code("""
        df = pd.read_csv("datos/consumo_basico.csv")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.set_index("timestamp").asfreq("h")

        df.head()
        """),
        md("""
        ## 2. Gráfico de líneas

        El primer paso suele ser mirar la serie completa y después acercarse a periodos concretos.
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(df.index, df["consumo_kwh"], linewidth=0.8)
        ax.set_title("Consumo eléctrico horario")
        ax.set_ylabel("kWh")
        plt.show()
        """),
        code("""
        semana = df.loc["2026-02-02":"2026-02-08"]

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(semana.index, semana["consumo_kwh"], marker="o")
        ax.set_title("Detalle de una semana")
        ax.set_ylabel("kWh")
        plt.show()
        """),
        md("""
        ## 3. Patrones estacionales

        Los promedios por hora y por día de semana muestran estacionalidades habituales en consumo eléctrico.
        """),
        code("""
        fig, axes = plt.subplots(1, 2, figsize=(14, 4))

        df.groupby(df.index.hour)["consumo_kwh"].mean().plot(ax=axes[0], marker="o")
        axes[0].set_title("Perfil medio por hora")
        axes[0].set_xlabel("Hora")
        axes[0].set_ylabel("kWh")

        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        perfil_dia = df.groupby(df.index.dayofweek)["consumo_kwh"].mean()
        sns.barplot(x=dias, y=perfil_dia.values, ax=axes[1], color="tab:blue")
        axes[1].set_title("Media por día de semana")
        axes[1].tick_params(axis="x", rotation=45)

        plt.tight_layout()
        plt.show()
        """),
        md("""
        ## 4. Boxplots estacionales

        Los boxplots permiten comparar distribuciones, no solo medias.
        """),
        code("""
        df_plot = df.copy()
        df_plot["hora"] = df_plot.index.hour
        df_plot["dia_semana"] = df_plot.index.dayofweek
        df_plot["nombre_dia"] = pd.Categorical(
            [dias[i] for i in df_plot["dia_semana"]],
            categories=dias,
            ordered=True,
        )

        fig, axes = plt.subplots(1, 2, figsize=(14, 4))
        sns.boxplot(data=df_plot, x="hora", y="consumo_kwh", ax=axes[0], color="lightblue")
        axes[0].set_title("Distribución por hora")
        sns.boxplot(data=df_plot, x="nombre_dia", y="consumo_kwh", ax=axes[1], color="lightgreen")
        axes[1].set_title("Distribución por día")
        axes[1].tick_params(axis="x", rotation=45)
        plt.tight_layout()
        plt.show()
        """),
        md("""
        ## 5. Mapa de calor hora-día

        Una matriz de día de semana frente a hora revela patrones combinados.
        """),
        code("""
        tabla = df_plot.pivot_table(
            values="consumo_kwh",
            index="nombre_dia",
            columns="hora",
            aggfunc="mean",
            observed=False,
        )

        fig, ax = plt.subplots(figsize=(14, 5))
        sns.heatmap(tabla, cmap="YlOrRd", ax=ax)
        ax.set_title("Consumo medio por día de semana y hora")
        ax.set_xlabel("Hora")
        ax.set_ylabel("Día")
        plt.show()
        """),
        md("""
        ## 6. Autocorrelación

        Si hay estacionalidad diaria y semanal, deberían aparecer relaciones en los lags 24 y 168.
        """),
        code("""
        fig, ax = plt.subplots(figsize=(12, 4))
        plot_acf(df["consumo_kwh"], lags=24 * 8, ax=ax)
        ax.set_title("Autocorrelación del consumo horario")
        plt.show()
        """),
        md("""
        ## 7. Medias móviles

        Las medias móviles suavizan la serie y ayudan a ver la tendencia.
        """),
        code("""
        df["media_24h"] = df["consumo_kwh"].rolling(24).mean()
        df["media_7d"] = df["consumo_kwh"].rolling(24 * 7).mean()

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(df.index, df["consumo_kwh"], alpha=0.25, label="consumo")
        ax.plot(df.index, df["media_24h"], label="media 24h")
        ax.plot(df.index, df["media_7d"], label="media 7d", linewidth=2)
        ax.set_title("Suavizado con medias móviles")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 8. Descomposición clásica y STL

        Descomponemos la serie en tendencia, estacionalidad y residuo usando periodo diario.
        """),
        code("""
        muestra = df["consumo_kwh"].iloc[:24 * 45]
        descomposicion = seasonal_decompose(muestra, model="additive", period=24)
        descomposicion.plot()
        plt.suptitle("Descomposición clásica", y=1.02)
        plt.show()
        """),
        code("""
        stl = STL(muestra, period=24)
        resultado_stl = stl.fit()
        resultado_stl.plot()
        plt.suptitle("Descomposición STL", y=1.02)
        plt.show()
        """),
        md("""
        ## 9. Outliers: detección y tratamiento

        Trabajamos con `consumo_realista.csv`, que contiene outliers simulados.
        """),
        code("""
        df_out = pd.read_csv("datos/consumo_realista.csv")
        df_out["timestamp"] = pd.to_datetime(df_out["timestamp"])
        df_out = df_out.set_index("timestamp").asfreq("h")

        media = df_out["consumo_kwh"].mean()
        desviacion = df_out["consumo_kwh"].std()
        limite_inferior = media - 3 * desviacion
        limite_superior = media + 3 * desviacion
        df_out["outlier_std"] = (df_out["consumo_kwh"] < limite_inferior) | (df_out["consumo_kwh"] > limite_superior)

        q1 = df_out["consumo_kwh"].quantile(0.25)
        q3 = df_out["consumo_kwh"].quantile(0.75)
        iqr = q3 - q1
        df_out["outlier_iqr"] = (df_out["consumo_kwh"] < q1 - 1.5 * iqr) | (df_out["consumo_kwh"] > q3 + 1.5 * iqr)

        df_out[["es_outlier_simulado", "outlier_std", "outlier_iqr"]].sum()
        """),
        code("""
        variables = df_out[["consumo_kwh", "hora", "dia_semana", "mes"]].dropna()
        modelo = IsolationForest(contamination=0.01, random_state=42)
        df_out["outlier_iforest"] = False
        df_out.loc[variables.index, "outlier_iforest"] = modelo.fit_predict(variables) == -1

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(df_out.index, df_out["consumo_kwh"], label="consumo", alpha=0.7)
        ax.scatter(
            df_out.index[df_out["outlier_iforest"]],
            df_out.loc[df_out["outlier_iforest"], "consumo_kwh"],
            color="tab:red",
            label="outlier Isolation Forest",
            zorder=3,
        )
        ax.set_title("Detección de outliers")
        ax.legend()
        plt.show()
        """),
        code("""
        df_out["consumo_limpio"] = df_out["consumo_kwh"]
        df_out.loc[df_out["outlier_iforest"], "consumo_limpio"] = np.nan
        df_out["consumo_limpio"] = df_out["consumo_limpio"].interpolate(method="time").ffill().bfill()

        zona = df_out.loc[df_out["outlier_iforest"]].index[:1]
        if len(zona) > 0:
            inicio = zona[0] - pd.Timedelta(days=2)
            fin = zona[0] + pd.Timedelta(days=2)
            muestra_out = df_out.loc[inicio:fin]
        else:
            muestra_out = df_out.iloc[:24 * 7]

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(muestra_out.index, muestra_out["consumo_kwh"], label="original", alpha=0.6)
        ax.plot(muestra_out.index, muestra_out["consumo_limpio"], label="limpia", linewidth=2)
        ax.set_title("Tratamiento simple de outliers")
        ax.legend()
        plt.show()
        """),
        md("""
        ## Actividades

        1. Cambia el periodo de STL a 168 y compara el resultado.
        2. Detecta outliers sobre residuos en lugar de sobre la serie original.
        3. Justifica si eliminarías, imputarías o conservarías cada outlier detectado.
        """),
    ]


def build_04() -> list[dict]:
    return [
        md("""
        # Sesión 4: Baselines y evaluación de forecasting

        En este notebook construimos referencias sólidas antes de pasar a modelos complejos: separación temporal, métricas y comparación de baselines.
        """),
        code(COMMON_STYLE + "\nfrom sklearn.metrics import mean_absolute_error, mean_squared_error\nfrom statsmodels.tsa.holtwinters import SimpleExpSmoothing, ExponentialSmoothing\nfrom statsmodels.tsa.arima.model import ARIMA"),
        md("""
        ## 1. Cargar datos y preparar la serie

        Usamos el consumo con meteorología y eventos para tener una serie realista, pero sin huecos artificiales.
        """),
        code("""
        df = pd.read_csv("datos/consumo_con_eventos.csv")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.set_index("timestamp").asfreq("h")

        serie = df["consumo_kwh"]
        serie.head()
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(serie.index, serie)
        ax.set_title("Consumo eléctrico horario")
        ax.set_ylabel("kWh")
        plt.show()
        """),
        md("""
        ## 2. Separación temporal

        La división debe respetar el tiempo: primero entrenamiento, después validación y finalmente test.
        """),
        code("""
        train = serie.iloc[:24 * 120]
        validacion = serie.iloc[24 * 120:24 * 150]
        test = serie.iloc[24 * 150:]

        len(train), len(validacion), len(test)
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(train.index, train, label="train")
        ax.plot(validacion.index, validacion, label="validación")
        ax.plot(test.index, test, label="test")
        ax.set_title("Separación temporal de los datos")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 3. Métricas

        Calcularemos MAE, RMSE y MAPE. MAPE se usa con cuidado porque falla con valores cercanos a cero.
        """),
        code("""
        def rmse(y_true, y_pred):
            return np.sqrt(mean_squared_error(y_true, y_pred))


        def mape(y_true, y_pred):
            y_true = np.asarray(y_true)
            y_pred = np.asarray(y_pred)
            mascara = y_true != 0
            return np.mean(np.abs((y_true[mascara] - y_pred[mascara]) / y_true[mascara])) * 100


        def evaluar(y_true, y_pred):
            return {
                "MAE": mean_absolute_error(y_true, y_pred),
                "RMSE": rmse(y_true, y_pred),
                "MAPE": mape(y_true, y_pred),
            }
        """),
        md("""
        ## 4. Baselines sencillos

        Empezamos con naive, medias recientes y seasonal naive.
        """),
        code("""
        predicciones = {}

        predicciones["naive"] = pd.Series(train.iloc[-1], index=validacion.index)
        predicciones["media_24h"] = pd.Series(train.tail(24).mean(), index=validacion.index)
        predicciones["media_7d"] = pd.Series(train.tail(24 * 7).mean(), index=validacion.index)

        historia_validacion = pd.concat([train, validacion])
        predicciones["seasonal_24h"] = historia_validacion.shift(24).loc[validacion.index]
        predicciones["seasonal_7d"] = historia_validacion.shift(24 * 7).loc[validacion.index]

        pd.DataFrame({nombre: evaluar(validacion, pred) for nombre, pred in predicciones.items()}).T.sort_values("MAE")
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(validacion.iloc[:24 * 7], label="real", linewidth=2)
        ax.plot(predicciones["naive"].iloc[:24 * 7], label="naive", linestyle="--")
        ax.plot(predicciones["seasonal_24h"].iloc[:24 * 7], label="seasonal 24h", linestyle="--")
        ax.plot(predicciones["seasonal_7d"].iloc[:24 * 7], label="seasonal 7d", linestyle="--")
        ax.set_title("Comparación visual de baselines")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 5. Suavizado exponencial

        Añadimos modelos clásicos que siguen siendo referencias fuertes en muchas series.
        """),
        code("""
        modelo_ses = SimpleExpSmoothing(train, initialization_method="estimated").fit()
        pred_ses = modelo_ses.forecast(len(validacion))
        pred_ses.index = validacion.index
        predicciones["suavizado_simple"] = pred_ses

        modelo_hw = ExponentialSmoothing(
            train,
            trend="add",
            seasonal="add",
            seasonal_periods=24,
            initialization_method="estimated",
        ).fit()
        pred_hw = modelo_hw.forecast(len(validacion))
        pred_hw.index = validacion.index
        predicciones["holt_winters"] = pred_hw
        """),
        md("""
        ## 6. ARIMA sencillo

        ARIMA se incluye como referencia conceptual. Para que el notebook sea ágil, se ajusta sobre una ventana reciente del entrenamiento.
        """),
        code("""
        train_arima = train.tail(24 * 45)
        modelo_arima = ARIMA(train_arima, order=(2, 1, 2)).fit()
        pred_arima = modelo_arima.forecast(steps=len(validacion))
        pred_arima.index = validacion.index
        predicciones["arima"] = pred_arima
        """),
        md("""
        ## 7. Tabla final de validación

        Todos los modelos se comparan sobre el mismo periodo de validación.
        """),
        code("""
        resultados = []

        for nombre, pred in predicciones.items():
            metricas = evaluar(validacion, pred)
            metricas["modelo"] = nombre
            resultados.append(metricas)

        tabla_resultados = pd.DataFrame(resultados).set_index("modelo").sort_values("MAE")
        tabla_resultados
        """),
        code("""
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.barplot(data=tabla_resultados.reset_index(), x="MAE", y="modelo", ax=ax, color="tab:blue")
        ax.set_title("Comparación de baselines por MAE")
        plt.show()
        """),
        code("""
        mejor_modelo = tabla_resultados.index[0]
        mejor_pred = predicciones[mejor_modelo]

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(validacion.iloc[:24 * 10], label="real")
        ax.plot(mejor_pred.iloc[:24 * 10], label=mejor_modelo, linestyle="--")
        ax.set_title("Mejor baseline en validación")
        ax.legend()
        plt.show()

        mejor_modelo
        """),
        md("""
        ## 8. Evaluación final en test

        El test se usa al final, una vez elegido el modelo con validación. Aquí repetimos el seasonal naive semanal como referencia fuerte.
        """),
        code("""
        historia_final = pd.concat([train, validacion, test])
        pred_test = historia_final.shift(24 * 7).loc[test.index]
        evaluar(test, pred_test)
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(test.iloc[:24 * 10], label="real")
        ax.plot(pred_test.iloc[:24 * 10], label="seasonal naive 7d", linestyle="--")
        ax.set_title("Evaluación final en test")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 9. Residuos y predictibilidad

        Si los residuos tienen estructura, quizá un modelo más avanzado pueda mejorar. Si son ruido, será más difícil.
        """),
        code("""
        residuos = validacion - predicciones["seasonal_7d"]
        coef_variacion = serie.std() / serie.mean()

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(residuos)
        ax.axhline(0, color="black", linewidth=1)
        ax.set_title(f"Residuos del seasonal naive semanal | CV: {coef_variacion:.3f}")
        plt.show()
        """),
        md("""
        ## Actividades

        1. Cambia las ventanas de media móvil y compara la tabla de resultados.
        2. Evalúa `seasonal_24h` y `seasonal_7d` en test.
        3. Representa los residuos del mejor baseline y describe si queda algún patrón visible.
        """),
    ]


def build_05() -> list[dict]:
    return [
        md("""
        # Sesión 5: Forecasting como problema de regresión

        En este notebook empezamos la segunda parte del taller: machine learning para series temporales.

        La idea principal es transformar una serie temporal en una tabla supervisada:

        ```text
        X = variables construidas con el pasado
        y = valor futuro que queremos predecir
        ```
        """),
        code(COMMON_STYLE + "\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor\nfrom sklearn.metrics import mean_absolute_error, mean_squared_error"),
        md("""
        ## 1. Cargar la serie de consumo

        Usamos `datos/consumo_con_eventos.csv`, que contiene consumo horario y eventos simulados. Para esta primera sesión de ML trabajaremos con predicción a un paso: predecir la siguiente hora usando información pasada.
        """),
        code("""
        df = pd.read_csv("datos/consumo_con_eventos.csv")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp").set_index("timestamp").asfreq("h")

        df.head()
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(df.index, df["consumo_kwh"], linewidth=0.8)
        ax.set_title("Consumo eléctrico horario")
        ax.set_ylabel("kWh")
        plt.show()
        """),
        md("""
        ## 2. Forecasting como tabla supervisada

        Un modelo de regresión necesita una tabla de variables (`X`) y una variable objetivo (`y`). Para conseguirlo, convertimos valores pasados en columnas.

        Ejemplos:

        - `lag_1`: consumo de la hora anterior.
        - `lag_24`: consumo a la misma hora del día anterior.
        - `lag_168`: consumo a la misma hora de la semana anterior.
        """),
        code("""
        def crear_variables_forecasting(df):
            datos = df[["consumo_kwh"]].copy()

            for lag in [1, 2, 3, 24, 48, 168]:
                datos[f"lag_{lag}"] = datos["consumo_kwh"].shift(lag)

            datos["media_24h"] = datos["consumo_kwh"].shift(1).rolling(24).mean()
            datos["media_7d"] = datos["consumo_kwh"].shift(1).rolling(24 * 7).mean()
            datos["std_24h"] = datos["consumo_kwh"].shift(1).rolling(24).std()

            datos["hora"] = datos.index.hour
            datos["dia_semana"] = datos.index.dayofweek
            datos["mes"] = datos.index.month
            datos["es_fin_de_semana"] = (datos.index.dayofweek >= 5).astype(int)

            return datos.dropna()


        datos_ml = crear_variables_forecasting(df)
        datos_ml.head()
        """),
        md("""
        ## 3. Evitar fuga de información

        Las medias móviles se calculan con `shift(1)` antes de `rolling`. Así evitamos usar el valor actual para predecirse a sí mismo.

        Correcto:

        ```python
        df["media_24h"] = df["consumo_kwh"].shift(1).rolling(24).mean()
        ```

        Incorrecto:

        ```python
        df["media_24h"] = df["consumo_kwh"].rolling(24).mean()
        ```
        """),
        code("""
        muestra = datos_ml[["consumo_kwh", "lag_1", "lag_24", "lag_168", "media_24h", "media_7d"]].head(10)
        muestra
        """),
        md("""
        ## 4. Definir `X` e `y`

        `y` es el consumo que queremos predecir. `X` contiene los lags, medias móviles y variables de calendario.
        """),
        code("""
        target = "consumo_kwh"
        features = [col for col in datos_ml.columns if col != target]

        X = datos_ml[features]
        y = datos_ml[target]

        X.shape, y.shape
        """),
        md("""
        ## 5. Separación temporal

        En series temporales no hacemos una división aleatoria. El entrenamiento usa el pasado, la validación un periodo posterior y el test queda reservado para el final.
        """),
        code("""
        n = len(datos_ml)
        fin_train = int(n * 0.70)
        fin_validacion = int(n * 0.85)

        X_train = X.iloc[:fin_train]
        y_train = y.iloc[:fin_train]

        X_validacion = X.iloc[fin_train:fin_validacion]
        y_validacion = y.iloc[fin_train:fin_validacion]

        X_test = X.iloc[fin_validacion:]
        y_test = y.iloc[fin_validacion:]

        len(X_train), len(X_validacion), len(X_test)
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(y_train.index, y_train, label="train")
        ax.plot(y_validacion.index, y_validacion, label="validación")
        ax.plot(y_test.index, y_test, label="test")
        ax.set_title("Separación temporal para machine learning")
        ax.set_ylabel("kWh")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 6. Métricas de evaluación

        Usaremos MAE, RMSE y MAPE para comparar modelos sobre el mismo periodo.
        """),
        code("""
        def rmse(y_true, y_pred):
            return np.sqrt(mean_squared_error(y_true, y_pred))


        def mape(y_true, y_pred):
            y_true = np.asarray(y_true)
            y_pred = np.asarray(y_pred)
            mascara = y_true != 0
            return np.mean(np.abs((y_true[mascara] - y_pred[mascara]) / y_true[mascara])) * 100


        def evaluar(y_true, y_pred):
            return {
                "MAE": mean_absolute_error(y_true, y_pred),
                "RMSE": rmse(y_true, y_pred),
                "MAPE": mape(y_true, y_pred),
            }
        """),
        md("""
        ## 7. Baseline: seasonal naive semanal

        Antes de usar ML, necesitamos una referencia. En consumo horario suele ser fuerte usar el valor de la misma hora de la semana anterior.
        """),
        code("""
        historia = y.copy()
        pred_seasonal_7d = historia.shift(24 * 7).loc[y_validacion.index]

        evaluar(y_validacion, pred_seasonal_7d)
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(y_validacion.iloc[:24 * 7], label="real", linewidth=2)
        ax.plot(pred_seasonal_7d.iloc[:24 * 7], label="seasonal naive 7d", linestyle="--")
        ax.set_title("Baseline seasonal naive semanal")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 8. Modelo lineal

        La regresión lineal es una primera referencia supervisada. Si las variables están bien construidas, puede funcionar razonablemente bien.
        """),
        code("""
        modelo_lineal = LinearRegression()
        modelo_lineal.fit(X_train, y_train)

        pred_lineal = pd.Series(
            modelo_lineal.predict(X_validacion),
            index=y_validacion.index,
        )

        evaluar(y_validacion, pred_lineal)
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(y_validacion.iloc[:24 * 7], label="real", linewidth=2)
        ax.plot(pred_lineal.iloc[:24 * 7], label="regresión lineal", linestyle="--")
        ax.set_title("Predicción con regresión lineal")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 9. Random Forest

        Un bosque aleatorio puede capturar relaciones no lineales, aunque también puede sobreajustar si lo dejamos crecer demasiado.
        """),
        code("""
        modelo_rf = RandomForestRegressor(
            n_estimators=200,
            max_depth=12,
            random_state=42,
            n_jobs=-1,
        )

        modelo_rf.fit(X_train, y_train)

        pred_rf = pd.Series(
            modelo_rf.predict(X_validacion),
            index=y_validacion.index,
        )

        evaluar(y_validacion, pred_rf)
        """),
        md("""
        ## 10. Gradient Boosting

        Gradient Boosting construye árboles secuencialmente, corrigiendo errores del modelo anterior.
        """),
        code("""
        modelo_gb = GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=3,
            random_state=42,
        )

        modelo_gb.fit(X_train, y_train)

        pred_gb = pd.Series(
            modelo_gb.predict(X_validacion),
            index=y_validacion.index,
        )

        evaluar(y_validacion, pred_gb)
        """),
        md("""
        ## 11. Comparación de modelos

        Todos los modelos se evalúan en el mismo periodo de validación.
        """),
        code("""
        predicciones = {
            "seasonal_7d": pred_seasonal_7d,
            "linear_regression": pred_lineal,
            "random_forest": pred_rf,
            "gradient_boosting": pred_gb,
        }

        resultados = []
        for nombre, pred in predicciones.items():
            metricas = evaluar(y_validacion, pred)
            metricas["modelo"] = nombre
            resultados.append(metricas)

        tabla_resultados = pd.DataFrame(resultados).set_index("modelo").sort_values("MAE")
        tabla_resultados
        """),
        code("""
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.barplot(data=tabla_resultados.reset_index(), x="MAE", y="modelo", ax=ax, color="tab:blue")
        ax.set_title("Comparación de modelos en validación")
        ax.set_xlabel("MAE")
        ax.set_ylabel("Modelo")
        plt.show()
        """),
        code("""
        mejor_modelo = tabla_resultados.index[0]
        mejor_pred = predicciones[mejor_modelo]

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(y_validacion.iloc[:24 * 10], label="real", linewidth=2)
        ax.plot(mejor_pred.iloc[:24 * 10], label=mejor_modelo, linestyle="--")
        ax.set_title("Mejor modelo en validación")
        ax.legend()
        plt.show()

        mejor_modelo
        """),
        md("""
        ## 12. Importancia de variables

        En modelos basados en árboles podemos mirar qué variables han sido más usadas. Esto no implica causalidad, pero ayuda a interpretar el modelo.
        """),
        code("""
        importancias = pd.Series(modelo_rf.feature_importances_, index=features).sort_values(ascending=False)
        importancias.head(15)
        """),
        code("""
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=importancias.head(15).values, y=importancias.head(15).index, ax=ax, color="tab:green")
        ax.set_title("Importancia de variables - Random Forest")
        ax.set_xlabel("Importancia")
        ax.set_ylabel("Variable")
        plt.show()
        """),
        md("""
        ## 13. Error en entrenamiento frente a validación

        Comparar error de entrenamiento y validación ayuda a detectar sobreajuste o subajuste.
        """),
        code("""
        modelos_entrenados = {
            "linear_regression": modelo_lineal,
            "random_forest": modelo_rf,
            "gradient_boosting": modelo_gb,
        }

        comparacion_train_validacion = []

        for nombre, modelo in modelos_entrenados.items():
            pred_train = modelo.predict(X_train)
            pred_val = modelo.predict(X_validacion)
            comparacion_train_validacion.append({
                "modelo": nombre,
                "MAE_train": mean_absolute_error(y_train, pred_train),
                "MAE_validacion": mean_absolute_error(y_validacion, pred_val),
            })

        pd.DataFrame(comparacion_train_validacion).set_index("modelo")
        """),
        md("""
        ## 14. Evaluación final en test

        El test debe usarse solo al final. Aquí evaluamos el mejor tipo de modelo elegido en validación. Para mantener el ejemplo explícito, usamos Gradient Boosting como candidato supervisado fuerte.
        """),
        code("""
        modelo_final = GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=3,
            random_state=42,
        )

        X_train_final = pd.concat([X_train, X_validacion])
        y_train_final = pd.concat([y_train, y_validacion])

        modelo_final.fit(X_train_final, y_train_final)

        pred_test_ml = pd.Series(
            modelo_final.predict(X_test),
            index=y_test.index,
        )

        pred_test_baseline = y.shift(24 * 7).loc[y_test.index]

        pd.DataFrame({
            "seasonal_7d": evaluar(y_test, pred_test_baseline),
            "gradient_boosting": evaluar(y_test, pred_test_ml),
        }).T
        """),
        code("""
        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(y_test.iloc[:24 * 10], label="real", linewidth=2)
        ax.plot(pred_test_baseline.iloc[:24 * 10], label="seasonal 7d", linestyle="--")
        ax.plot(pred_test_ml.iloc[:24 * 10], label="gradient boosting", linestyle="--")
        ax.set_title("Evaluación final en test")
        ax.legend()
        plt.show()
        """),
        md("""
        ## 15. Modelos globales de forecasting

        En este notebook hemos usado una sola serie. En problemas reales suele haber muchas series: tiendas, productos, sensores o contadores.

        Un modelo local entrena un modelo por serie.

        ```text
        tienda A -> modelo A
        tienda B -> modelo B
        tienda C -> modelo C
        ```

        Un modelo global entrena un único modelo usando todas las series.

        ```text
        tienda A + tienda B + tienda C -> un modelo global
        ```

        En próximas sesiones veremos cómo preparar una tabla con `id_serie` para entrenar modelos globales.
        """),
        md("""
        ## Actividades

        1. Añade `lag_12` y `lag_72`. ¿Mejora algún modelo?
        2. Cambia `max_depth` del random forest y compara train frente a validación.
        3. Añade variables de eventos (`es_festivo`, `campaña`, `ola_calor`) si están disponibles antes de predecir.
        4. Compara el mejor modelo de ML contra `seasonal_24h` y `seasonal_7d`.
        5. Explica si la mejora del modelo ML justifica su uso frente al baseline.
        """),
    ]


def main() -> None:
    global _CELL_COUNTER
    notebooks = {
        "01_introduccion_series_temporales.ipynb": build_01(),
        "02_obtencion_procesamiento_datos.ipynb": build_02(),
        "03_analisis_visualizacion_series_temporales.ipynb": build_03(),
        "04_baselines_evaluacion_forecasting.ipynb": build_04(),
        "05_forecasting_como_regresion.ipynb": build_05(),
    }

    for filename, cells in notebooks.items():
        _CELL_COUNTER = 0
        write_notebook(filename, cells)
        print(f"Creado {filename}")

    runpy.run_path(str(ROOT / "scripts" / "ampliar_notebook_02.py"), run_name="__main__")


if __name__ == "__main__":
    main()
