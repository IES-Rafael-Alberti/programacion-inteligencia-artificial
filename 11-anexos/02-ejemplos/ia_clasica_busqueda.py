"""Búsqueda DFS, BFS y A* en una cuadrícula pequeña, sin dependencias externas."""

from __future__ import annotations

from collections import deque
from heapq import heappop, heappush
from itertools import count
from typing import Callable

Position = tuple[int, int]
Grid = tuple[str, ...]

GRID: Grid = (
    "S...#...",
    ".#..#...",
    ".#......",
    "...###..",
    "......#.",
    "##...#..",
    "...#...G",
)

MOVES: tuple[Position, ...] = ((-1, 0), (1, 0), (0, -1), (0, 1))


def locate(grid: Grid, marker: str) -> Position:
    """Devuelve la coordenada del marcador indicado."""
    for row, line in enumerate(grid):
        column = line.find(marker)
        if column >= 0:
            return row, column
    raise ValueError(f"No se encuentra el marcador {marker!r}.")


def neighbours(grid: Grid, position: Position) -> list[Position]:
    """Enumera vecinos transitables dentro de los límites de la cuadrícula."""
    rows, columns = len(grid), len(grid[0])
    row, column = position
    result = []
    for delta_row, delta_column in MOVES:
        next_row, next_column = row + delta_row, column + delta_column
        if (
            0 <= next_row < rows
            and 0 <= next_column < columns
            and grid[next_row][next_column] != "#"
        ):
            result.append((next_row, next_column))
    return result


def reconstruct_path(
    parents: dict[Position, Position | None], goal: Position
) -> list[Position]:
    """Reconstruye la ruta desde el inicio usando el mapa de predecesores."""
    path = []
    current: Position | None = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path


def depth_first_search(
    grid: Grid, start: Position, goal: Position
) -> tuple[list[Position] | None, int]:
    """Busca en profundidad. No garantiza la ruta más corta."""
    frontier = [start]
    parents: dict[Position, Position | None] = {start: None}
    expanded = 0

    while frontier:
        current = frontier.pop()
        expanded += 1
        if current == goal:
            return reconstruct_path(parents, goal), expanded

        for neighbour in neighbours(grid, current):
            if neighbour not in parents:
                parents[neighbour] = current
                frontier.append(neighbour)

    return None, expanded


def breadth_first_search(
    grid: Grid, start: Position, goal: Position
) -> tuple[list[Position] | None, int]:
    """Busca por niveles; con costes unitarios encuentra una ruta mínima."""
    frontier = deque([start])
    parents: dict[Position, Position | None] = {start: None}
    expanded = 0

    while frontier:
        current = frontier.popleft()
        expanded += 1
        if current == goal:
            return reconstruct_path(parents, goal), expanded

        for neighbour in neighbours(grid, current):
            if neighbour not in parents:
                parents[neighbour] = current
                frontier.append(neighbour)

    return None, expanded


def manhattan(first: Position, second: Position) -> int:
    """Distancia adecuada para movimientos ortogonales de coste unitario."""
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def a_star_search(
    grid: Grid,
    start: Position,
    goal: Position,
    heuristic: Callable[[Position, Position], int] = manhattan,
) -> tuple[list[Position] | None, int]:
    """Busca el camino de menor coste con una heurística admisible."""
    tie_breaker = count()
    frontier: list[tuple[int, int, Position]] = []
    heappush(frontier, (heuristic(start, goal), next(tie_breaker), start))

    parents: dict[Position, Position | None] = {start: None}
    costs: dict[Position, int] = {start: 0}
    expanded = 0

    while frontier:
        _, _, current = heappop(frontier)
        expanded += 1
        if current == goal:
            return reconstruct_path(parents, goal), expanded

        for neighbour in neighbours(grid, current):
            new_cost = costs[current] + 1
            if new_cost < costs.get(neighbour, float("inf")):
                costs[neighbour] = new_cost
                parents[neighbour] = current
                priority = new_cost + heuristic(neighbour, goal)
                heappush(frontier, (priority, next(tie_breaker), neighbour))

    return None, expanded


def display(grid: Grid, path: list[Position] | None) -> str:
    """Dibuja la cuadrícula y marca la ruta con puntos."""
    cells = [list(row) for row in grid]
    if path:
        for row, column in path:
            if cells[row][column] not in {"S", "G"}:
                cells[row][column] = "*"
    return "\n".join("".join(row) for row in cells)


def main() -> None:
    start, goal = locate(GRID, "S"), locate(GRID, "G")
    algorithms = (
        ("DFS", depth_first_search),
        ("BFS", breadth_first_search),
        ("A*", a_star_search),
    )

    print("Laberinto inicial:")
    print(display(GRID, None))

    results = {}
    for name, search in algorithms:
        path, expanded = search(GRID, start, goal)
        results[name] = path
        length = len(path) - 1 if path else None
        print(f"\n{name}: longitud={length}, estados expandidos={expanded}")
        print(display(GRID, path))

    # Con costes unitarios y Manhattan admisible, BFS y A* dan rutas mínimas.
    assert results["BFS"] is not None
    assert results["A*"] is not None
    assert len(results["BFS"]) == len(results["A*"])


if __name__ == "__main__":
    main()
