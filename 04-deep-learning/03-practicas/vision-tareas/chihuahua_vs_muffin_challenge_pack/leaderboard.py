
import csv
from pathlib import Path

CSV_PATH = Path("leaderboard_template.csv")

def cargar_resultados(path=CSV_PATH):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["Accuracy_num"] = float(row["Accuracy"]) if row["Accuracy"] else -1.0
            except ValueError:
                row["Accuracy_num"] = -1.0
            rows.append(row)
    return rows

def imprimir_leaderboard(rows):
    rows = sorted(rows, key=lambda r: r["Accuracy_num"], reverse=True)
    print("=" * 70)
    print("LEADERBOARD — IA VISION CHALLENGE")
    print("=" * 70)
    print(f"{'#':<3} {'Equipo':<20} {'Accuracy':<10} {'Modelo':<18} Comentarios")
    print("-" * 70)
    for i, row in enumerate(rows, start=1):
        acc = row["Accuracy"] if row["Accuracy"] else "-"
        print(f"{i:<3} {row['Equipo']:<20} {acc:<10} {row['Modelo']:<18} {row['Comentarios']}")
    print("-" * 70)

if __name__ == "__main__":
    rows = cargar_resultados()
    imprimir_leaderboard(rows)
