"""Genera CSV de ejemplo para las demos del taller."""

from pathlib import Path

from series_temporales import generar_consumo_electrico


def main() -> None:
    raiz = Path(__file__).resolve().parents[1]
    salida = raiz / "datos"
    salida.mkdir(exist_ok=True)

    escenarios = {
        "consumo_basico.csv": dict(),
        "consumo_con_meteo.csv": dict(incluir_meteorologia=True),
        "consumo_con_eventos.csv": dict(incluir_meteorologia=True, incluir_eventos=True),
        "consumo_realista.csv": dict(
            incluir_meteorologia=True,
            incluir_eventos=True,
            incluir_huecos=True,
            incluir_outliers=True,
        ),
    }

    for nombre, opciones in escenarios.items():
        df = generar_consumo_electrico(**opciones)
        df.to_csv(salida / nombre, index=False)
        print(f"Generado {nombre}: {len(df)} filas")


if __name__ == "__main__":
    main()
