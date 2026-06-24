"""
Script para generar imágenes ilustrativas del Capítulo 8
Backpropagation
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

# ============================================================================
# IMAGEN 1: Backpropagation - visión general
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 6))
ax.set_xlim(0, 13)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('Backpropagation: Gradientes de salida a entrada', fontsize=13, fontweight='bold', pad=20)

# Capas
layers = [
    ('Entrada', 1.2),
    ('Capa 1', 3.7),
    ('Capa 2', 6.2),
    ('Capa 3', 8.7),
    ('Salida', 11.2),
]

for name, x in layers:
    rect = FancyBboxPatch((x-0.9, 2.2), 1.8, 1.6, boxstyle='round,pad=0.1',
                          edgecolor='black', facecolor='#AED6F1', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, 3, name, ha='center', va='center', fontsize=10, fontweight='bold')

# Flechas forward
for i in range(len(layers)-1):
    x1 = layers[i][1] + 0.9
    x2 = layers[i+1][1] - 0.9
    arrow = FancyArrowPatch((x1, 3), (x2, 3), arrowstyle='->', mutation_scale=20, linewidth=2.5, color='#2ca02c')
    ax.add_patch(arrow)

ax.text(6.5, 4.6, 'Forward pass (predicción)', ha='center', fontsize=10, color='#2ca02c', fontweight='bold')

# Flechas backward
for i in range(len(layers)-1, 0, -1):
    x1 = layers[i][1] - 0.9
    x2 = layers[i-1][1] + 0.9
    arrow = FancyArrowPatch((x1, 2.1), (x2, 2.1), arrowstyle='->', mutation_scale=20, linewidth=2.5, color='#d62728')
    ax.add_patch(arrow)

ax.text(6.5, 1.2, 'Backward pass (gradientes)', ha='center', fontsize=10, color='#d62728', fontweight='bold')

plt.tight_layout()
plt.savefig(img_dir / '40_backprop_overview.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 1 creada: 40_backprop_overview.png")
plt.close()

# ============================================================================
# IMAGEN 2: Regla de la cadena
# ============================================================================

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('Regla de la cadena: Cómo se propaga el efecto', fontsize=13, fontweight='bold', pad=20)

# Bloques A -> B -> C
blocks = [('A', 2), ('B', 6), ('C', 10)]
for label, x in blocks:
    circ = Circle((x, 3), 0.9, edgecolor='black', facecolor='#D7BDE2', linewidth=2)
    ax.add_patch(circ)
    ax.text(x, 3, label, ha='center', va='center', fontsize=12, fontweight='bold')

# Flechas
ax.add_patch(FancyArrowPatch((2.9, 3), (5.1, 3), arrowstyle='->', mutation_scale=20, linewidth=2))
ax.add_patch(FancyArrowPatch((6.9, 3), (9.1, 3), arrowstyle='->', mutation_scale=20, linewidth=2))

ax.text(4.0, 3.5, 'dB/dA', ha='center', fontsize=10)
ax.text(8.0, 3.5, 'dC/dB', ha='center', fontsize=10)

# Regla
ax.text(6, 1.4, 'dC/dA = (dC/dB) × (dB/dA)', ha='center', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFFFCC', alpha=0.9))

plt.tight_layout()
plt.savefig(img_dir / '41_chain_rule.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 2 creada: 41_chain_rule.png")
plt.close()

# ============================================================================
# IMAGEN 3: Forward vs Backward
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 6))
ax.set_xlim(0, 13)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('Forward Pass vs Backward Pass', fontsize=13, fontweight='bold', pad=20)

# Capas
for i, x in enumerate([2, 5, 8, 11]):
    rect = FancyBboxPatch((x-1, 2.2), 2, 1.6, boxstyle='round,pad=0.1',
                          edgecolor='black', facecolor='#E8F4F8', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, 3, f'L{i+1}', ha='center', va='center', fontsize=10, fontweight='bold')

# Forward arrows (top)
ax.add_patch(FancyArrowPatch((2.9, 3.8), (4.1, 3.8), arrowstyle='->', mutation_scale=18, linewidth=2.5, color='#2ca02c'))
ax.add_patch(FancyArrowPatch((5.9, 3.8), (7.1, 3.8), arrowstyle='->', mutation_scale=18, linewidth=2.5, color='#2ca02c'))
ax.add_patch(FancyArrowPatch((8.9, 3.8), (10.1, 3.8), arrowstyle='->', mutation_scale=18, linewidth=2.5, color='#2ca02c'))
ax.text(6.5, 4.6, 'Forward: activaciones', ha='center', fontsize=10, color='#2ca02c', fontweight='bold')

# Backward arrows (bottom)
ax.add_patch(FancyArrowPatch((10.1, 2.2), (8.9, 2.2), arrowstyle='->', mutation_scale=18, linewidth=2.5, color='#d62728'))
ax.add_patch(FancyArrowPatch((7.1, 2.2), (5.9, 2.2), arrowstyle='->', mutation_scale=18, linewidth=2.5, color='#d62728'))
ax.add_patch(FancyArrowPatch((4.1, 2.2), (2.9, 2.2), arrowstyle='->', mutation_scale=18, linewidth=2.5, color='#d62728'))
ax.text(6.5, 1.2, 'Backward: gradientes', ha='center', fontsize=10, color='#d62728', fontweight='bold')

plt.tight_layout()
plt.savefig(img_dir / '42_forward_backward.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 3 creada: 42_forward_backward.png")
plt.close()

# ============================================================================
# IMAGEN 4: Intuición geométrica - engranajes
# ============================================================================

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('Intuición: El error se reparte hacia atrás', fontsize=13, fontweight='bold', pad=20)

# Engranajes
centers = [(2.5, 3), (5.5, 3), (8.5, 3)]
for i, (x, y) in enumerate(centers):
    gear = Circle((x, y), 1.0, edgecolor='black', facecolor='#F8B88B', linewidth=2)
    ax.add_patch(gear)
    ax.text(x, y, f'Capa {i+1}', ha='center', va='center', fontsize=10, fontweight='bold')

# Flechas de error
ax.add_patch(FancyArrowPatch((10.5, 3), (9.6, 3), arrowstyle='->', mutation_scale=20, linewidth=2.5, color='#d62728'))
ax.add_patch(FancyArrowPatch((7.5, 3), (6.6, 3), arrowstyle='->', mutation_scale=20, linewidth=2.5, color='#d62728'))
ax.add_patch(FancyArrowPatch((4.5, 3), (3.6, 3), arrowstyle='->', mutation_scale=20, linewidth=2.5, color='#d62728'))

ax.text(10.8, 3.7, 'Error', fontsize=10, color='#d62728', fontweight='bold')
ax.text(6.5, 1.2, 'Cada capa recibe una parte del error', ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.8))

plt.tight_layout()
plt.savefig(img_dir / '43_error_flow_gears.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 4 creada: 43_error_flow_gears.png")
plt.close()

# ============================================================================
# IMAGEN 5: Activaciones y gradientes
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Funciones de activación y su impacto en el gradiente', fontsize=13, fontweight='bold')

# Sigmoide
ax = axes[0]
x = np.linspace(-6, 6, 400)
sig = 1 / (1 + np.exp(-x))
ax.plot(x, sig, linewidth=2.5, color='#1f77b4', label='σ(x)')
ax.plot(x, sig * (1 - sig), linewidth=2.5, color='#d62728', label="σ'(x)")
ax.set_title('Sigmoide: gradiente pequeño\nen saturación', fontsize=11, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('valor')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)

# ReLU
ax = axes[1]
relu = np.maximum(0, x)
relu_grad = (x > 0).astype(float)
ax.plot(x, relu, linewidth=2.5, color='#1f77b4', label='ReLU(x)')
ax.plot(x, relu_grad, linewidth=2.5, color='#2ca02c', label="ReLU'(x)")
ax.set_title('ReLU: gradiente estable\npara x>0', fontsize=11, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('valor')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig(img_dir / '44_activaciones_gradientes.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 5 creada: 44_activaciones_gradientes.png")
plt.close()

print("\n" + "="*60)
print("✅ TODAS LAS IMÁGENES DEL CAPÍTULO 8 GENERADAS")
print("="*60)
print("\nImágenes disponibles:")
print("  1. 40_backprop_overview.png")
print("  2. 41_chain_rule.png")
print("  3. 42_forward_backward.png")
print("  4. 43_error_flow_gears.png")
print("  5. 44_activaciones_gradientes.png")
