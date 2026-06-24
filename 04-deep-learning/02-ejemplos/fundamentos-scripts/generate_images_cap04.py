"""
Script para generar imágenes ilustrativas del Capítulo 4
Operaciones con tensores y redes neuronales como funciones
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon
import numpy as np
from pathlib import Path

img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

# ============================================================================
# IMAGEN 1: Red Neuronal como Función
# ============================================================================

fig, ax = plt.subplots(figsize=(13, 7))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Una Red Neuronal es una Función', fontsize=13, fontweight='bold', pad=20)

# Entrada
rect_input = FancyBboxPatch((1, 4), 2, 2, boxstyle='round,pad=0.1',
                           edgecolor='#1f77b4', facecolor='#AED6F1', linewidth=2)
ax.add_patch(rect_input)
ax.text(2, 5, 'Entrada\nx\n(tensor)', ha='center', va='center', fontsize=10, fontweight='bold')

# Red neuronal (caja negra)
rect_nn = FancyBboxPatch((4.5, 3), 4, 4, boxstyle='round,pad=0.1',
                        edgecolor='#9467bd', facecolor='#D7BDE2', linewidth=2.5)
ax.add_patch(rect_nn)
ax.text(6.5, 6.3, 'Red Neuronal', ha='center', fontsize=11, fontweight='bold')
ax.text(6.5, 5, 'f(x)', ha='center', fontsize=14, fontweight='bold', style='italic')
ax.text(6.5, 4.2, 'Composición de\ntransformaciones', ha='center', fontsize=9, style='italic')

# Salida
rect_output = FancyBboxPatch((10, 4), 2, 2, boxstyle='round,pad=0.1',
                            edgecolor='#2ca02c', facecolor='#98D8C8', linewidth=2)
ax.add_patch(rect_output)
ax.text(11, 5, 'Salida\nŷ\n(predicción)', ha='center', va='center', fontsize=10, fontweight='bold')

# Flechas
arrow1 = FancyArrowPatch((3.1, 5), (4.4, 5),
                        arrowstyle='->', mutation_scale=30, linewidth=2.5, color='gray')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((8.6, 5), (9.9, 5),
                        arrowstyle='->', mutation_scale=30, linewidth=2.5, color='gray')
ax.add_patch(arrow2)

# Explicación abajo
explanation = (
    "ŷ = f(x) = f_n(f_{n-1}(...f_2(f_1(x))))\n\n"
    "Cada capa aplica una transformación:\n"
    "1. Lineal: Y = X @ W + b\n"
    "2. No lineal: activación(Y)"
)

ax.text(6.5, 1.5, explanation, ha='center', fontsize=9,
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFFCC', alpha=0.8))

plt.tight_layout()
plt.savefig(img_dir / '19_red_como_funcion.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 1 creada: 19_red_como_funcion.png")
plt.close()

# ============================================================================
# IMAGEN 2: Transformación Lineal
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Transformación Lineal: Y = X @ W + b', fontsize=13, fontweight='bold', y=0.98)

# Producto matricial
ax = axes[0]
ax.set_xlim(-0.5, 8)
ax.set_ylim(-0.5, 7)
ax.axis('off')
ax.set_title('Producto Matricial: X @ W', fontweight='bold', fontsize=11)

# X matriz
ax.text(1, 6, 'X', fontweight='bold', fontsize=11)
ax.text(1, 5.5, '(batch, in)', fontsize=8, style='italic')
for i in range(3):
    for j in range(2):
        rect = Rectangle((0.5 + j*0.5, 4.5 - i*0.4), 0.45, 0.35,
                        edgecolor='black', facecolor='#AED6F1', linewidth=1)
        ax.add_patch(rect)

# W matriz
ax.text(3, 6, 'W', fontweight='bold', fontsize=11)
ax.text(3, 5.5, '(in, out)', fontsize=8, style='italic')
for i in range(2):
    for j in range(4):
        rect = Rectangle((2.5 + j*0.4, 4.8 - i*0.35), 0.35, 0.3,
                        edgecolor='black', facecolor='#D7BDE2', linewidth=1)
        ax.add_patch(rect)

ax.text(2, 3.8, '@', fontsize=14, fontweight='bold')

# Y resultado
ax.text(5, 6, '= Y', fontweight='bold', fontsize=11)
ax.text(5, 5.5, '(batch, out)', fontsize=8, style='italic')
for i in range(3):
    for j in range(4):
        rect = Rectangle((4.5 + j*0.4, 4.5 - i*0.4), 0.35, 0.35,
                        edgecolor='black', facecolor='#98D8C8', linewidth=1)
        ax.add_patch(rect)

ax.text(3.5, 2.5, 'Cada fila de X se combina\ncon todas las columnas de W', 
       ha='center', fontsize=9, style='italic',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F4F8', alpha=0.7))

# Interpretación geométrica
ax = axes[1]
ax.set_xlim(-3, 5)
ax.set_ylim(-3, 5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Efecto Geométrico: Rotación y Escala', fontweight='bold', fontsize=11)
ax.set_xlabel('Dimensión 1')
ax.set_ylabel('Dimensión 2')

# Datos originales
np.random.seed(42)
X_orig = np.random.randn(20, 2) * 0.8 + np.array([0, 0])

ax.scatter(X_orig[:, 0], X_orig[:, 1], c='#AED6F1', s=100,
          edgecolors='#1f77b4', linewidth=1.5, label='Datos originales', alpha=0.7, zorder=3)

# Transformados
theta = np.pi / 4
W = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]]) * 1.5
X_trans = X_orig @ W

ax.scatter(X_trans[:, 0], X_trans[:, 1], c='#98D8C8', s=100,
          edgecolors='#2ca02c', linewidth=1.5, label='Después de X @ W', alpha=0.7, zorder=3)

# Vectores de ejemplo
ax.arrow(0, 0, X_orig[0, 0], X_orig[0, 1], head_width=0.2, head_length=0.15,
        fc='#1f77b4', ec='#1f77b4', linewidth=1.5, alpha=0.5, zorder=2)
ax.arrow(0, 0, X_trans[0, 0], X_trans[0, 1], head_width=0.2, head_length=0.15,
        fc='#2ca02c', ec='#2ca02c', linewidth=1.5, alpha=0.5, zorder=2)

ax.legend(fontsize=9, loc='upper left')

plt.tight_layout()
plt.savefig(img_dir / '20_transformacion_lineal.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 2 creada: 20_transformacion_lineal.png")
plt.close()

# ============================================================================
# IMAGEN 3: Operaciones Elemento a Elemento
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle('Operaciones Elemento a Elemento', fontsize=13, fontweight='bold', y=0.995)

# ReLU
ax = axes[0, 0]
ax.set_xlim(-0.5, 6)
ax.set_ylim(-0.5, 4)
ax.axis('off')
ax.set_title('ReLU: max(0, x)', fontweight='bold', fontsize=11)

input_vals = [-2, 1, -1, 3]
output_vals = [max(0, v) for v in input_vals]

ax.text(1, 3.5, 'Entrada:', fontweight='bold', fontsize=10)
for i, val in enumerate(input_vals):
    rect = Rectangle((0.5 + i*0.8, 2.8), 0.7, 0.5,
                    edgecolor='black', facecolor='#AED6F1', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(0.85 + i*0.8, 3.05, str(val), ha='center', va='center', fontsize=10, fontweight='bold')

ax.text(1.8, 2.3, 'ReLU', fontsize=10, fontweight='bold')
for i in range(4):
    arrow = FancyArrowPatch((0.85 + i*0.8, 2.7), (0.85 + i*0.8, 2.1),
                           arrowstyle='->', mutation_scale=20, linewidth=1.5, color='gray')
    ax.add_patch(arrow)

ax.text(1, 1.5, 'Salida:', fontweight='bold', fontsize=10)
for i, val in enumerate(output_vals):
    color = '#98D8C8' if val > 0 else '#FFE5CC'
    rect = Rectangle((0.5 + i*0.8, 0.8), 0.7, 0.5,
                    edgecolor='black', facecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(0.85 + i*0.8, 1.05, str(val), ha='center', va='center', fontsize=10, fontweight='bold')

# Sigmoid
ax = axes[0, 1]
ax.set_xlim(-5, 5)
ax.set_ylim(-0.2, 1.2)
ax.grid(True, alpha=0.3)
ax.set_title('Sigmoid: σ(x) = 1/(1+e^(-x))', fontweight='bold', fontsize=11)

x = np.linspace(-5, 5, 200)
y = 1 / (1 + np.exp(-x))
ax.plot(x, y, linewidth=2.5, color='#ff7f0e')

ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)

# Mostrar transformación de valores
test_vals = [-3, 0, 3]
for xv in test_vals:
    yv = 1 / (1 + np.exp(-xv))
    ax.plot(xv, yv, 'o', markersize=8, color='red', zorder=3)
    ax.text(xv, yv + 0.1, f'{yv:.2f}', ha='center', fontsize=8)

ax.set_xlabel('x')
ax.set_ylabel('σ(x)')

# Tanh
ax = axes[1, 0]
ax.set_xlim(-5, 5)
ax.set_ylim(-1.2, 1.2)
ax.grid(True, alpha=0.3)
ax.set_title('Tanh: tanh(x)', fontweight='bold', fontsize=11)

x = np.linspace(-5, 5, 200)
y = np.tanh(x)
ax.plot(x, y, linewidth=2.5, color='#2ca02c')

ax.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)

test_vals = [-2, 0, 2]
for xv in test_vals:
    yv = np.tanh(xv)
    ax.plot(xv, yv, 'o', markersize=8, color='red', zorder=3)
    ax.text(xv, yv + 0.15, f'{yv:.2f}', ha='center', fontsize=8)

ax.set_xlabel('x')
ax.set_ylabel('tanh(x)')

# Composición
ax = axes[1, 1]
ax.set_xlim(-0.5, 6)
ax.set_ylim(-0.5, 5)
ax.axis('off')
ax.set_title('Composición: Lineal + Activación', fontweight='bold', fontsize=11)

# Paso 1: Lineal
ax.text(1, 4.5, '1. Transformación Lineal', fontweight='bold', fontsize=10)
ax.text(1, 4.1, 'z = X @ W + b', fontsize=9, style='italic')

rect1 = FancyBboxPatch((0.5, 3.2), 2, 0.7, boxstyle='round,pad=0.05',
                      edgecolor='black', facecolor='#AED6F1', linewidth=1.5)
ax.add_patch(rect1)
ax.text(1.5, 3.55, 'z = [-1, 2, -0.5]', ha='center', fontsize=8, family='monospace')

# Flecha
arrow = FancyArrowPatch((1.5, 3.1), (1.5, 2.5),
                       arrowstyle='->', mutation_scale=25, linewidth=2, color='gray')
ax.add_patch(arrow)

# Paso 2: Activación
ax.text(1, 2.3, '2. Activación ReLU', fontweight='bold', fontsize=10)
ax.text(1, 1.9, 'y = max(0, z)', fontsize=9, style='italic')

rect2 = FancyBboxPatch((0.5, 1), 2, 0.7, boxstyle='round,pad=0.05',
                      edgecolor='black', facecolor='#98D8C8', linewidth=1.5)
ax.add_patch(rect2)
ax.text(1.5, 1.35, 'y = [0, 2, 0]', ha='center', fontsize=8, family='monospace')

ax.text(4.5, 2.5, 'Se aplica\nelemento\na elemento', ha='center', fontsize=9, 
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.7))

plt.tight_layout()
plt.savefig(img_dir / '21_operaciones_elemento_elemento.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 3 creada: 21_operaciones_elemento_elemento.png")
plt.close()

# ============================================================================
# IMAGEN 4: Composición de Funciones
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Composición de Funciones: Red Neuronal Profunda', fontsize=13, fontweight='bold', pad=20)

# Capas
layers = [
    ('Entrada\nx', 1.5, '#AED6F1'),
    ('Capa 1\nf₁(x)', 3.5, '#D7BDE2'),
    ('Capa 2\nf₂(f₁(x))', 5.5, '#D7BDE2'),
    ('Capa 3\nf₃(f₂(f₁(x)))', 7.5, '#D7BDE2'),
    ('Capa 4\nf₄(...)', 9.5, '#D7BDE2'),
    ('Salida\nŷ', 11.5, '#98D8C8'),
]

for label, x, color in layers:
    rect = FancyBboxPatch((x - 0.7, 4), 1.4, 2, boxstyle='round,pad=0.1',
                         edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, 5, label, ha='center', va='center', fontsize=9, fontweight='bold')

# Flechas
for i in range(len(layers) - 1):
    x1, x2 = layers[i][1] + 0.7, layers[i + 1][1] - 0.7
    arrow = FancyArrowPatch((x1, 5), (x2, 5),
                           arrowstyle='->', mutation_scale=25, linewidth=2.5, color='gray')
    ax.add_patch(arrow)

# Fórmula completa
formula = r'$\hat{y} = f_4(f_3(f_2(f_1(x))))$'
ax.text(6.5, 2.5, formula, ha='center', fontsize=14, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFFCC', alpha=0.8))

# Explicación por capa
explanations = [
    'Cada f_i realiza:',
    '1. Transformación lineal: z = W @ a + b',
    '2. Activación no lineal: a = σ(z)',
]

for i, exp in enumerate(explanations):
    ax.text(6.5, 8.5 - i*0.4, exp, ha='center', fontsize=9, fontweight='bold' if i == 0 else 'normal',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F4F8', alpha=0.7))

# Flecha de profundidad
arrow_depth = FancyArrowPatch((1.5, 7.5), (11.5, 7.5),
                             arrowstyle='<->', mutation_scale=25, linewidth=2, color='#d62728')
ax.add_patch(arrow_depth)
ax.text(6.5, 8, 'Profundidad de la red', ha='center', fontsize=10, color='#d62728', fontweight='bold')

plt.tight_layout()
plt.savefig(img_dir / '22_composicion_funciones.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 4 creada: 22_composicion_funciones.png")
plt.close()

# ============================================================================
# IMAGEN 5: Deformación del Espacio
# ============================================================================

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
fig.suptitle('Redes Neuronales como Deformación del Espacio', fontsize=13, fontweight='bold', y=1.02)

np.random.seed(42)

# Datos originales
ax = axes[0]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('0. Datos Originales', fontweight='bold', fontsize=10)

class1 = np.random.randn(30, 2) * 0.6 + np.array([-1, -1])
class2 = np.random.randn(30, 2) * 0.6 + np.array([1, 1])

ax.scatter(class1[:, 0], class1[:, 1], c='#AED6F1', s=80, edgecolors='#1f77b4', linewidth=1.5, alpha=0.7)
ax.scatter(class2[:, 0], class2[:, 1], c='#F5B7B1', s=80, edgecolors='#d62728', linewidth=1.5, alpha=0.7)

# Después de capa 1
ax = axes[1]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('1. Después Capa 1\n(Lineal + ReLU)', fontweight='bold', fontsize=10)

# Rotación
angle = np.pi / 6
rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
class1_t1 = (class1 @ rot.T) * 0.9
class2_t1 = (class2 @ rot.T) * 0.9
class1_t1 = np.maximum(class1_t1, 0) - 0.5
class2_t1 = np.maximum(class2_t1, 0) - 0.5

ax.scatter(class1_t1[:, 0], class1_t1[:, 1], c='#AED6F1', s=80, edgecolors='#1f77b4', linewidth=1.5, alpha=0.7)
ax.scatter(class2_t1[:, 0], class2_t1[:, 1], c='#F5B7B1', s=80, edgecolors='#d62728', linewidth=1.5, alpha=0.7)

# Después de capa 2
ax = axes[2]
ax.set_xlim(-0.2, 2.5)
ax.set_ylim(-0.2, 2.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('2. Después Capa 2\n(Mayor separación)', fontweight='bold', fontsize=10)

class1_t2 = class1_t1 * np.array([1.2, 0.8]) + np.array([0.3, 0.3])
class2_t2 = class2_t1 * np.array([0.8, 1.2]) + np.array([1.2, 1.2])
class1_t2 = np.maximum(class1_t2, 0)
class2_t2 = np.maximum(class2_t2, 0)

ax.scatter(class1_t2[:, 0], class1_t2[:, 1], c='#AED6F1', s=80, edgecolors='#1f77b4', linewidth=1.5, alpha=0.7)
ax.scatter(class2_t2[:, 0], class2_t2[:, 1], c='#F5B7B1', s=80, edgecolors='#d62728', linewidth=1.5, alpha=0.7)

# Separación final
ax = axes[3]
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('3. Salida Final\n(Linealmente separable)', fontweight='bold', fontsize=10)

# Proyección a 1D para visualizar separación
class1_final = np.zeros((30, 2))
class1_final[:, 0] = 0.2
class1_final[:, 1] = np.random.rand(30) * 0.4 + 0.05

class2_final = np.zeros((30, 2))
class2_final[:, 0] = 0.8
class2_final[:, 1] = np.random.rand(30) * 0.4 + 0.55

ax.scatter(class1_final[:, 0], class1_final[:, 1], c='#AED6F1', s=80, edgecolors='#1f77b4', linewidth=1.5, alpha=0.7)
ax.scatter(class2_final[:, 0], class2_final[:, 1], c='#F5B7B1', s=80, edgecolors='#d62728', linewidth=1.5, alpha=0.7)

# Línea separadora
ax.axvline(x=0.5, color='green', linestyle='--', linewidth=2, label='Frontera')
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig(img_dir / '23_deformacion_espacio.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 5 creada: 23_deformacion_espacio.png")
plt.close()

# ============================================================================
# IMAGEN 6: Papel del Sesgo (Bias)
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('El Papel del Sesgo (Bias)', fontsize=13, fontweight='bold', y=0.98)

# Sin sesgo
ax = axes[0]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Sin Sesgo (b=0): Limitado', fontweight='bold', fontsize=11)
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')

# Datos que requieren desplazamiento
points1 = np.random.randn(20, 2) * 0.5 + np.array([1.5, 0.5])
points2 = np.random.randn(20, 2) * 0.5 + np.array([-1.5, -0.5])

ax.scatter(points1[:, 0], points1[:, 1], c='#AED6F1', s=100, edgecolors='#1f77b4', linewidth=1.5, alpha=0.7)
ax.scatter(points2[:, 0], points2[:, 1], c='#F5B7B1', s=100, edgecolors='#d62728', linewidth=1.5, alpha=0.7)

# Línea que pasa por el origen (sin sesgo)
x_line = np.linspace(-3, 3, 100)
y_line = -0.3 * x_line  # Pasa por origen
ax.plot(x_line, y_line, 'purple', linewidth=2, linestyle=':', label='Debe pasar por (0,0)', alpha=0.7)

ax.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)
ax.legend(fontsize=9)

ax.text(0, -2.7, '❌ No puede separar bien estos datos', ha='center', fontsize=9,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5E5', alpha=0.7))

# Con sesgo
ax = axes[1]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Con Sesgo (b≠0): Flexible', fontweight='bold', fontsize=11)
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')

ax.scatter(points1[:, 0], points1[:, 1], c='#AED6F1', s=100, edgecolors='#1f77b4', linewidth=1.5, alpha=0.7)
ax.scatter(points2[:, 0], points2[:, 1], c='#F5B7B1', s=100, edgecolors='#d62728', linewidth=1.5, alpha=0.7)

# Línea con desplazamiento (con sesgo)
y_line_bias = -0.3 * x_line + 0.8  # Desplazada
ax.plot(x_line, y_line_bias, 'green', linewidth=2, linestyle='-', label='Puede desplazarse', alpha=0.7)

ax.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)
ax.legend(fontsize=9)

ax.text(0, -2.7, '✓ Separa correctamente', ha='center', fontsize=9,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#E5F5E5', alpha=0.7))

plt.tight_layout()
plt.savefig(img_dir / '24_papel_sesgo.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 6 creada: 24_papel_sesgo.png")
plt.close()

print("\n" + "="*60)
print("✅ TODAS LAS IMÁGENES DEL CAPÍTULO 4 GENERADAS")
print("="*60)
print("\nImágenes disponibles:")
print("  1. 19_red_como_funcion.png")
print("  2. 20_transformacion_lineal.png")
print("  3. 21_operaciones_elemento_elemento.png")
print("  4. 22_composicion_funciones.png")
print("  5. 23_deformacion_espacio.png")
print("  6. 24_papel_sesgo.png")
