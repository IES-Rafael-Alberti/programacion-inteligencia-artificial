"""Minimax y poda alfa-beta para tres en raya, sin dependencias externas."""

from __future__ import annotations

from math import inf

Board = list[str]
WINNING_LINES: tuple[tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def winner(board: Board) -> str | None:
    """Devuelve X u O si hay ganador; en otro caso, None."""
    for first, second, third in WINNING_LINES:
        if board[first] != " " and board[first] == board[second] == board[third]:
            return board[first]
    return None


def available_moves(board: Board) -> list[int]:
    return [index for index, cell in enumerate(board) if cell == " "]


def terminal_score(board: Board) -> int | None:
    """Evalúa el estado desde la perspectiva de X; None si sigue la partida."""
    result = winner(board)
    if result == "X":
        return 1
    if result == "O":
        return -1
    if not available_moves(board):
        return 0
    return None


def minimax(
    board: Board,
    maximizing: bool,
    alpha: float = -inf,
    beta: float = inf,
    use_alpha_beta: bool = True,
    counter: list[int] | None = None,
) -> tuple[int, int | None]:
    """Devuelve (valor, mejor jugada); X maximiza y O minimiza."""
    if counter is not None:
        counter[0] += 1

    score = terminal_score(board)
    if score is not None:
        return score, None

    best_move = None
    if maximizing:
        best_score = -inf
        for move in available_moves(board):
            board[move] = "X"
            child_score, _ = minimax(
                board, False, alpha, beta, use_alpha_beta, counter
            )
            board[move] = " "

            if child_score > best_score:
                best_score, best_move = child_score, move
            alpha = max(alpha, best_score)
            if use_alpha_beta and alpha >= beta:
                break
        return int(best_score), best_move

    best_score = inf
    for move in available_moves(board):
        board[move] = "O"
        child_score, _ = minimax(
            board, True, alpha, beta, use_alpha_beta, counter
        )
        board[move] = " "

        if child_score < best_score:
            best_score, best_move = child_score, move
        beta = min(beta, best_score)
        if use_alpha_beta and alpha >= beta:
            break
    return int(best_score), best_move


def display(board: Board) -> str:
    rows = [" | ".join(board[offset : offset + 3]) for offset in (0, 3, 6)]
    return "\n---------\n".join(rows)


def main() -> None:
    # Comparamos el árbol completo desde la posición inicial.
    empty_board = [" "] * 9
    plain_count = [0]
    pruned_count = [0]
    plain_score, plain_move = minimax(
        empty_board.copy(), True, use_alpha_beta=False, counter=plain_count
    )
    pruned_score, pruned_move = minimax(
        empty_board.copy(), True, use_alpha_beta=True, counter=pruned_count
    )

    print("Posición inicial:")
    print(display(empty_board))
    print(f"\nMinimax sin poda: valor={plain_score}, jugada={plain_move}")
    print(f"Nodos examinados: {plain_count[0]}")
    print(f"Minimax con alfa-beta: valor={pruned_score}, jugada={pruned_move}")
    print(f"Nodos examinados: {pruned_count[0]}")

    assert plain_score == pruned_score
    assert plain_move == pruned_move
    assert pruned_count[0] <= plain_count[0]

    # Ejemplo táctico: X puede ganar inmediatamente en la casilla central superior.
    tactical_board = ["X", "X", " ", "O", "O", " ", " ", " ", " "]
    score, move = minimax(tactical_board, True)
    print("\nPosición táctica:")
    print(display(tactical_board))
    print(f"Jugada elegida para X: {move}, valor minimax: {score}")
    assert move == 2 and score == 1


if __name__ == "__main__":
    main()
