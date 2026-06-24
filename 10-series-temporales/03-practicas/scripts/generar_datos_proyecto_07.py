import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Añadir src al path para importar el generador original
raiz = Path(__file__).resolve().parents[1]
sys.path.append(str(raiz / "src"))

from series_temporales.generador_consumo import generar_consumo_electrico

def generar_datos_retail(out_dir):
    np.random.seed(42)
    # Generar tráfico horario de 6 meses
    rango_horas = pd.date_range(start="2026-01-01", end="2026-06-30 23:00:00", freq="h")
    
    # Patrón horario (curva en forma de campana por el día, poco por la noche)
    horas = rango_horas.hour
    patron_diario = np.sin(np.pi * np.clip((horas - 8) / 12, 0, 1)) * 100
    ruido_trafico = np.random.normal(0, 10, len(rango_horas))
    trafico = np.maximum(0, patron_diario + ruido_trafico).astype(int)
    
    df_trafico = pd.DataFrame({"timestamp": rango_horas, "trafico_personas": trafico})
    
    # Generar ventas diarias basadas en el tráfico (solo de lunes a sábado)
    df_trafico["fecha_dia"] = df_trafico["timestamp"].dt.date
    trafico_diario = df_trafico.groupby("fecha_dia")["trafico_personas"].sum()
    
    fechas_diarias = pd.date_range(start="2026-01-01", end="2026-06-30", freq="D")
    df_ventas = pd.DataFrame({"fecha": fechas_diarias})
    
    # Ventas proporcionales al tráfico + un factor de ruido + ticket medio de 15€
    ventas = trafico_diario.values * 15 * np.random.normal(1.0, 0.1, len(fechas_diarias))
    
    df_ventas["ventas_euros"] = ventas.round(2)
    
    # Simular cierre los domingos
    es_domingo = df_ventas["fecha"].dt.dayofweek == 6
    df_ventas.loc[es_domingo, "ventas_euros"] = np.nan
    
    # Limpiar columnas temporales auxiliares
    df_trafico = df_trafico.drop(columns=["fecha_dia"])
    
    df_ventas.to_csv(out_dir / "ventas_diarias.csv", index=False)
    df_trafico.to_csv(out_dir / "trafico_peatonal_horario.csv", index=False)

def generar_datos_energia(out_dir):
    # Usamos el generador del taller, pero a 15 minutos (4 periodos por hora)
    # 3 meses * 30 dias * 24 horas * 4 periodos = 8640 periodos
    df_completo = generar_consumo_electrico(
        fecha_inicio="2026-04-01",
        periodos=24 * 90 * 4,
        frecuencia="15min",
        incluir_meteorologia=True,
        incluir_eventos=False, # Simplificamos para no desviar la atencion
        incluir_huecos=True, # Inyecta huecos simulados (apagones)
        semilla=42
    )

    # 1. Creamos el CSV de consumo a 15 minutos (le quitamos la temperatura)
    columnas_consumo = ["timestamp", "consumo_kwh"]
    df_consumo = df_completo[columnas_consumo].copy()
    
    # El generador_consumo_electrico original mete huecos (es_hueco_simulado)
    # Aseguramos que se plasmen en la columna de consumo_kwh (el generador original ya lo hace)
    
    df_consumo.to_csv(out_dir / "consumo_energia_15min.csv", index=False)

    # 2. Creamos el CSV de Clima separándolo, y haciendo downsampling a 1 Hora
    # Nos quedamos solo con las filas en punto (minuto == 0)
    df_clima_horario = df_completo[df_completo["timestamp"].dt.minute == 0].copy()
    
    columnas_clima = ["timestamp", "temperatura"]
    df_clima_horario = df_clima_horario[columnas_clima]
    
    # Guardamos el clima a 1 hora
    df_clima_horario.to_csv(out_dir / "clima_horario.csv", index=False)

if __name__ == "__main__":
    out_dir = raiz / "datos"
    out_dir.mkdir(exist_ok=True)
    
    print("Generando datasets para la Sesión 07 usando el src original...")
    generar_datos_retail(out_dir)
    generar_datos_energia(out_dir)
    print("¡Generación completada! Archivos guardados en la carpeta 'datos/'.")
