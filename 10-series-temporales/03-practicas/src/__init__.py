"""Utilidades para el taller de series temporales."""

from .generador_consumo import (
    generar_consumo_electrico,
    generar_eventos,
    generar_meteorologia,
)

__all__ = [
    "generar_consumo_electrico",
    "generar_eventos",
    "generar_meteorologia",
]
