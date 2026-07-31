#!/usr/bin/env python3
"""Comprueba la navegación pública de las doce páginas de unidad."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


SECTION_NAMES = ("Teoría", "Ejemplos", "Prácticas", "Evaluación", "Recursos")
REPOSITORY_URL = "https://github.com/IES-Rafael-Alberti/programacion-inteligencia-artificial/"
REPOSITORY_TREE_PREFIX = f"{REPOSITORY_URL}tree/main/"
ROW_PATTERN = re.compile(
    r"^\|\s*(Teoría|Ejemplos|Prácticas|Evaluación|Recursos)\s*\|\s*(.*?)\s*\|$"
)


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.hrefs.append(href)


def generated_target(page: Path, href: str, site_dir: Path) -> Path | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith(("#", "mailto:", "javascript:")):
        return None

    raw_path = unquote(parsed.path)
    if not raw_path:
        return None

    relative_page = page.relative_to(site_dir)
    base = relative_page.parent
    target = (site_dir / base / raw_path).resolve()
    site_root = site_dir.resolve()
    if site_root not in target.parents and target != site_root:
        raise ValueError(f"El enlace sale de site/: {href}")
    if raw_path.endswith("/") or not target.suffix:
        target /= "index.html"
    return target


def check_source_contract(repo_root: Path) -> list[str]:
    errors: list[str] = []
    section_count = 0
    link_count = 0
    empty_count = 0
    for number in range(1, 13):
        source = repo_root / "docs" / "unidades" / f"ud{number:02}.md"
        rows: dict[str, str] = {}
        for line in source.read_text(encoding="utf-8").splitlines():
            match = ROW_PATTERN.match(line)
            if match:
                rows[match.group(1)] = match.group(2)

        missing = set(SECTION_NAMES) - rows.keys()
        if missing:
            errors.append(f"{source}: faltan secciones: {', '.join(sorted(missing))}")
        section_count += len(rows)

        for name, value in rows.items():
            if "](../" in value:
                link = re.search(r"\]\(([^)]+)\)", value)
                if link:
                    link_count += 1
                    target = (source.parent / link.group(1)).resolve()
                    if not target.is_file():
                        errors.append(f"{source}: {name} apunta a un Markdown inexistente: {link.group(1)}")
            elif REPOSITORY_TREE_PREFIX in value:
                link = re.search(r"\]\(([^)]+)\)", value)
                if link:
                    link_count += 1
                    relative = link.group(1).removeprefix(REPOSITORY_TREE_PREFIX)
                    target = repo_root / unquote(relative)
                    if not target.exists():
                        errors.append(f"{source}: {name} apunta a una ruta inexistente del repositorio: {relative}")
            elif "No hay material publicado" in value:
                empty_count += 1
            else:
                errors.append(f"{source}: {name} no tiene destino ni estado explícito")

    if section_count != 60:
        errors.append(f"Se esperaban 60 entradas de sección y se encontraron {section_count}")
    if link_count != 55 or empty_count != 5:
        errors.append(
            "Se esperaban 55 secciones con destino y 5 sin material; "
            f"se encontraron {link_count} y {empty_count}"
        )
    return errors


def check_generated_links(repo_root: Path, site_dir: Path) -> list[str]:
    errors: list[str] = []
    for number in range(1, 13):
        page = site_dir / "unidades" / f"ud{number:02}" / "index.html"
        if not page.is_file():
            errors.append(f"No se generó {page}")
            continue
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for href in parser.hrefs:
            try:
                target = generated_target(page, href, site_dir)
            except ValueError as error:
                errors.append(f"{page}: {error}")
                continue
            if target is not None and not target.exists():
                errors.append(f"{page}: enlace generado roto: {href} -> {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default="site", type=Path)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    site_dir = args.site_dir if args.site_dir.is_absolute() else repo_root / args.site_dir
    errors = check_source_contract(repo_root) + check_generated_links(repo_root, site_dir)
    if errors:
        print("Navegación pública incorrecta:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Navegación pública validada: 12 unidades y 60 secciones revisadas "
        "(55 con destino y 5 sin material); cero enlaces internos rotos."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
