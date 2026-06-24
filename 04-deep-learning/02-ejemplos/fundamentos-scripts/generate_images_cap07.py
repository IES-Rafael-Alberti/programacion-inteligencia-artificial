"""
Script para generar imágenes ilustrativas del Capítulo 7
Gradiente descendente
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D

img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

# ============================================================================
# IMAGEN 1: Algoritmo Gradiente Descendente
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Algoritmo de Gradiente Descendente', fontsize=13, fontweight='bold', pad=20)

# Pasos del algoritmo
steps = [
    ('1. Inicializar\npesos', 2, 8, '#AED6F1'),
    ('2. Forward Pass\nCalcular ŷ', 2, 6, '#AED6F1'),
    ('3. Calcular\nPérdida L', 2, 4, '#AED6F1'),
    ('4. Calcular\nGradiente ∇L', 6.5, 8, '#F8B88B'),
    ('5. Actualizar\nPesos', 6.5, 6, '#F8B88B'),
    ('6. ¿Convergió?', 6.5, 4, '#D7BDE2'),
]

for label, x, y, color in steps:
    rect = FancyBboxPatch((x - 1.2, y - 0.6), 2.4, 1.2, boxstyle='round,pad=0.1',
                         edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold')

# Flechas
arrows = [
    ((2, 7.4), (2, 6.6)),      # 1 -> 2
    ((2, 5.4), (2, 4.6)),      # 2 -> 3
    ((3.2, 3.7), (5.3, 7.5)),  # 3 -> 4
    ((6.5, 7.4), (6.5, 6.6)),  # 4 -> 5
    ((6.5, 5.4), (6.5, 4.6)),  # 5 -> 6
]

for (x1, y1), (x2, y2) in arrows:
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25, linewidth=2, color='black')
    ax.add_patch(arrow)

# Bifurcación (Sí / No)
arrow_no = FancyArrowPatch((5.3, 4), (4, 3),
                          arrowstyle='->', mutation_scale=20, linewidth=2, color='#d62728')
ax.add_patch(arrow_no)
ax.text(4.6, 3.5, 'No', fontsize=9, color='#d62728', fontweight='bold')

# Flecha "Sí" hacia el final
arrow_si = FancyArrowPatch((6.5, 3.4), (6.5, 2.4),
                          arrowstyle='->', mutation_scale=25, linewidth=2, color='#2ca02c')
ax.add_patch(arrow_si)
ax.text(7, 2.9, 'Sí', fontsize=9, color='#2ca02c', fontweight='bold')

# Ciclo
cycle_arrow = FancyArrowPatch((4, 3), (2, 5.4),
                             arrowstyle='->', mutation_scale=20, linewidth=2.5,
                             color='#d62728', connectionstyle='arc3,rad=0.5')
ax.add_patch(cycle_arrow)

# Fin
rect_end = FancyBboxPatch((6.5 - 1.2, 1.2 - 0.6), 2.4, 1.2, boxstyle='round,pad=0.1',
                         edgecolor='black', facecolor='#98D8C8', linewidth=2)
ax.add_patch(rect_end)
ax.text(6.5, 1.2, 'Fin:\nModelo entrenado', ha='center', va='center', fontsize=9, fontweight='bold')

# Fórmula
formula_box = (
    "Fórmula de actualización:\n\n"
    "w_nuevo = w - α × ∇L(w)\n\n"
    "donde:\n"
    "α = learning rate\n"
    "∇L = gradiente de la pérdida"
)

ax.text(10, 5.5, formula_box, fontsize=9, family='monospace',
       bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFFCC', alpha=0.8, edgecolor='black', linewidth=2))

plt.tight_layout()
plt.savefig(img_dir / '35_algoritmo_gradiente_descendente.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 1 creada: 35_algoritmo_gradiente_descendente.png")
plt.close()

# ============================================================================
# IMAGEN 2: Visualización del Descenso
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 8))

# Superficie de pérdida
w = np.linspace(-3, 3, 300)
loss = (w - 0.5)**2 + 1.5 * np.exp(-0.5 * (w - 0.5)**2) * np.sin(3 * w) + 0.2

ax.plot(w, loss, linewidth=3, color='#1f77b4', label='Función de Pérdida')

# Simulación de pasos de gradiente descendente
learning_rates = [0.15]  # Learning rate
w_positions = [2.2]
loss_positions = [(2.2 - 0.5)**2 + 1.5 * np.exp(-0.5 * (2.2 - 0.5)**2) * np.sin(3 * 2.2) + 0.2]

# Calcular pasos
for step in range(15):
    w_current = w_positions[-1]
    grad = 2 * (w_current - 0.5) + 1.5 * (
        -np.exp(-0.5 * (w_current - 0.5)**2) * np.sin(3 * w_current) * (w_current - 0.5) +
        3 * np.exp(-0.5 * (w_current - 0.5)**2) * np.cos(3 * w_current)
    )
    
    w_new = w_current - learning_rates[0] * grad
    w_new = np.clip(w_new, -3, 3)
    
    loss_new = (w_new - 0.5)**2 + 1.5 * np.exp(-0.5 * (w_new - 0.5)**2) * np.sin(3 * w_new) + 0.2
    
    w_positions.append(w_new)
    loss_positions.append(loss_new)

# Graficar la trayectoria
ax.plot(w_positions, loss_positions, 'o-', markersize=6, linewidth=2, color='#d62728', alpha=0.7, label='Trayectoria del aprendizaje')

# Puntos destacados
ax.scatter([w_positions[0]], [loss_positions[0]], s=300, c='orange', zorder=5, 
          edgecolors='black', linewidth=2.5, label='Inicio')
ax.scatter([w_positions[-1]], [loss_positions[-1]], s=300, c='green', zorder=5,
          edgecolors='black', linewidth=2.5, label='Final')

# Anotaciones
ax.annotate(f'Paso 0\nw={w_positions[0]:.2f}', xy=(w_positions[0], loss_positions[0]), 
           xytext=(w_positions[0] + 0.3, loss_positions[0] + 0.5),
           fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5CC', alpha=0.8),
           arrowprops=dict(arrowstyle='->', lw=1.5))

ax.annotate(f'Paso {len(w_positions)-1}\nw={w_positions[-1]:.2f}', xy=(w_positions[-1], loss_positions[-1]),
           xytext=(w_positions[-1] - 0.5, loss_positions[-1] + 0.5),
           fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='#E5F5E5', alpha=0.8),
           arrowprops=dict(arrowstyle='->', lw=1.5))

ax.set_xlabel('Peso (w)', fontsize=11, fontweight='bold')
ax.set_ylabel('Pérdida L(w)', fontsize=11, fontweight='bold')
ax.set_title('Gradiente Descendente: Descenso Iterativo hacia el Mínimo', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10, loc='upper right')
ax.set_xlim(-3, 3)

plt.tight_layout()
plt.savefig(img_dir / '36_visualizacion_descenso.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 2 creada: 36_visualizacion_descenso.png")
plt.close()

# ============================================================================
# IMAGEN 3: Tipos de Gradiente Descendente
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Tipos de Gradiente Descendente según Tamaño de Batch', fontsize=13, fontweight='bold')

# Datos
w = np.linspace(-3, 3, 200)
loss = (w - 0.5)**2 + 0.2

# BGD - Batch
ax = axes[0]
ax.plot(w, loss, linewidth=2.5, color='#1f77b4')

# Trayectoria BGD
w_bgd = [2.0, 1.75, 1.55, 1.39, 1.26, 1.15, 1.06, 0.99]
loss_bgd = [(wi - 0.5)**2 + 0.2 for wi in w_bgd]

ax.plot(w_bgd, loss_bgd, 'o-', markersize=8, linewidth=2.5, color='#2ca02c', label='BGD (suave)')
ax.scatter([w_bgd[0]], [loss_bgd[0]], s=250, c='orange', zorder=5, edgecolors='black', linewidth=2)
ax.scatter([w_bgd[-1]], [loss_bgd[-1]], s=250, c='green', zorder=5, edgecolors='black', linewidth=2)

ax.set_xlabel('Peso (w)', fontsize=10)
ax.set_ylabel('Pérdida L', fontsize=10)
ax.set_title('Batch GD\nTodo el dataset\nSuave, preciso, lento', fontsize=11, fontweight='bold', color='#2ca02c')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)

# SGD - Stochastic
ax = axes[1]
ax.plot(w, loss, linewidth=2.5, color='#1f77b4')

# Trayectoria SGD (ruidosa)
np.random.seed(42)
w_sgd = [2.0]
for _ in range(20):
    w_curr = w_sgd[-1]
    grad = 2 * (w_curr - 0.5)
    w_new = w_curr - 0.15 * grad + np.random.normal(0, 0.1)
    w_sgd.append(np.clip(w_new, -3, 3))

loss_sgd = [(wi - 0.5)**2 + 0.2 for wi in w_sgd]

ax.plot(w_sgd, loss_sgd, 'o-', markersize=6, linewidth=1.5, color='#ff7f0e', alpha=0.7, label='SGD (ruidoso)')
ax.scatter([w_sgd[0]], [loss_sgd[0]], s=250, c='orange', zorder=5, edgecolors='black', linewidth=2)
ax.scatter([w_sgd[-1]], [loss_sgd[-1]], s=250, c='green', zorder=5, edgecolors='black', linewidth=2)

ax.set_xlabel('Peso (w)', fontsize=10)
ax.set_ylabel('Pérdida L', fontsize=10)
ax.set_title('SGD\nUn ejemplo por paso\nRápido, ruidoso, puede escapar', fontsize=11, fontweight='bold', color='#ff7f0e')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)

# Mini-batch
ax = axes[2]
ax.plot(w, loss, linewidth=2.5, color='#1f77b4')

# Trayectoria Mini-batch (intermedio)
np.random.seed(42)
w_mini = [2.0]
for _ in range(15):
    w_curr = w_mini[-1]
    grad = 2 * (w_curr - 0.5)
    w_new = w_curr - 0.15 * grad + np.random.normal(0, 0.05)
    w_mini.append(np.clip(w_new, -3, 3))

loss_mini = [(wi - 0.5)**2 + 0.2 for wi in w_mini]

ax.plot(w_mini, loss_mini, 'o-', markersize=7, linewidth=2, color='#d62728', label='Mini-batch (equilibrio)')
ax.scatter([w_mini[0]], [loss_mini[0]], s=250, c='orange', zorder=5, edgecolors='black', linewidth=2)
ax.scatter([w_mini[-1]], [loss_mini[-1]], s=250, c='green', zorder=5, edgecolors='black', linewidth=2)

ax.set_xlabel('Peso (w)', fontsize=10)
ax.set_ylabel('Pérdida L', fontsize=10)
ax.set_title('Mini-batch GD\nPequeños lotes\nEquilibrado, usado en práctica', fontsize=11, fontweight='bold', color='#d62728')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)

plt.tight_layout()
plt.savefig(img_dir / '37_tipos_gradiente_descendente.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 3 creada: 37_tipos_gradiente_descendente.png")
plt.close()

# ============================================================================
# IMAGEN 4: Learning Rate - Efecto
# ============================================================================

fig = plt.figure(figsize=(14, 6))

# 3D con múltiples trayectorias
ax = fig.add_subplot(121, projection='3d')

# Superficie
w1 = np.linspace(-2.5, 2.5, 60)
w2 = np.linspace(-2.5, 2.5, 60)
W1, W2 = np.meshgrid(w1, w2)
Loss = (W1 - 0.4)**2 + (W2 + 0.3)**2 + 0.3 * np.sin(W1) * np.cos(W2)

surf = ax.plot_surface(W1, W2, Loss, cmap='viridis', alpha=0.6, edgecolor='none')

# Trayectorias con diferentes learning rates
np.random.seed(42)

# Learning rate grande
w1_init, w2_init = 2.0, 2.0
w1_traj_big, w2_traj_big = [w1_init], [w2_init]
for _ in range(5):
    grad1 = 2 * (w1_traj_big[-1] - 0.4) + 0.3 * np.cos(w1_traj_big[-1]) * np.cos(w2_traj_big[-1])
    grad2 = 2 * (w2_traj_big[-1] + 0.3) - 0.3 * np.sin(w1_traj_big[-1]) * np.sin(w2_traj_big[-1])
    w1_new = w1_traj_big[-1] - 0.4 * grad1
    w2_new = w2_traj_big[-1] - 0.4 * grad2
    w1_traj_big.append(np.clip(w1_new, -2.5, 2.5))
    w2_traj_big.append(np.clip(w2_new, -2.5, 2.5))

loss_traj_big = [(w1_traj_big[i] - 0.4)**2 + (w2_traj_big[i] + 0.3)**2 + 
                  0.3 * np.sin(w1_traj_big[i]) * np.cos(w2_traj_big[i]) for i in range(len(w1_traj_big))]

ax.plot(w1_traj_big, w2_traj_big, loss_traj_big, 'ro-', linewidth=2.5, markersize=6, label='LR grande (0.4)')

# Learning rate pequeño
w1_traj_small, w2_traj_small = [w1_init], [w2_init]
for _ in range(15):
    grad1 = 2 * (w1_traj_small[-1] - 0.4) + 0.3 * np.cos(w1_traj_small[-1]) * np.cos(w2_traj_small[-1])
    grad2 = 2 * (w2_traj_small[-1] + 0.3) - 0.3 * np.sin(w1_traj_small[-1]) * np.sin(w2_traj_small[-1])
    w1_new = w1_traj_small[-1] - 0.1 * grad1
    w2_new = w2_traj_small[-1] - 0.1 * grad2
    w1_traj_small.append(np.clip(w1_new, -2.5, 2.5))
    w2_traj_small.append(np.clip(w2_new, -2.5, 2.5))

loss_traj_small = [(w1_traj_small[i] - 0.4)**2 + (w2_traj_small[i] + 0.3)**2 + 
                    0.3 * np.sin(w1_traj_small[i]) * np.cos(w2_traj_small[i]) for i in range(len(w1_traj_small))]

ax.plot(w1_traj_small, w2_traj_small, loss_traj_small, 'go-', linewidth=2.5, markersize=5, label='LR pequeño (0.1)')

ax.set_xlabel('w₁', fontsize=10)
ax.set_ylabel('w₂', fontsize=10)
ax.set_zlabel('Pérdida', fontsize=10)
ax.set_title('Superficie 3D\nTrayectorias con diferente Learning Rate', fontsize=11, fontweight='bold')
ax.legend(fontsize=9)

# Gráfico 2D de convergencia
ax2 = fig.add_subplot(122)

# Pérdida vs iteraciones para ambos LR
loss_big_iter = [Loss[int((w2_traj_big[i] + 2.5) / 5 * 60), int((w1_traj_big[i] + 2.5) / 5 * 60)] for i in range(len(w1_traj_big))]
loss_small_iter = [Loss[min(int((w2_traj_small[i] + 2.5) / 5 * 60), 59), min(int((w1_traj_small[i] + 2.5) / 5 * 60), 59)] for i in range(len(w1_traj_small))]

ax2.plot(range(len(loss_big_iter)), loss_big_iter, 'o-', linewidth=2.5, markersize=8, 
        color='#ff7f0e', label='LR grande: Converge rápido pero inestable')
ax2.plot(range(len(loss_small_iter)), loss_small_iter, 's-', linewidth=2.5, markersize=6,
        color='#2ca02c', label='LR pequeño: Converge lentamente pero suave')

ax2.set_xlabel('Iteración', fontsize=11, fontweight='bold')
ax2.set_ylabel('Pérdida', fontsize=11, fontweight='bold')
ax2.set_title('Pérdida vs Iteraciones', fontsize=11, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=9)

plt.tight_layout()
plt.savefig(img_dir / '38_learning_rate_efecto.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 4 creada: 38_learning_rate_efecto.png")
plt.close()

# ============================================================================
# IMAGEN 5: Mínimos Locales vs Globales
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('El Paisaje de Pérdida: Mínimos Locales vs Globales', fontsize=13, fontweight='bold')

# Gráfico 1D
ax = axes[0]

w = np.linspace(-5, 5, 300)
# Función con múltiples mínimos
loss = 0.5 * (w + 2)**2 * np.sin(0.5 * w)**2 + 0.3 * np.exp(-0.5 * (w + 2)**2) + \
        (w - 1)**2 - 0.8 * np.sin(w + 1)**2 + 0.5

ax.plot(w, loss, linewidth=3, color='#1f77b4', label='Función de Pérdida')

# Mínimos locales
minimos_locales = [-3.2, -0.5, 0.8]
for mini in minimos_locales:
    idx = np.argmin(np.abs(w - mini))
    ax.scatter([w[idx]], [loss[idx]], s=200, c='orange', zorder=4, edgecolors='black', linewidth=2)
    ax.text(w[idx], loss[idx] - 1, 'Mínimo\nlocal', ha='center', fontsize=9, 
           bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFE5CC', alpha=0.7))

# Mínimo global
global_mini = 2.8
idx_global = np.argmin(np.abs(w - global_mini))
ax.scatter([w[idx_global]], [loss[idx_global]], s=300, c='#2ca02c', zorder=5, edgecolors='black', linewidth=2.5)
ax.text(w[idx_global], loss[idx_global] - 1.8, 'Mínimo\nGLOBAL', ha='center', fontsize=10, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.2', facecolor='#E5F5E5', alpha=0.8))

# Trayectoria posible (quedarse atrapado)
w_traj_trapped = [4.5, 3.8, 3.2, 2.7, 2.5, 2.4, 2.35]
loss_traj_trapped = [loss[np.argmin(np.abs(w - wi))] for wi in w_traj_trapped]
ax.plot(w_traj_trapped, loss_traj_trapped, 'r*-', markersize=10, linewidth=2, label='Posible trayectoria')

ax.set_xlabel('Peso (w)', fontsize=11, fontweight='bold')
ax.set_ylabel('Pérdida L(w)', fontsize=11, fontweight='bold')
ax.set_title('1D: Múltiples Mínimos', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10)
ax.set_xlim(-5, 5)

# Gráfico 3D
ax = axes[1]
ax = fig.add_subplot(122, projection='3d')

w1 = np.linspace(-2, 2, 50)
w2 = np.linspace(-2, 2, 50)
W1, W2 = np.meshgrid(w1, w2)
Loss = (W1)**2 + (W2)**2 + 2*np.sin(W1*1.5) + 2*np.sin(W2*1.5)

surf = ax.plot_surface(W1, W2, Loss, cmap='viridis', alpha=0.7, edgecolor='none')

# Marcar mínimo global
ax.scatter([0], [0], [Loss[25, 25]], s=300, c='#2ca02c', edgecolors='black', linewidth=2.5, zorder=5)

# Otros mínimos locales
ax.scatter([-1.2], [-1.2], [Loss[10, 10] + 0.5], s=200, c='orange', edgecolors='black', linewidth=2, zorder=4)
ax.scatter([1.2], [1.2], [Loss[40, 40] + 0.3], s=200, c='orange', edgecolors='black', linewidth=2, zorder=4)

ax.set_xlabel('w₁', fontsize=10)
ax.set_ylabel('w₂', fontsize=10)
ax.set_zlabel('Pérdida', fontsize=10)
ax.set_title('2D: Paisaje Complejo\ncon Múltiples Valles', fontsize=12, fontweight='bold')

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Anotación clave
key_text = (
    "En redes neuronales modernas:\n"
    "• Las superficies son muy complejas\n"
    "• Hay muchos mínimos locales\n"
    "• El gradiente descendente NO garantiza global\n"
    "• Pero encuentra soluciones \"buenas\"\n"
    "• En la práctica, esto suele bastar"
)

fig.text(0.5, -0.05, key_text, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFFCC', alpha=0.8, edgecolor='black', linewidth=2))

plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.savefig(img_dir / '39_minimos_locales_globales.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 5 creada: 39_minimos_locales_globales.png")
plt.close()

print("\n" + "="*60)
print("✅ TODAS LAS IMÁGENES DEL CAPÍTULO 7 GENERADAS")
print("="*60)
print("\nImágenes disponibles:")
print("  1. 35_algoritmo_gradiente_descendente.png")
print("  2. 36_visualizacion_descenso.png")
print("  3. 37_tipos_gradiente_descendente.png")
print("  4. 38_learning_rate_efecto.png")
print("  5. 39_minimos_locales_globales.png")
