# AGENTS.md

## Scope
- This is a Spanish teaching repository for a time-series workshop: paired lesson notes (`01_*.md` ... `10_*.md`), executable notebooks, Marp slide sources in `presentaciones/`, synthetic data in `datos/`, and a small importable module under `src/series_temporales/`.
- Keep explanations and learner-facing material in Spanish unless the user asks otherwise.

## Environment
- Install dependencies from the repo root with `pip install -r requirements.txt`; the documented classroom environment is conda/mamba `pia-ud1`.
- There is no packaging config; use `PYTHONPATH=src` for scripts or ad hoc imports from `series_temporales`.
- Deep-learning sessions 07-10 require `torch` and `pytorch-lightning`; `ipywidgets` is included to avoid Jupyter `IProgress not found` warnings.

## Commands
- Regenerate core demo CSVs: `PYTHONPATH=src python scripts/generar_datos_demo.py`.
- Regenerate final-project CSVs: `python scripts/generar_datos_proyecto_07.py`.
- Smoke-test the local module: `PYTHONPATH=src python -c "from series_temporales import generar_consumo_electrico; print(generar_consumo_electrico().shape)"`.
- Execute one notebook from the repo root and write outputs outside the teaching material: `jupyter nbconvert --execute --to notebook --output-dir /tmp/opencode/series_temporales_nbcheck 04_baselines_evaluacion_forecasting.ipynb`.

## Content Conventions
- The `.md` lesson files are full notes; the `.ipynb` files are executable class versions. They are intentionally not literal copies.
- Notebooks and lesson snippets assume the current working directory is the repo root because they load files like `datos/consumo_basico.csv` and append `src` to `sys.path`.
- For slides, edit the Marp Markdown files in `presentaciones/*.md`; existing `.html` files are generated outputs.

## Gotchas
- Do not run `scripts/crear_notebooks_taller.py` casually: it only rebuilds sessions 01-05 plus an older session-02 expansion and can overwrite notebooks that now contain manual fixes for sessions 06-10.
- Treat `lightning_logs/` checkpoints/events and rendered PDFs/HTML as generated artifacts unless the user explicitly asks to update them.
- No pytest, lint, typecheck, CI, lockfile, or formatter config is present; focused verification is by running the affected script or notebook with `nbconvert`.
