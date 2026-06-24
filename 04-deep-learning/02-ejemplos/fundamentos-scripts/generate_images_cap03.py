"""
Script para generar imágenes ilustrativas del Capítulo 3
Representación matemática de datos: escalares, vectores, matrices y tensores
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np
from pathlib import Path

# Crear directorio para imágenes si no existe
img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

# ============================================================================
# IMAGEN 1: Escalar, Vector, Matriz, Tensor
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Escalares, Vectores, Matrices y Tensores', fontsize=14, fontweight='bold', y=0.995)

# 1. Escalar
ax = axes[0, 0]
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.axis('off')
ax.set_title('Escalar (0D)', fontweight='bold', fontsize=12)

rect_scalar = FancyBboxPatch((0.5, 0.5), 2, 1.5, boxstyle='round,pad=0.1',
                            edgecolor='black', facecolor='#AED6F1', linewidth=2)
ax.add_patch(rect_scalar)
ax.text(1.5, 1.25, '42', ha='center', va='center', fontsize=24, fontweight='bold')
ax.text(1.5, -0.3, 'Un número individual', ha='center', fontsize=9, style='italic')

# 2. Vector
ax = axes[0, 1]
ax.set_xlim(-0.5, 4)
ax.set_ylim(-1, 4)
ax.axis('off')
ax.set_title('Vector (1D)', fontweight='bold', fontsize=12)

vector_data = [2, 5, 3, 7]
for i, val in enumerate(vector_data):
    rect = Rectangle((i*0.9, 1.5), 0.8, 1.2, edgecolor='black', 
                     facecolor='#D7BDE2', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(i*0.9 + 0.4, 2.1, str(val), ha='center', va='center', 
           fontsize=12, fontweight='bold')

ax.text(1.5, -0.3, '[2, 5, 3, 7]  -  Una observación (4 variables)', 
       ha='center', fontsize=9, style='italic')

# Forma
ax.text(1.5, 3.3, 'shape: (4,)', ha='center', fontsize=9, 
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFF99', alpha=0.7))

# 3. Matriz
ax = axes[1, 0]
ax.set_xlim(-0.5, 4)
ax.set_ylim(-0.5, 5)
ax.axis('off')
ax.set_title('Matriz (2D)', fontweight='bold', fontsize=12)

matrix_data = np.array([[2, 5, 3],
                        [4, 1, 8],
                        [6, 9, 2]])

for i in range(3):
    for j in range(3):
        rect = Rectangle((j*0.9, 3 - i*0.9), 0.8, 0.8, edgecolor='black',
                         facecolor='#98D8C8', linewidth=1)
        ax.add_patch(rect)
        ax.text(j*0.9 + 0.4, 3.4 - i*0.9, str(matrix_data[i, j]), 
               ha='center', va='center', fontsize=10, fontweight='bold')

ax.text(1.5, 0.5, '3 observaciones × 3 variables', ha='center', fontsize=9, style='italic')
ax.text(1.5, 1.3, 'shape: (3, 3)', ha='center', fontsize=9,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFF99', alpha=0.7))

# 4. Tensor (imagen)
ax = axes[1, 1]
ax.set_xlim(-0.5, 4)
ax.set_ylim(-0.5, 5)
ax.axis('off')
ax.set_title('Tensor (3D+)', fontweight='bold', fontsize=12)

# Dibujar cubo con perspectiva para representar 3D
from matplotlib.patches import Polygon

# Frente
front = Polygon([[0.5, 1], [2, 1], [2, 2.5], [0.5, 2.5]], 
               facecolor='#F5B7B1', edgecolor='black', linewidth=1.5, alpha=0.8)
ax.add_patch(front)

# Lado
side = Polygon([[2, 1], [2.8, 0.5], [2.8, 2], [2, 2.5]],
              facecolor='#F8B88B', edgecolor='black', linewidth=1.5, alpha=0.8)
ax.add_patch(side)

# Arriba
top = Polygon([[0.5, 2.5], [2, 2.5], [2.8, 2], [1.3, 2]],
             facecolor='#FFE5CC', edgecolor='black', linewidth=1.5, alpha=0.8)
ax.add_patch(top)

ax.text(1.25, 1.75, '32×28\n×28×3', ha='center', va='center', 
       fontsize=9, fontweight='bold', color='black')

ax.text(1.5, 0.2, 'Batch de imágenes: 32 imágenes, 28×28 píxeles, 3 canales (RGB)', 
       ha='center', fontsize=8, style='italic')
ax.text(1.5, -0.15, 'shape: (32, 28, 28, 3)', ha='center', fontsize=9,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFF99', alpha=0.7))

plt.tight_layout()
plt.savefig(img_dir / '13_escalares_vectores_matrices_tensores.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 1 creada: 13_escalares_vectores_matrices_tensores.png")
plt.close()

# ============================================================================
# IMAGEN 2: Interpretación Geométrica
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Interpretación Geométrica de Vectores y Matrices', 
             fontsize=13, fontweight='bold', y=0.98)

# Vector en 2D
ax = axes[0]
ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Vector = Punto en el espacio', fontweight='bold', fontsize=11)
ax.set_xlabel('Variable 1')
ax.set_ylabel('Variable 2')

# Dibujar vector
v1 = np.array([2, 3])
ax.arrow(0, 0, v1[0], v1[1], head_width=0.2, head_length=0.15, 
        fc='#1f77b4', ec='#1f77b4', linewidth=2)
ax.plot(v1[0], v1[1], 'o', markersize=10, color='#1f77b4')
ax.text(v1[0]+0.2, v1[1]+0.2, 'v = [2, 3]', fontsize=10, fontweight='bold')

ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 5)

# Matriz en 2D - nube de puntos
ax = axes[1]
ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Matriz = Nube de puntos', fontweight='bold', fontsize=11)
ax.set_xlabel('Variable 1')
ax.set_ylabel('Variable 2')

np.random.seed(42)
points_class1 = np.random.randn(15, 2) + np.array([1.5, 1.5])
points_class2 = np.random.randn(15, 2) + np.array([3.5, 3.5])

ax.scatter(points_class1[:, 0], points_class1[:, 1], c='#AED6F1', s=100,
          edgecolors='#1f77b4', linewidth=1.5, label='Clase 1', alpha=0.7)
ax.scatter(points_class2[:, 0], points_class2[:, 1], c='#F5B7B1', s=100,
          edgecolors='#d62728', linewidth=1.5, label='Clase 2', alpha=0.7)

ax.legend(fontsize=9)
ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 5)

# Tensor en 3D
ax = axes[2]
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
ax.set_title('Tensor 3D = Múltiples nubes', fontweight='bold', fontsize=11)
ax.axis('off')

# Dibujar 3 capas para representar tensor 3D
colors = ['#AED6F1', '#D7BDE2', '#98D8C8']
labels = ['Capa 1', 'Capa 2', 'Capa 3']

for layer in range(3):
    offset = layer * 0.3
    for i in range(5):
        x = np.random.randn() * 0.6 + 2 + offset
        y = np.random.randn() * 0.6 + 2.5 + offset
        circle = plt.Circle((x, y), 0.15, color=colors[layer], alpha=0.7, ec='black', linewidth=1)
        ax.add_patch(circle)

ax.text(2, 4.8, 'shape: (32, 10, 10)', ha='center', fontsize=9,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFF99', alpha=0.7))
ax.text(2, -0.3, 'Tensor ND: cada "capa" es una matriz', ha='center', fontsize=9, style='italic')
ax.set_xlim(0, 4)
ax.set_ylim(-0.5, 5.5)

plt.tight_layout()
plt.savefig(img_dir / '14_interpretacion_geometrica.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 2 creada: 14_interpretacion_geometrica.png")
plt.close()

# ============================================================================
# IMAGEN 3: Batches de datos
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 7))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Batches: Procesamiento iterativo de datos', fontsize=13, fontweight='bold', pad=20)

# Dataset completo
rect_full = FancyBboxPatch((0.5, 6), 3, 2.5, boxstyle='round,pad=0.1',
                          edgecolor='#1f77b4', facecolor='#AED6F1', linewidth=2)
ax.add_patch(rect_full)
ax.text(2, 7.5, 'Dataset Completo\n1000 observaciones\nshape: (1000, 10)', 
       ha='center', va='center', fontsize=10, fontweight='bold')

# Flecha
arrow = FancyArrowPatch((3.7, 7.25), (4.8, 7.25),
                       arrowstyle='->', mutation_scale=30, linewidth=2.5, color='gray')
ax.add_patch(arrow)

# Batches
batch_positions = [(5.5, 8), (5.5, 6.5), (5.5, 5), (8.5, 8), (8.5, 6.5), (8.5, 5)]
batch_labels = ['Batch 1\n(32, 10)', 'Batch 2\n(32, 10)', 'Batch 3\n(32, 10)', 
               'Batch 4\n(32, 10)', 'Batch 5\n(32, 10)', 'Batch 6\n(32, 10)']

for i, (x, y) in enumerate(batch_positions[:6]):
    rect_batch = FancyBboxPatch((x-0.6, y-0.5), 1.2, 1, boxstyle='round,pad=0.05',
                               edgecolor='black', facecolor='#D7BDE2', linewidth=1.5)
    ax.add_patch(rect_batch)
    ax.text(x, y, batch_labels[i], ha='center', va='center', fontsize=8, fontweight='bold')

# Ventaja de batches
ax.text(10.5, 8.5, 'Ventajas de Batches:', fontweight='bold', fontsize=11)
advantages = [
    '✓ Menor consumo de memoria',
    '✓ Actualización más frecuente',
    '✓ Mejor generalización',
    '✓ Paralelización eficiente',
    '✓ Convergencia más estable'
]

for i, adv in enumerate(advantages):
    ax.text(10.5, 8 - i*0.35, adv, fontsize=9)

# Flujo de entrenamiento
ax.text(6.5, 4, 'Flujo de entrenamiento:', fontweight='bold', fontsize=10)
flow_steps = ['1. Cargar batch', '2. Forward Pass', '3. Calcular pérdida', 
             '4. Backprop', '5. Actualizar pesos', '6. Siguiente batch']

for i, step in enumerate(flow_steps):
    y_pos = 3.4 - i * 0.35
    ax.text(6.5, y_pos, step, fontsize=9)

plt.tight_layout()
plt.savefig(img_dir / '15_batches_datos.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 3 creada: 15_batches_datos.png")
plt.close()

# ============================================================================
# IMAGEN 4: Operaciones Básicas
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle('Operaciones Básicas con Tensores', fontsize=13, fontweight='bold', y=0.995)

# Suma elemento a elemento
ax = axes[0, 0]
ax.set_xlim(-0.5, 6)
ax.set_ylim(-0.5, 5)
ax.axis('off')
ax.set_title('Suma Elemento a Elemento', fontweight='bold', fontsize=11)

# A
ax.text(0.8, 4.5, 'A =', fontweight='bold', fontsize=11)
A = np.array([[1, 2], [3, 4]])
for i in range(2):
    for j in range(2):
        rect = Rectangle((1.2 + j*0.6, 3.5 - i*0.5), 0.5, 0.45, 
                        edgecolor='black', facecolor='#AED6F1', linewidth=1)
        ax.add_patch(rect)
        ax.text(1.45 + j*0.6, 3.725 - i*0.5, str(A[i,j]), ha='center', va='center', fontsize=10)

# +
ax.text(2.6, 3.3, '+', fontsize=14, fontweight='bold')

# B
B = np.array([[5, 6], [7, 8]])
for i in range(2):
    for j in range(2):
        rect = Rectangle((3 + j*0.6, 3.5 - i*0.5), 0.5, 0.45,
                        edgecolor='black', facecolor='#D7BDE2', linewidth=1)
        ax.add_patch(rect)
        ax.text(3.25 + j*0.6, 3.725 - i*0.5, str(B[i,j]), ha='center', va='center', fontsize=10)

# =
ax.text(4.2, 3.3, '=', fontsize=14, fontweight='bold')

# Resultado
C = A + B
for i in range(2):
    for j in range(2):
        rect = Rectangle((4.8 + j*0.6, 3.5 - i*0.5), 0.5, 0.45,
                        edgecolor='black', facecolor='#98D8C8', linewidth=1)
        ax.add_patch(rect)
        ax.text(5.05 + j*0.6, 3.725 - i*0.5, str(C[i,j]), ha='center', va='center', fontsize=10)

ax.text(2.5, 1.8, 'Operación posición a posición\nRápida y paralelizable', 
       ha='center', fontsize=9, style='italic',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.7))

# Multiplicación elemento a elemento
ax = axes[0, 1]
ax.set_xlim(-0.5, 6)
ax.set_ylim(-0.5, 5)
ax.axis('off')
ax.set_title('Multiplicación Elemento a Elemento', fontweight='bold', fontsize=11)

ax.text(0.5, 4.5, 'A ⊙ B', fontweight='bold', fontsize=11)
D = np.array([[2, 3], [1, 4]])
E = np.array([[0, 1], [2, 1]])
F = D * E

for i in range(2):
    for j in range(2):
        rect = Rectangle((1.2 + j*0.6, 3.5 - i*0.5), 0.5, 0.45,
                        edgecolor='black', facecolor='#AED6F1', linewidth=1)
        ax.add_patch(rect)
        ax.text(1.45 + j*0.6, 3.725 - i*0.5, str(D[i,j]), ha='center', va='center', fontsize=10)

ax.text(2.5, 3.3, '⊙', fontsize=14, fontweight='bold')

for i in range(2):
    for j in range(2):
        rect = Rectangle((3 + j*0.6, 3.5 - i*0.5), 0.5, 0.45,
                        edgecolor='black', facecolor='#D7BDE2', linewidth=1)
        ax.add_patch(rect)
        ax.text(3.25 + j*0.6, 3.725 - i*0.5, str(E[i,j]), ha='center', va='center', fontsize=10)

ax.text(4.2, 3.3, '=', fontsize=14, fontweight='bold')

for i in range(2):
    for j in range(2):
        rect = Rectangle((4.8 + j*0.6, 3.5 - i*0.5), 0.5, 0.45,
                        edgecolor='black', facecolor='#98D8C8', linewidth=1)
        ax.add_patch(rect)
        ax.text(5.05 + j*0.6, 3.725 - i*0.5, str(F[i,j]), ha='center', va='center', fontsize=10)

ax.text(2.5, 1.8, 'Se aplica en activaciones\ny normalización', 
       ha='center', fontsize=9, style='italic',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.7))

# Broadcasting
ax = axes[1, 0]
ax.set_xlim(-0.5, 6)
ax.set_ylim(-0.5, 5)
ax.axis('off')
ax.set_title('Broadcasting: Suma con sesgo', fontweight='bold', fontsize=11)

ax.text(1.5, 4.5, 'X + b', fontweight='bold', fontsize=11)

# Matriz X
for i in range(2):
    for j in range(3):
        rect = Rectangle((0.7 + j*0.5, 3.5 - i*0.4), 0.45, 0.35,
                        edgecolor='black', facecolor='#AED6F1', linewidth=1)
        ax.add_patch(rect)
        ax.text(0.925 + j*0.5, 3.675 - i*0.4, '●', ha='center', va='center', fontsize=8)

ax.text(2.3, 3.3, '+', fontsize=14, fontweight='bold')

# Bias
for i in range(1):
    for j in range(3):
        rect = Rectangle((2.7 + j*0.5, 3.15), 0.45, 0.35,
                        edgecolor='black', facecolor='#D7BDE2', linewidth=1)
        ax.add_patch(rect)
        ax.text(2.925 + j*0.5, 3.325, 'b', ha='center', va='center', fontsize=8)

ax.text(3.9, 3.3, '=', fontsize=14, fontweight='bold')

# Resultado
for i in range(2):
    for j in range(3):
        rect = Rectangle((4.3 + j*0.5, 3.5 - i*0.4), 0.45, 0.35,
                        edgecolor='black', facecolor='#98D8C8', linewidth=1)
        ax.add_patch(rect)
        ax.text(4.525 + j*0.5, 3.675 - i*0.4, '●', ha='center', va='center', fontsize=8)

ax.text(2.5, 1.8, 'Broadcasting replica el sesgo\npara cada fila de X', 
       ha='center', fontsize=9, style='italic',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.7))

# Producto matricial
ax = axes[1, 1]
ax.set_xlim(-0.5, 6)
ax.set_ylim(-0.5, 5)
ax.axis('off')
ax.set_title('Producto Matricial: X @ W', fontweight='bold', fontsize=11)

ax.text(1.5, 4.5, 'Y = X @ W', fontweight='bold', fontsize=11)

# X (m x n)
ax.text(0.5, 4, 'X', fontweight='bold', fontsize=10)
for i in range(2):
    for j in range(2):
        rect = Rectangle((0.5 + j*0.4, 3.2 - i*0.3), 0.35, 0.25,
                        edgecolor='black', facecolor='#AED6F1', linewidth=1)
        ax.add_patch(rect)

ax.text(0.7, 2.8, '2×2', ha='center', fontsize=8, style='italic')

# W (n x p)
ax.text(1.5, 4, 'W', fontweight='bold', fontsize=10)
for i in range(2):
    for j in range(3):
        rect = Rectangle((1.5 + j*0.3, 3.2 - i*0.25), 0.25, 0.2,
                        edgecolor='black', facecolor='#D7BDE2', linewidth=1)
        ax.add_patch(rect)

ax.text(1.95, 2.9, '2×3', ha='center', fontsize=8, style='italic')

ax.text(2.5, 3.5, '@', fontsize=14, fontweight='bold')

# = Y (m x p)
ax.text(3.2, 4, '=', fontsize=14, fontweight='bold')
ax.text(3.7, 4, 'Y', fontweight='bold', fontsize=10)

for i in range(2):
    for j in range(3):
        rect = Rectangle((3.7 + j*0.4, 3.15 - i*0.3), 0.35, 0.25,
                        edgecolor='black', facecolor='#98D8C8', linewidth=1)
        ax.add_patch(rect)

ax.text(4.65, 2.75, '2×3', ha='center', fontsize=8, style='italic')

ax.text(2.5, 1.8, 'La operación CENTRAL en redes neuronales\nCombinación lineal de variables', 
       ha='center', fontsize=9, style='italic',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.7))

plt.tight_layout()
plt.savefig(img_dir / '16_operaciones_basicas.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 4 creada: 16_operaciones_basicas.png")
plt.close()

# ============================================================================
# IMAGEN 5: Reshape
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 6))
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_title('Reshape: Cambiar la forma sin cambiar los datos', fontsize=13, fontweight='bold', pad=20)

# Original
ax.text(1.5, 6.3, 'Original', fontweight='bold', fontsize=11)
ax.text(1.5, 5.9, 'shape: (2, 3)', fontsize=9, style='italic')

data = np.array([[1, 2, 3], [4, 5, 6]])
for i in range(2):
    for j in range(3):
        rect = Rectangle((0.5 + j*0.6, 4.5 - i*0.5), 0.55, 0.45,
                        edgecolor='black', facecolor='#AED6F1', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(0.775 + j*0.6, 4.725 - i*0.5, str(data[i,j]), ha='center', va='center', fontsize=10, fontweight='bold')

# Arrow
arrow = FancyArrowPatch((2.5, 4), (3.5, 4),
                       arrowstyle='->', mutation_scale=30, linewidth=2.5, color='gray')
ax.add_patch(arrow)
ax.text(3, 4.4, '.reshape(3, 2)', ha='center', fontsize=9, fontweight='bold')

# Reshaped
ax.text(4.5, 6.3, 'Reshaped', fontweight='bold', fontsize=11)
ax.text(4.5, 5.9, 'shape: (3, 2)', fontsize=9, style='italic')

for i in range(3):
    for j in range(2):
        rect = Rectangle((4 + j*0.6, 4.5 - i*0.5), 0.55, 0.45,
                        edgecolor='black', facecolor='#D7BDE2', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(4.275 + j*0.6, 4.725 - i*0.5, str(data.reshape(3, 2)[i,j]), 
               ha='center', va='center', fontsize=10, fontweight='bold')

# Otros reshapes
reshapes = [
    ('(6,)', 6),
    ('(1, 6)', 8),
    ('(6, 1)', 10),
]

ax.text(6.5, 6.3, 'Otros Reshapes Posibles', fontweight='bold', fontsize=11)

for reshape_str, x_pos in reshapes:
    ax.text(x_pos, 5.9, f'shape: {reshape_str}', fontsize=8, style='italic')
    
    # Mostrar representación
    if reshape_str == '(6,)':
        for j in range(6):
            rect = Rectangle((x_pos - 1.5 + j*0.3, 4.2), 0.25, 0.4,
                           edgecolor='black', facecolor='#98D8C8', linewidth=1)
            ax.add_patch(rect)
    elif reshape_str == '(1, 6)':
        for j in range(6):
            rect = Rectangle((x_pos - 1.5 + j*0.3, 4.2), 0.25, 0.4,
                           edgecolor='black', facecolor='#98D8C8', linewidth=1)
            ax.add_patch(rect)
    else:  # (6, 1)
        for i in range(6):
            rect = Rectangle((x_pos - 0.3, 4.8 - i*0.25), 0.25, 0.2,
                           edgecolor='black', facecolor='#98D8C8', linewidth=1)
            ax.add_patch(rect)

# Clave: Los datos son los mismos
ax.text(6.5, 2, 'CLAVE: Los datos NO cambian, solo cómo se interpretan', 
       fontsize=10, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFF99', alpha=0.8))

# Casos de uso
use_cases = [
    'CNN: pasar entre capas densas y convolucionales',
    'RNN: preparar datos secuenciales',
    'Batches: agrupar o expandir dimensiones',
]

ax.text(1, 1, 'Casos de uso común:', fontweight='bold', fontsize=10)
for i, case in enumerate(use_cases):
    ax.text(1.2, 0.6 - i*0.35, f'• {case}', fontsize=8)

plt.tight_layout()
plt.savefig(img_dir / '17_reshape.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 5 creada: 17_reshape.png")
plt.close()

# ============================================================================
# IMAGEN 6: Shape y Debugging
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Entender Shape: Clave para debugging', fontsize=13, fontweight='bold', pad=20)

# Jerarquía de shapes
ax.text(1, 9.2, 'Jerarquía de Dimensiones:', fontweight='bold', fontsize=11)

shapes = [
    ('Escalar', '42', 'Número único', '#AED6F1', 1.5),
    ('Vector', '(4,)', '[2, 5, 3, 7]', '#D7BDE2', 3),
    ('Matriz', '(3, 4)', '3 filas × 4 columnas', '#98D8C8', 4.5),
    ('Tensor 3D', '(32, 28, 28)', 'Lote de 32 imágenes', '#FFE5CC', 6),
    ('Tensor 4D', '(32, 28, 28, 3)', 'Lote con 3 canales RGB', '#F8B88B', 7.5),
]

for name, shape, desc, color, y in shapes:
    rect = FancyBboxPatch((0.5, y - 0.35), 3, 0.7, boxstyle='round,pad=0.05',
                         edgecolor='black', facecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(0.7, y, f'{name}:', fontweight='bold', fontsize=9)
    ax.text(2.5, y, f'{shape} - {desc}', fontsize=8, style='italic')

# Error común
ax.text(5.5, 8.8, 'Error Común en CNN:', fontweight='bold', fontsize=11, color='#d62728')

error_box = FancyBboxPatch((5, 7.5), 7.5, 1, boxstyle='round,pad=0.1',
                          edgecolor='#d62728', facecolor='#FFE5E5', linewidth=2)
ax.add_patch(error_box)

ax.text(5.2, 8.2, '❌ Error: Esperado (batch, 784) pero obtuve (batch, 28, 28)', 
       fontsize=9, fontweight='bold', color='#d62728')
ax.text(5.2, 7.8, '👉 Solución: x.reshape(batch_size, -1) para aplanar', 
       fontsize=9, color='#2ca02c', fontweight='bold')

# Debugging ejemplo
ax.text(5.5, 6.8, 'Debugging paso a paso:', fontweight='bold', fontsize=11)

debug_steps = [
    'print(X.shape)         → (1000, 28, 28, 1)',
    'X_flat = X.reshape(1000, -1)  → (1000, 784)',
    'Y = X_flat @ W         → Shape de W debe ser (784, 10)',
    'Y.shape                → (1000, 10)  ✓',
]

for i, step in enumerate(debug_steps):
    y_pos = 6.2 - i * 0.4
    if '✓' in step:
        box_color = '#E5F5E5'
        ax.text(5.3, y_pos, step, fontsize=8, family='monospace',
               bbox=dict(boxstyle='round,pad=0.3', facecolor=box_color, alpha=0.8))
    else:
        ax.text(5.3, y_pos, step, fontsize=8, family='monospace')

# Shape mnemotécnico
ax.text(1, 4.5, 'Regla mnemotécnica (Batch first):', fontweight='bold', fontsize=11)

rule_box = FancyBboxPatch((0.5, 2.8), 4, 1.4, boxstyle='round,pad=0.1',
                         edgecolor='#1f77b4', facecolor='#E8F4F8', linewidth=2)
ax.add_patch(rule_box)

rules = [
    '(Batch, Features)         → Datos tabulares',
    '(Batch, Height, Width)    → Imágenes 1 canal',
    '(Batch, H, W, Channels)   → Imágenes RGB',
    '(Batch, Time, Features)   → Series temporales',
]

for i, rule in enumerate(rules):
    ax.text(0.7, 4 - i * 0.3, rule, fontsize=8, family='monospace')

# Herramientas útiles
ax.text(5.5, 4.5, 'Herramientas para debugging:', fontweight='bold', fontsize=11)

tools = [
    'tensor.shape              Ver dimensiones',
    'tensor.reshape(...)       Cambiar forma',
    'tensor.flatten()          Aplanar a 1D',
    'tensor.view(...)          Cambiar sin copiar',
]

for i, tool in enumerate(tools):
    y_pos = 4 - i * 0.35
    parts = tool.split('      ')
    ax.text(5.5, y_pos, parts[0], fontsize=8, family='monospace', fontweight='bold')
    ax.text(7.5, y_pos, parts[1], fontsize=8, style='italic')

plt.tight_layout()
plt.savefig(img_dir / '18_shape_debugging.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 6 creada: 18_shape_debugging.png")
plt.close()

print("\n" + "="*60)
print("✅ TODAS LAS IMÁGENES DEL CAPÍTULO 3 GENERADAS")
print("="*60)
print("\nImágenes disponibles:")
print("  1. 13_escalares_vectores_matrices_tensores.png")
print("  2. 14_interpretacion_geometrica.png")
print("  3. 15_batches_datos.png")
print("  4. 16_operaciones_basicas.png")
print("  5. 17_reshape.png")
print("  6. 18_shape_debugging.png")
