"""
Script para generar imágenes ilustrativas del Capítulo 6
Derivadas y gradientes
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
# IMAGEN 1: Concepto de Derivada - Pendiente
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(14, 5))
fig.suptitle('Derivada: La Idea de Pendiente', fontsize=13, fontweight='bold')

# Cuesta arriba (derivada positiva)
ax = axes[0]
x = np.linspace(0, 10, 100)
y = 0.3 * x + 1

ax.plot(x, y, linewidth=3, color='#2ca02c')
ax.scatter([5], [2.5], s=200, c='red', zorder=5, edgecolors='black', linewidth=2)

# Triángulo de pendiente
dx, dy = 2, 0.6
ax.plot([5, 5+dx], [2.5, 2.5], 'k--', linewidth=1.5)
ax.plot([5+dx, 5+dx], [2.5, 2.5+dy], 'k--', linewidth=1.5)
ax.text(6.2, 2.35, f'dy/dx = {dy/dx:.2f}', fontsize=10, fontweight='bold')

ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_xlabel('x', fontsize=10)
ax.set_ylabel('f(x)', fontsize=10)
ax.set_title('Derivada > 0\nSubida', fontsize=11, fontweight='bold', color='#2ca02c')
ax.grid(True, alpha=0.3)

# Horizontal (derivada cero)
ax = axes[1]
x = np.linspace(0, 10, 100)
y = np.ones_like(x) * 2.5

ax.plot(x, y, linewidth=3, color='#ff7f0e')
ax.scatter([5], [2.5], s=200, c='red', zorder=5, edgecolors='black', linewidth=2)
ax.text(5, 3.2, 'dy/dx = 0', ha='center', fontsize=10, fontweight='bold')

ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_xlabel('x', fontsize=10)
ax.set_ylabel('f(x)', fontsize=10)
ax.set_title('Derivada = 0\nLlano', fontsize=11, fontweight='bold', color='#ff7f0e')
ax.grid(True, alpha=0.3)

# Cuesta abajo (derivada negativa)
ax = axes[2]
x = np.linspace(0, 10, 100)
y = -0.3 * x + 4

ax.plot(x, y, linewidth=3, color='#d62728')
ax.scatter([5], [2.5], s=200, c='red', zorder=5, edgecolors='black', linewidth=2)

# Triángulo de pendiente
dx, dy = 2, -0.6
ax.plot([5, 5+dx], [2.5, 2.5], 'k--', linewidth=1.5)
ax.plot([5+dx, 5+dx], [2.5, 2.5+dy], 'k--', linewidth=1.5)
ax.text(6.2, 2.65, f'dy/dx = {dy/dx:.2f}', fontsize=10, fontweight='bold')

ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_xlabel('x', fontsize=10)
ax.set_ylabel('f(x)', fontsize=10)
ax.set_title('Derivada < 0\nBajada', fontsize=11, fontweight='bold', color='#d62728')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(img_dir / '30_derivada_pendiente.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 1 creada: 30_derivada_pendiente.png")
plt.close()

# ============================================================================
# IMAGEN 2: Derivada aplicada a Pérdida
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 7))

# Superficie de pérdida (1D)
w = np.linspace(-3, 3, 200)
loss = (w - 0.5)**2 + 0.5

ax.plot(w, loss, linewidth=3.5, color='#1f77b4', label='Función de Pérdida L(w)')

# Punto actual
w_actual = 1.5
loss_actual = (w_actual - 0.5)**2 + 0.5

ax.scatter([w_actual], [loss_actual], s=300, c='#ff7f0e', zorder=5, 
          edgecolors='black', linewidth=2.5, label='Peso actual')

# Derivada en ese punto (tangente)
# dL/dw = 2(w - 0.5) = 2(1.5 - 0.5) = 2
derivada = 2 * (w_actual - 0.5)
w_tangent = np.array([w_actual - 0.5, w_actual + 0.5])
loss_tangent = loss_actual + derivada * (w_tangent - w_actual)

ax.plot(w_tangent, loss_tangent, 'r--', linewidth=2.5, label=f'Tangente (pendiente = {derivada:.2f})')

# Anotaciones
ax.annotate('', xy=(w_actual + 0.3, loss_actual + derivada * 0.3), 
           xytext=(w_actual, loss_actual),
           arrowprops=dict(arrowstyle='->', lw=3, color='red'))

ax.text(w_actual + 0.5, loss_actual + 1.2, 
       'dL/dw: Si cambio\nel peso, cómo\ncambia la pérdida',
       fontsize=10, bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFFFCC', alpha=0.8))

# Líneas de ayuda
ax.axvline(x=w_actual, color='gray', linestyle=':', alpha=0.5)
ax.axhline(y=loss_actual, color='gray', linestyle=':', alpha=0.5)

ax.set_xlabel('Peso (w)', fontsize=11, fontweight='bold')
ax.set_ylabel('Pérdida L(w)', fontsize=11, fontweight='bold')
ax.set_title('Derivada aplicada a la Función de Pérdida', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10, loc='upper left')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)

plt.tight_layout()
plt.savefig(img_dir / '31_derivada_perdida.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 2 creada: 31_derivada_perdida.png")
plt.close()

# ============================================================================
# IMAGEN 3: Gradiente en muchas dimensiones
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('De Derivada a Gradiente: Múltiples Parámetros', fontsize=13, fontweight='bold')

# 1D - Derivada
ax = axes[0]
ax.text(0.5, 0.9, '1 Peso: Derivada', ha='center', fontsize=12, fontweight='bold', 
       transform=ax.transAxes)

# Una línea vertical con flechas
ax.arrow(0.5, 0.75, 0, -0.15, head_width=0.05, head_length=0.03, 
        fc='red', ec='red', transform=ax.transAxes, linewidth=2)

ax.text(0.5, 0.5, 'dL/dw', ha='center', fontsize=14, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFE5E5', alpha=0.8),
       transform=ax.transAxes)

ax.text(0.5, 0.3, 'Un número que indica\ncómo cambia L respecto a w', 
       ha='center', fontsize=10, style='italic', transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# 2D+ - Gradiente
ax = axes[1]
ax.text(0.5, 0.9, 'Muchos Pesos: Gradiente', ha='center', fontsize=12, fontweight='bold',
       transform=ax.transAxes)

# Vectores de gradiente
ax.arrow(0.5, 0.7, 0.15, -0.1, head_width=0.04, head_length=0.03,
        fc='red', ec='red', transform=ax.transAxes, linewidth=2)
ax.arrow(0.5, 0.7, -0.1, -0.15, head_width=0.04, head_length=0.03,
        fc='red', ec='red', transform=ax.transAxes, linewidth=2)

ax.text(0.5, 0.5, '∇L = (dL/dw₁, dL/dw₂, ..., dL/dwₙ)', ha='center', fontsize=11, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFE5E5', alpha=0.8),
       transform=ax.transAxes, family='monospace')

ax.text(0.5, 0.28, 'Un vector con n componentes\n(una derivada por cada parámetro)', 
       ha='center', fontsize=10, style='italic', transform=ax.transAxes)

ax.text(0.5, 0.1, 'Apunta hacia donde\ncrece más rápido la pérdida', 
       ha='center', fontsize=9, fontweight='bold', color='red', transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()
plt.savefig(img_dir / '32_gradiente_multidimensional.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 3 creada: 32_gradiente_multidimensional.png")
plt.close()

# ============================================================================
# IMAGEN 4: Interpretación geométrica del Gradiente
# ============================================================================

fig = plt.figure(figsize=(14, 6))

# Contorno 2D con vector gradiente
ax1 = fig.add_subplot(121)

# Crear la superficie de pérdida
w1 = np.linspace(-2, 2, 100)
w2 = np.linspace(-2, 2, 100)
W1, W2 = np.meshgrid(w1, w2)
Loss = (W1 - 0.3)**2 + (W2 + 0.2)**2 + 0.2 * np.sin(2*W1) * np.cos(2*W2)

# Contorno
contour = ax1.contour(W1, W2, Loss, levels=15, cmap='viridis', alpha=0.6)
ax1.clabel(contour, inline=True, fontsize=8)

# Punto actual
w1_act, w2_act = 1.2, 0.8
ax1.scatter([w1_act], [w2_act], s=300, c='red', zorder=5, edgecolors='black', linewidth=2.5, label='Posición actual')

# Gradiente (vector hacia arriba del contorno)
grad_w1 = 2 * (w1_act - 0.3) + 0.4 * np.cos(2*w1_act) * np.cos(2*w2_act)
grad_w2 = 2 * (w2_act + 0.2) - 0.4 * np.sin(2*w1_act) * np.sin(2*w2_act)

# Normalizar para visualización
grad_norm = np.sqrt(grad_w1**2 + grad_w2**2)
grad_w1_norm = grad_w1 / grad_norm * 0.3
grad_w2_norm = grad_w2 / grad_norm * 0.3

# Flecha del gradiente
ax1.arrow(w1_act, w2_act, grad_w1_norm, grad_w2_norm, 
         head_width=0.15, head_length=0.1, fc='red', ec='red', linewidth=2.5,
         label='Gradiente ∇L')

# Flecha contraria (descenso)
ax1.arrow(w1_act, w2_act, -grad_w1_norm*0.8, -grad_w2_norm*0.8,
         head_width=0.12, head_length=0.08, fc='green', ec='green', linewidth=2, 
         linestyle='--', label='Descenso (-∇L)')

ax1.set_xlabel('w₁', fontsize=11, fontweight='bold')
ax1.set_ylabel('w₂', fontsize=11, fontweight='bold')
ax1.set_title('Contorno de Pérdida\n2D', fontsize=12, fontweight='bold')
ax1.legend(fontsize=10)
ax1.set_aspect('equal')

# 3D con gradiente
ax2 = fig.add_subplot(122, projection='3d')

surf = ax2.plot_surface(W1, W2, Loss, cmap='viridis', alpha=0.7, edgecolor='none')

# Punto actual
loss_act = Loss[int((w2_act + 2) / 4 * 100), int((w1_act + 2) / 4 * 100)]
ax2.scatter([w1_act], [w2_act], [loss_act], s=300, c='red', edgecolors='black', linewidth=2, zorder=5)

# Línea de ascenso (gradiente)
scale = 0.3
w1_grad = w1_act + grad_w1_norm
w2_grad = w2_act + grad_w2_norm
loss_grad_idx = min(int((w2_grad + 2) / 4 * 100), 99)
loss_grad_idx = max(loss_grad_idx, 0)
loss_grad_idx2 = min(int((w1_grad + 2) / 4 * 100), 99)
loss_grad_idx2 = max(loss_grad_idx2, 0)
loss_grad = Loss[loss_grad_idx, loss_grad_idx2]

ax2.plot([w1_act, w1_grad], [w2_act, w2_grad], [loss_act, loss_grad], 
        'r-', linewidth=3, label='Dirección de mayor crecimiento')

ax2.set_xlabel('w₁', fontsize=10)
ax2.set_ylabel('w₂', fontsize=10)
ax2.set_zlabel('Pérdida L', fontsize=10)
ax2.set_title('Superficie 3D\ncon Gradiente', fontsize=12, fontweight='bold')

fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)

plt.tight_layout()
plt.savefig(img_dir / '33_interpretacion_geometrica_gradiente.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 4 creada: 33_interpretacion_geometrica_gradiente.png")
plt.close()

# ============================================================================
# IMAGEN 5: Gradiente y Learning Rate
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Gradiente + Learning Rate = Actualización de Pesos', fontsize=13, fontweight='bold')

# Superficie base para todos
w = np.linspace(-3, 3, 200)
loss = (w - 0.5)**2 + 0.5

# Punto inicial
w_init = 2.2
loss_init = (w_init - 0.5)**2 + 0.5
grad = 2 * (w_init - 0.5)  # derivada

# Learning rate grande
ax = axes[0]
ax.plot(w, loss, linewidth=2.5, color='#1f77b4')
ax.scatter([w_init], [loss_init], s=250, c='#ff7f0e', edgecolors='black', linewidth=2, zorder=5, label='Inicio')

lr = 0.4
w_new = w_init - lr * grad
loss_new = (w_new - 0.5)**2 + 0.5

ax.scatter([w_new], [loss_new], s=250, c='#2ca02c', edgecolors='black', linewidth=2, zorder=5, label='Después 1 paso')
ax.arrow(w_init, loss_init, w_new - w_init, loss_new - loss_init,
        head_width=0.15, head_length=0.2, fc='red', ec='red', linewidth=2, alpha=0.7)

ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)
ax.set_xlabel('Peso (w)', fontsize=10)
ax.set_ylabel('Pérdida L', fontsize=10)
ax.set_title('Learning Rate = 0.4 (Grande)\nPasos largos', fontsize=11, fontweight='bold', color='#d62728')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)

# Learning rate normal
ax = axes[1]
ax.plot(w, loss, linewidth=2.5, color='#1f77b4')
ax.scatter([w_init], [loss_init], s=250, c='#ff7f0e', edgecolors='black', linewidth=2, zorder=5, label='Inicio')

lr = 0.1
w_new = w_init - lr * grad
loss_new = (w_new - 0.5)**2 + 0.5

ax.scatter([w_new], [loss_new], s=250, c='#2ca02c', edgecolors='black', linewidth=2, zorder=5, label='Después 1 paso')
ax.arrow(w_init, loss_init, w_new - w_init, loss_new - loss_init,
        head_width=0.15, head_length=0.15, fc='red', ec='red', linewidth=2, alpha=0.7)

ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)
ax.set_xlabel('Peso (w)', fontsize=10)
ax.set_ylabel('Pérdida L', fontsize=10)
ax.set_title('Learning Rate = 0.1 (Normal)\nPasos equilibrados', fontsize=11, fontweight='bold', color='#2ca02c')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)

# Learning rate pequeño
ax = axes[2]
ax.plot(w, loss, linewidth=2.5, color='#1f77b4')
ax.scatter([w_init], [loss_init], s=250, c='#ff7f0e', edgecolors='black', linewidth=2, zorder=5, label='Inicio')

lr = 0.02
w_new = w_init - lr * grad
loss_new = (w_new - 0.5)**2 + 0.5

ax.scatter([w_new], [loss_new], s=250, c='#2ca02c', edgecolors='black', linewidth=2, zorder=5, label='Después 1 paso')
ax.arrow(w_init, loss_init, w_new - w_init, loss_new - loss_init,
        head_width=0.15, head_length=0.05, fc='red', ec='red', linewidth=2, alpha=0.7)

ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)
ax.set_xlabel('Peso (w)', fontsize=10)
ax.set_ylabel('Pérdida L', fontsize=10)
ax.set_title('Learning Rate = 0.02 (Pequeño)\nPasos cortos y lentos', fontsize=11, fontweight='bold', color='#ff7f0e')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig(img_dir / '34_gradiente_learning_rate.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 5 creada: 34_gradiente_learning_rate.png")
plt.close()

print("\n" + "="*60)
print("✅ TODAS LAS IMÁGENES DEL CAPÍTULO 6 GENERADAS")
print("="*60)
print("\nImágenes disponibles:")
print("  1. 30_derivada_pendiente.png")
print("  2. 31_derivada_perdida.png")
print("  3. 32_gradiente_multidimensional.png")
print("  4. 33_interpretacion_geometrica_gradiente.png")
print("  5. 34_gradiente_learning_rate.png")
