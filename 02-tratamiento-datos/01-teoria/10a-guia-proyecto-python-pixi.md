# Guía de proyecto de tratamiento de datos con Python, Pixi y conda

Esta guía acompaña a UD2: no sustituye al [manual general de Pixi](../../docs/manual-pixi-pia.md). El alcance formativo es **Python 3.12**, NumPy, pandas, Matplotlib, Jupyter y el trabajo de EDA, limpieza, transformación, agrupación, exportación y visualización. No incluye scikit-learn, PyCaret, XGBoost, entrenamiento, inferencia, APIs ni datasets de ML.

## Ruta recomendada: Pixi

En la raíz del repositorio se versionan `pixi.toml` y `pixi.lock`. Desde esa carpeta:

```bash
pixi install
pixi run --environment default python --version
pixi run --environment default python -c "import numpy, pandas; print(numpy.__version__, pandas.__version__)"
pixi run --environment default jupyter lab
```

La comprobación debe confirmar Python 3.12 y las versiones efectivamente resueltas. **Advertencia:** en el `pixi.toml` actual Matplotlib está declarado en `ud3`, no en `base/default`; por tanto no se debe afirmar que `default` ya lo contiene. Antes de impartir visualización hay que declararlo en la feature o entorno de UD2, o usar la ruta conda siguiente. La decisión de modificar el manifiesto y regenerar `pixi.lock` queda pendiente.

## Ruta alternativa: conda

Para un entorno reutilizable y específico de UD2:

```bash
conda create -n pia-ud2 -c conda-forge python=3.12 "numpy>=2,<3" "pandas>=2.2,<3" "matplotlib>=3.8,<4" jupyterlab ipykernel
conda activate pia-ud2
python --version
python -c "import numpy, pandas, matplotlib; print(numpy.__version__, pandas.__version__, matplotlib.__version__)"
jupyter lab
conda env export --from-history > pia-ud2.yml
conda env update -n pia-ud2 --file pia-ud2.yml --prune
conda deactivate
```

El `environment.yml` de la raíz está sobredimensionado para UD2: no debe presentarse como entorno mínimo. No se mezclan instalaciones Pixi y conda sin criterio; se elige una ruta para el proyecto y se documenta.

## Pixi o conda

Pixi es preferible cuando el proyecto viaja con `pixi.toml`/`pixi.lock` y necesita features o entornos por proyecto. Conda resulta útil para experimentar con un entorno nombrado y paquetes nativos. En ambos casos se conserva la especificación y se actualiza el entorno, en lugar de crear uno por cada prueba.

Una estructura razonable es:

```text
proyecto-datos/
|-- data/
|-- notebooks/
|-- src/          # o scripts/
`-- outputs/figures/
```

### Checklist reproducible

- [ ] Alcance y versiones de Python y paquetes documentados.
- [ ] `pixi.toml` + `pixi.lock`, o `pia-ud2.yml` exportado con `--from-history`.
- [ ] Comandos ejecutados desde la raíz del proyecto y entorno comprobado.
- [ ] Datos de entrada, notebooks/scripts y figuras separados.
- [ ] Resultados exportados en `outputs/`, sin sobrescribir los datos originales.
- [ ] Otra persona puede instalar, abrir Jupyter y repetir el análisis.

Más información: [manual de Pixi](../../docs/manual-pixi-pia.md), [guía de inicio](../../docs/guia-inicio.md), [entornos de Python](../../docs/entornos-python.md).
