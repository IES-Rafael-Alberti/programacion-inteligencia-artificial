import os
import re
from pathlib import Path


EXCLUDE_DIRS = {
    '.atl',
    '.git',
    '.ipynb_checkpoints',
    '.mypy_cache',
    '.pytest_cache',
    '.ruff_cache',
    '.venv',
    '__pycache__',
    '_profesor',
    '00-planificación',
    '90-archivo',
    '90-archivo-historico',
    '99-profesor',
    '99-sensible',
    'env',
    'openspec',
    'site',
    'venv',
}

EXCLUDE_FILES = {
    '.env',
    '.gitattributes',
    '.gitignore',
    'README_Docente.md',
}

EXCLUDE_SUFFIXES = {
    '.7z',
    '.csv',
    '.docx',
    '.gz',
    '.html',
    '.ipynb',
    '.json',
    '.key',
    '.p12',
    '.parquet',
    '.pdf',
    '.pem',
    '.pptx',
    '.py',
    '.rar',
    '.rmd',
    '.tar',
    '.tgz',
    '.zip',
}

SECTION_ORDER = {
    '01-teoria': 'Teoría',
    '02-ejemplos': 'Ejemplos',
    '03-practicas': 'Prácticas',
    '04-evaluacion': 'Evaluación',
    '05-recursos': 'Recursos',
    '06-extra': 'Extra',
}
SECTION_KEYS = set(SECTION_ORDER)

UNIT_NAMES = {
    '01-fundamentos-python': ('UD1 — Fundamentos de Python', 'unidades/ud01.md'),
    '02-tratamiento-datos': ('UD2 — Tratamiento de Datos', 'unidades/ud02.md'),
    '03-machine-learning': ('UD3 — Machine Learning', 'unidades/ud03.md'),
    '04-deep-learning': ('UD4 — Deep Learning', 'unidades/ud04.md'),
    '05-cloud-mlops': ('UD5 — Cloud y MLOps', 'unidades/ud05.md'),
    '06-llm-agentes': ('UD6 — LLM y Agentes', 'unidades/ud06.md'),
    '07-convergencia-herramientas': ('UD7 — Convergencia de Herramientas', 'unidades/ud07.md'),
    '08-vision-xai': ('UD8 — Visión y XAI', 'unidades/ud08.md'),
    '09-gpu-avanzado': ('UD9 — GPU Avanzado', 'unidades/ud09.md'),
    '10-series-temporales': ('UD10 — Series Temporales', 'unidades/ud10.md'),
    '11-anexos': ('UD11 — Anexos', 'unidades/ud11.md'),
    '12-proyecto-integrado': ('UD12 — Proyecto Integrado', 'unidades/ud12.md'),
}


def should_exclude_path(path: Path) -> bool:
    parts = set(path.parts)
    if parts.intersection(EXCLUDE_DIRS):
        return True

    name = path.name
    if name.startswith('.') or name in EXCLUDE_FILES:
        return True

    lower_name = name.lower()
    if 'profesor' in lower_name:
        return True
    if 'api' in lower_name and 'key' in lower_name:
        return True

    return any(lower_name.endswith(suffix) for suffix in EXCLUDE_SUFFIXES)


def clean_title(filename: str) -> str:
    name = filename.removesuffix('.md')
    name = re.sub(r'^UD\d+(_[A-Z]\d+)?_', '', name, flags=re.IGNORECASE)
    name = re.sub(r'^\d{2,3}-', '', name)
    name = name.replace('_', ' ').replace('-', ' ').replace('.', ' ')
    name = re.sub(r'\s+', ' ', name).strip()
    if len(name) > 75:
        name = f'{name[:72]}...'
    return name or filename.removesuffix('.md')


def scan_files(dirpath: Path, docs_dir: Path):
    entries = []
    try:
        items = sorted(dirpath.iterdir(), key=lambda p: p.name.lower())
    except (FileNotFoundError, PermissionError):
        return entries

    for path in items:
        if should_exclude_path(path):
            continue

        if path.is_dir():
            sub = scan_files(path, docs_dir)
            if sub:
                entries.append({clean_title(path.name): sub})
        elif path.is_file() and path.suffix == '.md':
            rel = str(path.relative_to(docs_dir))
            entries.append({clean_title(path.name): rel})

    return entries


def scan_unit(unit_symlink: Path, docs_dir: Path, index_path: str):
    children = [{'Guía de la unidad': index_path}]

    readme = unit_symlink / 'README.md'
    if readme.is_file() and not should_exclude_path(readme):
        children.append({'README de la unidad': str(readme.relative_to(docs_dir))})

    try:
        top_items = sorted(unit_symlink.iterdir(), key=lambda p: p.name.lower())
    except (FileNotFoundError, PermissionError):
        return children

    for path in top_items:
        if path.name == 'README.md' or should_exclude_path(path):
            continue
        if path.is_file() and path.suffix == '.md':
            rel = str(path.relative_to(docs_dir))
            children.append({clean_title(path.name): rel})

    for section_key, section_title in SECTION_ORDER.items():
        section_path = unit_symlink / section_key
        if not section_path.is_dir() or should_exclude_path(section_path):
            continue
        entries = scan_files(section_path, docs_dir)
        if entries:
            children.append({section_title: entries})

    for path in top_items:
        if should_exclude_path(path) or not path.is_dir() or path.name in SECTION_KEYS:
            continue
        entries = scan_files(path, docs_dir)
        if entries:
            children.append({clean_title(path.name): entries})

    return children


def on_config(config):
    docs_dir = Path(config['docs_dir']).resolve()
    nav = [{'Inicio': 'index.md'}]

    for unit_dirname, (unit_title, index_path) in UNIT_NAMES.items():
        unit_symlink = docs_dir / unit_dirname
        if not unit_symlink.exists() or should_exclude_path(unit_symlink):
            continue
        children = scan_unit(unit_symlink, docs_dir, index_path)
        nav.append({unit_title: children})

    config['nav'] = nav
    return config
