"""
Script para generar imágenes ilustrativas del Capítulo 5
La función de pérdida
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D

img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

# ============================================================================
# IMAGEN 1: Concepto de Función de Pérdida
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 7))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Función de Pérdida: Medida del Error', fontsize=13, fontweight='bold', pad=20)

# Valores reales
rect1 = FancyBboxPatch((1, 6), 2.5, 1.5, boxstyle='round,pad=0.1',
                      edgecolor='#2ca02c', facecolor='#98D8C8', linewidth=2)
ax.add_patch(rect1)
ax.text(2.25, 6.75, 'Valores\nReales\ny', ha='center', va='center', fontsize=10, fontweight='bold')

# Valores predichos
rect2 = FancyBboxPatch((5, 6), 2.5, 1.5, boxstyle='round,pad=0.1',
                      edgecolor='#ff7f0e', facecolor='#FFE5CC', linewidth=2)
ax.add_patch(rect2)
ax.text(6.25, 6.75, 'Valores\nPredichos\nŷ', ha='center', va='center', fontsize=10, fontweight='bold')

# Función de pérdida
rect3 = FancyBboxPatch((9, 6), 2.5, 1.5, boxstyle='round,pad=0.1',
                      edgecolor='#d62728', facecolor='#F5B7B1', linewidth=2)
ax.add_patch(rect3)
ax.text(10.25, 6.75, 'Pérdida\nL(y, ŷ)', ha='center', va='center', fontsize=10, fontweight='bold')

# Flechas
arrow1 = FancyArrowPatch((3.6, 6.75), (4.9, 6.75),
                        arrowstyle='->', mutation_scale=25, linewidth=2, color='gray')
ax.add_patch(arrow1)
ax.text(4.25, 7.3, 'Comparar', ha='center', fontsize=9, style='italic')

arrow2 = FancyArrowPatch((7.6, 6.75), (8.9, 6.75),
                        arrowstyle='->', mutation_scale=25, linewidth=2, color='gray')
ax.add_patch(arrow2)
ax.text(8.25, 7.3, 'Medir error', ha='center', fontsize=9, style='italic')

# Ejemplos
examples = [
    ('Regresión: MSE', 2.25, 4.5, 'L = (y - ŷ)²'),
    ('Clasificación: CE', 6.25, 4.5, 'L = -y log(ŷ)'),
]

for title, x, y, formula in examples:
    rect = FancyBboxPatch((x-1.2, y-0.5), 2.4, 1, boxstyle='round,pad=0.05',
                         edgecolor='black', facecolor='#E8F4F8', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, y + 0.2, title, ha='center', fontsize=9, fontweight='bold')
    ax.text(x, y - 0.2, formula, ha='center', fontsize=8, style='italic', family='monospace')

# Clave
key_text = (
    "Pérdida alta → Modelo malo\n"
    "Pérdida baja → Modelo bueno\n"
    "Objetivo: Minimizar la pérdida"
)
ax.text(6.5, 2, key_text, ha='center', fontsize=10,
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFFCC', alpha=0.8))

plt.tight_layout()
plt.savefig(img_dir / '25_concepto_perdida.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 1 creada: 25_concepto_perdida.png")
plt.close()

# ============================================================================
# IMAGEN 2: Superficie de Pérdida
# ============================================================================

fig = plt.figure(figsize=(14, 6))

# 2D simple
ax1 = fig.add_subplot(121)
w = np.linspace(-5, 5, 100)
loss = (w - 1)**2 + 3  # Parábola simple

ax1.plot(w, loss, linewidth=2.5, color='#1f77b4')
ax1.axvline(x=1, color='red', linestyle='--', linewidth=2, label='Mínimo')
ax1.scatter([1], [3], s=200, c='red', zorder=5, edgecolors='black', linewidth=2)

ax1.set_xlabel('Peso (w)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Pérdida L(w)', fontsize=11, fontweight='bold')
ax1.set_title('Superficie de Pérdida (1 parámetro)', fontweight='bold', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=10)

ax1.text(1, 12, 'Objetivo: Encontrar\nel mínimo', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.7), fontsize=9)

# 3D más complejo
ax2 = fig.add_subplot(122, projection='3d')

w1 = np.linspace(-3, 3, 50)
w2 = np.linspace(-3, 3, 50)
W1, W2 = np.meshgrid(w1, w2)
Loss = (W1 - 0.5)**2 + (W2 + 0.5)**2 + 0.5 * np.sin(W1) * np.cos(W2)

surf = ax2.plot_surface(W1, W2, Loss, cmap='viridis', alpha=0.8, edgecolor='none')

ax2.set_xlabel('Peso w₁', fontsize=10, fontweight='bold')
ax2.set_ylabel('Peso w₂', fontsize=10, fontweight='bold')
ax2.set_zlabel('Pérdida', fontsize=10, fontweight='bold')
ax2.set_title('Superficie de Pérdida (2 parámetros)', fontweight='bold', fontsize=12)

# Marcar mínimo aproximado
ax2.scatter([0.5], [-0.5], [Loss.min()], s=200, c='red', zorder=5, edgecolors='black', linewidth=2)

fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)

plt.tight_layout()
plt.savefig(img_dir / '26_superficie_perdida.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 2 creada: 26_superficie_perdida.png")
plt.close()

# ============================================================================
# IMAGEN 3: Tipos de Funciones de Pérdida
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle('Tipos de Funciones de Pérdida según el Problema', fontsize=13, fontweight='bold', y=0.995)

# MSE - Regresión
ax = axes[0, 0]
y_true = 5
y_pred = np.linspace(0, 10, 100)
mse = (y_true - y_pred)**2

ax.plot(y_pred, mse, linewidth=2.5, color='#1f77b4')
ax.axvline(x=y_true, color='red', linestyle='--', linewidth=2, label='Valor real (y=5)')
ax.scatter([y_true], [0], s=200, c='red', zorder=5, edgecolors='black', linewidth=2)

ax.set_xlabel('Predicción ŷ', fontsize=10)
ax.set_ylabel('MSE: (y - ŷ)²', fontsize=10)
ax.set_title('Regresión: Mean Squared Error (MSE)', fontweight='bold', fontsize=11)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)

ax.text(5, 20, 'Penaliza fuertemente\nerrores grandes', ha='center', fontsize=8,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F4F8', alpha=0.7))

# MAE - Regresión
ax = axes[0, 1]
mae = np.abs(y_true - y_pred)

ax.plot(y_pred, mae, linewidth=2.5, color='#ff7f0e')
ax.axvline(x=y_true, color='red', linestyle='--', linewidth=2, label='Valor real (y=5)')
ax.scatter([y_true], [0], s=200, c='red', zorder=5, edgecolors='black', linewidth=2)

ax.set_xlabel('Predicción ŷ', fontsize=10)
ax.set_ylabel('MAE: |y - ŷ|', fontsize=10)
ax.set_title('Regresión: Mean Absolute Error (MAE)', fontweight='bold', fontsize=11)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)

ax.text(5, 4, 'Más robusta a\noutliers', ha='center', fontsize=8,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F4F8', alpha=0.7))

# Binary Cross Entropy
ax = axes[1, 0]
y_pred_prob = np.linspace(0.01, 0.99, 100)

# Caso y=1
bce_1 = -np.log(y_pred_prob)
# Caso y=0
bce_0 = -np.log(1 - y_pred_prob)

ax.plot(y_pred_prob, bce_1, linewidth=2.5, color='#2ca02c', label='y=1 (clase positiva)')
ax.plot(y_pred_prob, bce_0, linewidth=2.5, color='#d62728', label='y=0 (clase negativa)')

ax.set_xlabel('Predicción ŷ (probabilidad)', fontsize=10)
ax.set_ylabel('Binary Cross-Entropy', fontsize=10)
ax.set_title('Clasificación Binaria: BCE', fontweight='bold', fontsize=11)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_ylim(0, 5)

ax.text(0.5, 4.2, 'Penaliza predicciones\nconfiadas pero incorrectas', ha='center', fontsize=8,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F4F8', alpha=0.7))

# Categorical Cross Entropy (ejemplo conceptual)
ax = axes[1, 1]
ax.axis('off')
ax.set_title('Clasificación Multiclase: CCE', fontweight='bold', fontsize=11)

# Ejemplo visual
categories = ['Gato', 'Perro', 'Pájaro']
y_true = [1, 0, 0]  # Gato
y_pred1 = [0.8, 0.15, 0.05]  # Buena predicción
y_pred2 = [0.3, 0.5, 0.2]  # Mala predicción

x_pos = np.arange(len(categories))
width = 0.25

ax.bar(x_pos - width, y_true, width, label='Real', color='#2ca02c', alpha=0.7, edgecolor='black', linewidth=1.5)
ax.bar(x_pos, y_pred1, width, label='Pred. buena (Loss baja)', color='#AED6F1', alpha=0.7, edgecolor='black', linewidth=1.5)
ax.bar(x_pos + width, y_pred2, width, label='Pred. mala (Loss alta)', color='#F5B7B1', alpha=0.7, edgecolor='black', linewidth=1.5)

ax.set_ylabel('Probabilidad', fontsize=10)
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.legend(fontsize=8)
ax.set_ylim(0, 1.1)
ax.grid(axis='y', alpha=0.3)

# Calcular losses
loss1 = -np.log(0.8)
loss2 = -np.log(0.3)
ax.text(1.5, 0.95, f'CCE (buena) = {loss1:.3f}\nCCE (mala) = {loss2:.3f}', 
       fontsize=8, bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.7))

plt.tight_layout()
plt.savefig(img_dir / '27_tipos_perdida.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 3 creada: 27_tipos_perdida.png")
plt.close()

# ============================================================================
# IMAGEN 4: Pérdida vs Métricas
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 7))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Función de Pérdida vs Métricas de Evaluación', fontsize=13, fontweight='bold', pad=20)

# Función de Pérdida
rect_loss = FancyBboxPatch((1, 5.5), 4.5, 3, boxstyle='round,pad=0.1',
                          edgecolor='#d62728', facecolor='#FFE5E5', linewidth=2.5)
ax.add_patch(rect_loss)
ax.text(3.25, 8.2, 'Función de Pérdida', ha='center', fontsize=11, fontweight='bold', color='#d62728')

loss_props = [
    '✓ Debe ser diferenciable',
    '✓ Se usa para entrenar',
    '✓ Guía el aprendizaje',
    '✓ Ejemplos: MSE, BCE, CCE',
]

for i, prop in enumerate(loss_props):
    ax.text(3.25, 7.5 - i*0.4, prop, ha='center', fontsize=9)

# Métricas
rect_metrics = FancyBboxPatch((7.5, 5.5), 4.5, 3, boxstyle='round,pad=0.1',
                             edgecolor='#2ca02c', facecolor='#E5F5E5', linewidth=2.5)
ax.add_patch(rect_metrics)
ax.text(9.75, 8.2, 'Métricas de Evaluación', ha='center', fontsize=11, fontweight='bold', color='#2ca02c')

metrics_props = [
    '✓ No necesita ser diferenciable',
    '✓ Se usa para evaluar',
    '✓ Interpreta resultados',
    '✓ Ejemplos: Accuracy, F1, AUC',
]

for i, prop in enumerate(metrics_props):
    ax.text(9.75, 7.5 - i*0.4, prop, ha='center', fontsize=9)

# Diferencia clave
key_diff = (
    "DIFERENCIA CLAVE\n\n"
    "Pérdida: Optimizable matemáticamente → Entrena el modelo\n"
    "Métrica: Interpretable humanamente → Evalúa el modelo"
)

ax.text(6.5, 3, key_diff, ha='center', fontsize=10,
       bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFFCC', alpha=0.9, edgecolor='black', linewidth=2))

# Ejemplo
example = (
    "Ejemplo: Clasificación\n"
    "• Entrenar con: Binary Cross-Entropy (diferenciable)\n"
    "• Evaluar con: Accuracy, Precision, Recall (interpretables)"
)

ax.text(6.5, 1, example, ha='center', fontsize=9, style='italic',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8F4F8', alpha=0.8))

plt.tight_layout()
plt.savefig(img_dir / '28_perdida_vs_metricas.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 4 creada: 28_perdida_vs_metricas.png")
plt.close()

# ============================================================================
# IMAGEN 5: Minimizar la Pérdida - Proceso
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Proceso de Entrenamiento: Minimizar la Pérdida', fontsize=13, fontweight='bold', pad=20)

# Ciclo de entrenamiento
steps = [
    ('1. Forward Pass', 3, 7.5, '#AED6F1', 'Calcular ŷ = f(x, W)'),
    ('2. Calcular Pérdida', 7, 7.5, '#F8B88B', 'L = Loss(y, ŷ)'),
    ('3. Backpropagation', 10, 5, '#D7BDE2', 'Calcular gradientes'),
    ('4. Actualizar Pesos', 7, 2.5, '#98D8C8', 'W = W - η∇L'),
    ('5. Repetir', 3, 2.5, '#FFE5CC', 'Siguiente batch'),
]

for i, (label, x, y, color, desc) in enumerate(steps):
    rect = FancyBboxPatch((x - 1.2, y - 0.6), 2.4, 1.2, boxstyle='round,pad=0.1',
                         edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y + 0.2, label, ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(x, y - 0.2, desc, ha='center', va='center', fontsize=8, style='italic')

# Flechas del ciclo
arrows = [
    ((4.2, 7.5), (5.8, 7.5)),      # 1 -> 2
    ((8.2, 6.9), (9.2, 5.7)),       # 2 -> 3
    ((9.2, 4.3), (8.2, 3.1)),       # 3 -> 4
    ((5.8, 2.5), (4.2, 2.5)),       # 4 -> 5
    ((2.3, 3.1), (2.3, 6.9)),       # 5 -> 1
]

for (x1, y1), (x2, y2) in arrows:
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25, linewidth=2.5, color='#d62728')
    ax.add_patch(arrow)

# Objetivo
objective = (
    "OBJETIVO ÚNICO\n\n"
    "Encontrar los parámetros W que minimizan L(W)\n\n"
    "min L(W) = min (1/N) Σ Loss(y_i, f(x_i, W))"
)

ax.text(6.5, 9, objective, ha='center', fontsize=10, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFFCC', alpha=0.9, edgecolor='black', linewidth=2))

plt.tight_layout()
plt.savefig(img_dir / '29_minimizar_perdida.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 5 creada: 29_minimizar_perdida.png")
plt.close()

print("\n" + "="*60)
print("✅ TODAS LAS IMÁGENES DEL CAPÍTULO 5 GENERADAS")
print("="*60)
print("\nImágenes disponibles:")
print("  1. 25_concepto_perdida.png")
print("  2. 26_superficie_perdida.png")
print("  3. 27_tipos_perdida.png")
print("  4. 28_perdida_vs_metricas.png")
print("  5. 29_minimizar_perdida.png")
