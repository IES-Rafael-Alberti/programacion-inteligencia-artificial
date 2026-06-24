"""Generadores de datos sintéticos para el taller de series temporales.

El objetivo no es simular el sistema eléctrico con precisión física, sino crear
series plausibles y controlables para explicar conceptos de forecasting.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ConfiguracionConsumo:
    """Parámetros principales del generador de consumo eléctrico."""

    fecha_inicio: str = "2026-01-01"
    periodos: int = 24 * 180
    frecuencia: str = "h"
    consumo_base: float = 1.8
    tendencia_total: float = 0.25
    amplitud_diaria: float = 0.55
    amplitud_semanal: float = 0.18
    amplitud_anual: float = 0.20
    ruido: float = 0.08
    semilla: int = 42


def generar_meteorologia(
    fechas: pd.DatetimeIndex,
    semilla: int = 42,
) -> pd.DataFrame:
    """Genera temperatura sintética asociada a las fechas.

    La temperatura combina un ciclo anual, un ciclo diario y ruido. Se devuelve
    en un DataFrame para poder unirla fácilmente con la serie de consumo.
    """

    rng = np.random.default_rng(semilla)
    pasos = np.arange(len(fechas))
    hora = fechas.hour.to_numpy()
    dia_anyo = fechas.dayofyear.to_numpy()

    temperatura_anual = 17 + 9 * np.sin(2 * np.pi * (dia_anyo - 80) / 365)
    temperatura_diaria = 4 * np.sin(2 * np.pi * (hora - 14) / 24)
    ruido = rng.normal(0, 1.2, len(fechas))

    temperatura = temperatura_anual + temperatura_diaria + ruido

    return pd.DataFrame(
        {
            "timestamp": fechas,
            "temperatura": temperatura,
        }
    )


def generar_eventos(
    fechas: pd.DatetimeIndex,
    semilla: int = 42,
) -> pd.DataFrame:
    """Genera eventos externos simulados.

    Incluye festivos, campaña especial y ola de calor. Estos eventos permiten
    explicar variables exógenas sin depender de fuentes externas.
    """

    rng = np.random.default_rng(semilla)
    eventos = pd.DataFrame({"timestamp": fechas})
    eventos["es_festivo"] = False
    eventos["campaña"] = False
    eventos["ola_calor"] = False

    dias_unicos = pd.DatetimeIndex(fechas.normalize().unique())
    n_festivos = max(3, len(dias_unicos) // 35)
    festivos = rng.choice(dias_unicos, size=n_festivos, replace=False)
    eventos.loc[eventos["timestamp"].dt.normalize().isin(festivos), "es_festivo"] = True

    if len(dias_unicos) >= 60:
        inicio_campaña = dias_unicos[len(dias_unicos) // 3]
        fin_campaña = inicio_campaña + pd.Timedelta(days=10)
        eventos.loc[
            eventos["timestamp"].between(inicio_campaña, fin_campaña, inclusive="left"),
            "campaña",
        ] = True

    if len(dias_unicos) >= 90:
        inicio_ola = dias_unicos[(2 * len(dias_unicos)) // 3]
        fin_ola = inicio_ola + pd.Timedelta(days=7)
        eventos.loc[
            eventos["timestamp"].between(inicio_ola, fin_ola, inclusive="left"),
            "ola_calor",
        ] = True

    return eventos


def generar_consumo_electrico(
    fecha_inicio: str = "2026-01-01",
    periodos: int = 24 * 180,
    frecuencia: str = "h",
    semilla: int = 42,
    incluir_meteorologia: bool = False,
    incluir_eventos: bool = False,
    incluir_huecos: bool = False,
    incluir_outliers: bool = False,
) -> pd.DataFrame:
    """Genera una serie sintética de consumo eléctrico horario.

    Parámetros principales:
    - `incluir_meteorologia`: añade temperatura y efecto por frío/calor.
    - `incluir_eventos`: añade festivos, campaña y ola de calor.
    - `incluir_huecos`: introduce valores perdidos aislados y un hueco largo.
    - `incluir_outliers`: introduce picos y caídas artificiales.
    """

    cfg = ConfiguracionConsumo(
        fecha_inicio=fecha_inicio,
        periodos=periodos,
        frecuencia=frecuencia,
        semilla=semilla,
    )

    rng = np.random.default_rng(cfg.semilla)
    fechas = pd.date_range(cfg.fecha_inicio, periods=cfg.periodos, freq=cfg.frecuencia)
    pasos = np.arange(cfg.periodos)
    hora = fechas.hour.to_numpy()
    dia_semana = fechas.dayofweek.to_numpy()
    dia_anyo = fechas.dayofyear.to_numpy()

    tendencia = np.linspace(0, cfg.tendencia_total, cfg.periodos)

    perfil_diario = cfg.amplitud_diaria * (
        0.65 * np.sin(2 * np.pi * (hora - 7) / 24)
        + 0.35 * np.sin(4 * np.pi * (hora - 17) / 24)
    )
    perfil_diario = perfil_diario - perfil_diario.min()

    efecto_fin_semana = np.where(dia_semana >= 5, -cfg.amplitud_semanal, 0)
    estacionalidad_anual = cfg.amplitud_anual * np.sin(2 * np.pi * (dia_anyo - 20) / 365)
    ruido = rng.normal(0, cfg.ruido, cfg.periodos)

    consumo = (
        cfg.consumo_base
        + tendencia
        + perfil_diario
        + efecto_fin_semana
        + estacionalidad_anual
        + ruido
    )

    df = pd.DataFrame(
        {
            "timestamp": fechas,
            "consumo_kwh": consumo,
            "tendencia": cfg.consumo_base + tendencia,
            "componente_diaria": perfil_diario,
            "componente_semanal": efecto_fin_semana,
            "componente_anual": estacionalidad_anual,
            "ruido": ruido,
        }
    )

    if incluir_meteorologia:
        meteo = generar_meteorologia(fechas, semilla=semilla + 1)
        df = df.merge(meteo, on="timestamp", how="left")
        frio = np.clip(15 - df["temperatura"], 0, None) * 0.025
        calor = np.clip(df["temperatura"] - 26, 0, None) * 0.045
        df["efecto_temperatura"] = frio + calor
        df["consumo_kwh"] = df["consumo_kwh"] + df["efecto_temperatura"]

    if incluir_eventos:
        eventos = generar_eventos(fechas, semilla=semilla + 2)
        df = df.merge(eventos, on="timestamp", how="left")
        df["efecto_eventos"] = 0.0
        df.loc[df["es_festivo"], "efecto_eventos"] -= 0.25
        df.loc[df["campaña"], "efecto_eventos"] += 0.18
        df.loc[df["ola_calor"], "efecto_eventos"] += 0.30
        df["consumo_kwh"] = df["consumo_kwh"] + df["efecto_eventos"]
    else:
        df["es_festivo"] = False
        df["campaña"] = False
        df["ola_calor"] = False

    df["consumo_kwh"] = df["consumo_kwh"].clip(lower=0.05)

    if incluir_outliers:
        n_outliers = max(4, cfg.periodos // 400)
        posiciones = rng.choice(cfg.periodos, size=n_outliers, replace=False)
        mitad = n_outliers // 2
        df["es_outlier_simulado"] = False
        df.loc[posiciones[:mitad], "consumo_kwh"] *= rng.uniform(1.8, 2.6, mitad)
        df.loc[posiciones[mitad:], "consumo_kwh"] *= rng.uniform(0.15, 0.45, n_outliers - mitad)
        df.loc[posiciones, "es_outlier_simulado"] = True
    else:
        df["es_outlier_simulado"] = False

    if incluir_huecos:
        df["es_hueco_simulado"] = False
        n_huecos_aislados = max(5, cfg.periodos // 250)
        posiciones = rng.choice(cfg.periodos, size=n_huecos_aislados, replace=False)
        df.loc[posiciones, "consumo_kwh"] = np.nan
        df.loc[posiciones, "es_hueco_simulado"] = True

        if cfg.periodos >= 24 * 30:
            inicio = cfg.periodos // 2
            fin = min(inicio + 12, cfg.periodos)
            df.loc[inicio:fin, "consumo_kwh"] = np.nan
            df.loc[inicio:fin, "es_hueco_simulado"] = True
    else:
        df["es_hueco_simulado"] = False

    df["hora"] = df["timestamp"].dt.hour
    df["dia_semana"] = df["timestamp"].dt.dayofweek
    df["mes"] = df["timestamp"].dt.month
    df["es_fin_de_semana"] = df["dia_semana"] >= 5

    columnas_base = [
        "timestamp",
        "consumo_kwh",
        "hora",
        "dia_semana",
        "mes",
        "es_fin_de_semana",
        "es_festivo",
        "campaña",
        "ola_calor",
        "es_outlier_simulado",
        "es_hueco_simulado",
    ]
    columnas_componentes = [col for col in df.columns if col not in columnas_base]

    return df[columnas_base + columnas_componentes]
