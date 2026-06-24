"""
Script para generar imágenes ilustrativas del Capítulo 2
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np
from pathlib import Path

# Crear directorio para imágenes si no existe
img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

# Configuración general
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

# ============================================================================
# IMAGEN 1: Neurona Artificial - Estructura
# ============================================================================

fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(-0.5, 12)
ax.set_ylim(-0.5, 7)
ax.axis('off')
ax.set_title('Estructura de una Neurona Artificial', fontsize=13, fontweight='bold', pad=20)

# Entradas (lado izquierdo)
n_inputs = 3
y_positions = np.linspace(5, 1, n_inputs)

for i, y in enumerate(y_positions):
    # Círculo entrada
    circle = Circle((1, y), 0.25, color='#AED6F1', ec='black', linewidth=1.5, zorder=3)
    ax.add_patch(circle)
    ax.text(1, y, f'x{i+1}', ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Etiqueta entrada
    ax.text(0.3, y, f'x{i+1}', ha='right', va='center', fontsize=9)

# Neurona (centro)
neuron_circle = Circle((4.5, 3), 0.6, color='#D7BDE2', ec='black', linewidth=2.5, zorder=3)
ax.add_patch(neuron_circle)
ax.text(4.5, 3.3, 'Σ', ha='center', va='center', fontsize=16, fontweight='bold')

# Conexiones entrada -> neurona con pesos
for i, y in enumerate(y_positions):
    # Línea
    ax.plot([1.25, 3.9], [y, 3], 'gray', linewidth=1.5, alpha=0.6, zorder=1)
    # Etiqueta peso
    mid_x, mid_y = 2.55, (y + 3) / 2
    ax.text(mid_x, mid_y + 0.35, f'w{i+1}', ha='center', fontsize=8, 
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5CC', alpha=0.8))

# Sesgo (bias)
bias_circle = Circle((2.5, 0.2), 0.2, color='#F8B88B', ec='black', linewidth=1.5, zorder=3)
ax.add_patch(bias_circle)
ax.text(2.5, 0.2, 'b', ha='center', va='center', fontsize=8, fontweight='bold')
ax.plot([2.7, 3.95], [0.2, 2.7], 'gray', linewidth=1.5, alpha=0.6, zorder=1)

# Función de activación (zona de procesamiento)
ax.text(4.5, 1.5, 'σ(w·x + b)', ha='center', fontsize=8, style='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFFFCC', alpha=0.7))

# Flecha y salida
arrow = FancyArrowPatch((5.2, 3), (6.5, 3),
                       arrowstyle='->', mutation_scale=25, linewidth=2, color='#d62728')
ax.add_patch(arrow)

output_circle = Circle((7.5, 3), 0.35, color='#98D8C8', ec='black', linewidth=1.5, zorder=3)
ax.add_patch(output_circle)
ax.text(7.5, 3, 'y', ha='center', va='center', fontsize=9, fontweight='bold')

# Explicación de fórmula
formula_text = r'$y = \sigma(w_1 x_1 + w_2 x_2 + w_3 x_3 + b)$'
ax.text(6, 0.5, formula_text, ha='center', fontsize=11,
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#E8F4F8', alpha=0.9))

# Leyenda
legend_elements = [
    mpatches.Patch(facecolor='#AED6F1', edgecolor='black', label='Entrada (x)'),
    mpatches.Patch(facecolor='#D7BDE2', edgecolor='black', label='Suma ponderada'),
    mpatches.Patch(facecolor='#98D8C8', edgecolor='black', label='Salida (y)'),
    mpatches.Patch(facecolor='#F8B88B', edgecolor='black', label='Sesgo (bias)'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig(img_dir / '06_neurona_artificial_estructura.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 1 creada: 06_neurona_artificial_estructura.png")
plt.close()

# ============================================================================
# IMAGEN 2: Funciones de Activación
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Funciones de Activación Comunes', fontsize=13, fontweight='bold', y=0.995)

x = np.linspace(-5, 5, 300)

# ReLU
ax = axes[0, 0]
y_relu = np.maximum(0, x)
ax.plot(x, y_relu, linewidth=2.5, color='#1f77b4', label='ReLU(x) = max(0, x)')
ax.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)
ax.grid(True, alpha=0.3)
ax.set_title('ReLU (Rectified Linear Unit)', fontweight='bold', fontsize=11)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(fontsize=9)
ax.set_ylim(-0.5, 5.5)

# Sigmoid
ax = axes[0, 1]
y_sigmoid = 1 / (1 + np.exp(-x))
ax.plot(x, y_sigmoid, linewidth=2.5, color='#ff7f0e', label='σ(x) = 1/(1+e^(-x))')
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)
ax.grid(True, alpha=0.3)
ax.set_title('Sigmoid', fontweight='bold', fontsize=11)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylim(-0.1, 1.1)
ax.legend(fontsize=9)

# Tanh
ax = axes[1, 0]
y_tanh = np.tanh(x)
ax.plot(x, y_tanh, linewidth=2.5, color='#2ca02c', label='tanh(x)')
ax.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)
ax.grid(True, alpha=0.3)
ax.set_title('Tanh (Tangente Hiperbólica)', fontweight='bold', fontsize=11)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylim(-1.1, 1.1)
ax.legend(fontsize=9)

# Comparación
ax = axes[1, 1]
ax.plot(x, y_relu / 5, linewidth=2.5, color='#1f77b4', label='ReLU (normalizado)')
ax.plot(x, y_sigmoid, linewidth=2.5, color='#ff7f0e', label='Sigmoid')
ax.plot(x, y_tanh, linewidth=2.5, color='#2ca02c', label='Tanh')
ax.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.3)
ax.grid(True, alpha=0.3)
ax.set_title('Comparación', fontweight='bold', fontsize=11)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig(img_dir / '07_funciones_activacion.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 2 creada: 07_funciones_activacion.png")
plt.close()

# ============================================================================
# IMAGEN 3: Capas de una Red Neuronal
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(-0.5, 14.5)
ax.set_ylim(-1, 8)
ax.axis('off')
ax.set_title('Capas de una Red Neuronal (Organización)', fontsize=13, fontweight='bold', pad=20)

# Capas
layer_info = [
    ('Capa de\nEntrada\n(Input)', 2, 3, '#AED6F1', '5 variables'),
    ('Capa\nOculta 1\n(Hidden)', 6, 4, '#D7BDE2', '8 neuronas'),
    ('Capa\nOculta 2\n(Hidden)', 10, 3, '#D7BDE2', '4 neuronas'),
    ('Capa de\nSalida\n(Output)', 13, 2, '#98D8C8', '2 clases')
]

neuron_configs = [3, 4, 3, 2]  # neuronas por capa para visualización
x_positions = [2, 6, 10, 13]

for layer_idx, (title, x, n_neurons_vis, color, description) in enumerate(layer_info):
    # Título capa
    ax.text(x, 7.3, title, ha='center', fontweight='bold', fontsize=10)
    ax.text(x, 6.8, description, ha='center', fontsize=8, style='italic', color='gray')
    
    # Neuronas
    y_spacing = 4 / (n_neurons_vis - 1) if n_neurons_vis > 1 else 2
    y_start = 3 - (n_neurons_vis - 1) * y_spacing / 2
    
    for i in range(n_neurons_vis):
        y = y_start + i * y_spacing
        circle = Circle((x, y), 0.28, color=color, ec='black', linewidth=1.5, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, str(i+1), ha='center', va='center', fontsize=7, fontweight='bold')

# Conexiones entre capas
for layer_idx in range(len(x_positions) - 1):
    x1, x2 = x_positions[layer_idx], x_positions[layer_idx + 1]
    n1, n2 = neuron_configs[layer_idx], neuron_configs[layer_idx + 1]
    
    y_start1 = 3 - (n1 - 1) * (4 / (n1 - 1)) / 2 if n1 > 1 else 3
    y_start2 = 3 - (n2 - 1) * (4 / (n2 - 1)) / 2 if n2 > 1 else 3
    
    spacing1 = 4 / (n1 - 1) if n1 > 1 else 0
    spacing2 = 4 / (n2 - 1) if n2 > 1 else 0
    
    # Solo conectar algunas líneas para claridad
    for i in range(min(n1, 3)):
        for j in range(min(n2, 3)):
            y1 = y_start1 + i * spacing1
            y2 = y_start2 + j * spacing2
            ax.plot([x1 + 0.28, x2 - 0.28], [y1, y2], 'gray', linewidth=0.5, alpha=0.4, zorder=1)

# Anotaciones
ax.text(4, 0.2, 'Pesos (w)\ny Sesgos (b)', ha='center', fontsize=8, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5CC', alpha=0.7))
ax.text(8, 0.2, 'Pesos (w)\ny Sesgos (b)', ha='center', fontsize=8, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5CC', alpha=0.7))
ax.text(11.5, 0.2, 'Pesos (w)\ny Sesgos (b)', ha='center', fontsize=8, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5CC', alpha=0.7))

# Flecha de dirección
arrow = FancyArrowPatch((0.5, -0.5), (13.5, -0.5),
                       arrowstyle='->', mutation_scale=30, linewidth=2.5, color='#d62728')
ax.add_patch(arrow)
ax.text(7, -0.75, 'Flujo de información (Forward Pass)', ha='center', fontsize=9, 
        color='#d62728', fontweight='bold')

plt.tight_layout()
plt.savefig(img_dir / '08_capas_red_neuronal.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 3 creada: 08_capas_red_neuronal.png")
plt.close()

# ============================================================================
# IMAGEN 4: Redes Feedforward vs Otras
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle('Redes Feedforward (Perceptrón Multicapa)', fontsize=13, fontweight='bold', y=0.98)

# Feedforward
ax = axes[0]
ax.set_xlim(-0.5, 6)
ax.set_ylim(-0.5, 6)
ax.axis('off')
ax.set_title('Feedforward (Sin ciclos)', fontsize=11, fontweight='bold', pad=15)

# Capas
x_pos = [1, 3, 5]
layer_sizes = [3, 4, 2]

for layer_idx, (x, n) in enumerate(zip(x_pos, layer_sizes)):
    y_spacing = 4 / (n - 1) if n > 1 else 2.5
    y_start = 2.5 - (n - 1) * y_spacing / 2
    
    for i in range(n):
        y = y_start + i * y_spacing
        circle = Circle((x, y), 0.25, color='#AED6F1', ec='black', linewidth=1.5, zorder=3)
        ax.add_patch(circle)

# Conexiones (solo hacia adelante)
for i in range(len(x_pos) - 1):
    for j in range(layer_sizes[i]):
        for k in range(layer_sizes[i + 1]):
            y1 = 2.5 - (layer_sizes[i] - 1) * 4 / (layer_sizes[i] - 1) / 2 + j * 4 / (layer_sizes[i] - 1) if layer_sizes[i] > 1 else 2.5
            y2 = 2.5 - (layer_sizes[i + 1] - 1) * 4 / (layer_sizes[i + 1] - 1) / 2 + k * 4 / (layer_sizes[i + 1] - 1) if layer_sizes[i + 1] > 1 else 2.5
            ax.plot([x_pos[i] + 0.25, x_pos[i + 1] - 0.25], [y1, y2], 
                   'green', linewidth=1, alpha=0.5, zorder=1)

# Flecha de dirección
arrow = FancyArrowPatch((0.5, -0.2), (5.5, -0.2),
                       arrowstyle='->', mutation_scale=25, linewidth=2.5, color='green')
ax.add_patch(arrow)
ax.text(3, -0.4, 'Información hacia adelante', ha='center', fontsize=9, color='green', fontweight='bold')

# Con ciclos (conceptual)
ax = axes[1]
ax.set_xlim(-0.5, 6)
ax.set_ylim(-0.5, 6)
ax.axis('off')
ax.set_title('Con ciclos (RNN - No estudiamos aún)', fontsize=11, fontweight='bold', pad=15)

# Capas más simples
x_pos_rnn = [1.5, 4.5]
layer_sizes_rnn = [3, 3]

for layer_idx, (x, n) in enumerate(zip(x_pos_rnn, layer_sizes_rnn)):
    y_spacing = 4 / (n - 1) if n > 1 else 2.5
    y_start = 2.5 - (n - 1) * y_spacing / 2
    
    for i in range(n):
        y = y_start + i * y_spacing
        circle = Circle((x, y), 0.25, color='#D7BDE2', ec='black', linewidth=1.5, zorder=3)
        ax.add_patch(circle)

# Conexiones adelante
for j in range(3):
    for k in range(3):
        y1 = 2.5 - 2 * 4 / 2 + j * 4 / 2
        y2 = 2.5 - 2 * 4 / 2 + k * 4 / 2
        ax.plot([1.75, 4.25], [y1, y2], 'orange', linewidth=1, alpha=0.5, zorder=1)

# Conexiones atrás (ciclos)
for j in range(3):
    for k in range(3):
        y1 = 2.5 - 2 * 4 / 2 + j * 4 / 2
        y2 = 2.5 - 2 * 4 / 2 + k * 4 / 2
        # Arco hacia atrás
        from matplotlib.patches import Arc
        angle = np.degrees(np.arctan2(y2 - y1, 1.75 - 4.25))
        arc = Arc((3, 2.5), 3, 4, angle=0, theta1=180, theta2=360, 
                 color='red', linewidth=1, alpha=0.3)
        ax.add_patch(arc)

# Flechas adelante y atrás
arrow1 = FancyArrowPatch((1.75, -0.2), (4.25, -0.2),
                        arrowstyle='->', mutation_scale=20, linewidth=2, color='orange')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((4.25, 0), (1.75, 0),
                        arrowstyle='->', mutation_scale=20, linewidth=2, color='red')
ax.add_patch(arrow2)

ax.text(3, -0.5, 'Información también hacia atrás (ciclos)', ha='center', 
       fontsize=8, color='red', fontweight='bold')

plt.tight_layout()
plt.savefig(img_dir / '09_feedforward_vs_ciclos.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 4 creada: 09_feedforward_vs_ciclos.png")
plt.close()

# ============================================================================
# IMAGEN 5: Transformación Geométrica - Una capa deforma el espacio
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Cómo una Capa Neuronal Deforma el Espacio de Datos', 
             fontsize=13, fontweight='bold', y=0.98)

# Datos originales (punto 2D)
ax = axes[0]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('1. Datos Originales', fontweight='bold', fontsize=11)
ax.set_xlabel('Variable 1')
ax.set_ylabel('Variable 2')

# Dos clases separables
np.random.seed(42)
class1_x = np.random.randn(30) - 1.2
class1_y = np.random.randn(30) - 1.2
class2_x = np.random.randn(30) + 1.2
class2_y = np.random.randn(30) + 1.2

ax.scatter(class1_x, class1_y, c='#AED6F1', s=100, edgecolors='#1f77b4', 
          linewidth=1.5, label='Clase 1', alpha=0.7)
ax.scatter(class2_x, class2_y, c='#F5B7B1', s=100, edgecolors='#d62728',
          linewidth=1.5, label='Clase 2', alpha=0.7)
ax.legend(fontsize=9)

# Después de transformación lineal
ax = axes[1]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('2. Después de Transformación Lineal\n(rotación, escala)', 
            fontweight='bold', fontsize=11)
ax.set_xlabel('Nueva variable 1')
ax.set_ylabel('Nueva variable 2')

# Rotación y escala
angle = np.pi / 6  # 30 grados
rot_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                       [np.sin(angle), np.cos(angle)]])

class1_transformed = np.column_stack([class1_x, class1_y]) @ rot_matrix.T * 0.8
class2_transformed = np.column_stack([class2_x, class2_y]) @ rot_matrix.T * 0.8

ax.scatter(class1_transformed[:, 0], class1_transformed[:, 1], c='#AED6F1', 
          s=100, edgecolors='#1f77b4', linewidth=1.5, label='Clase 1', alpha=0.7)
ax.scatter(class2_transformed[:, 0], class2_transformed[:, 1], c='#F5B7B1',
          s=100, edgecolors='#d62728', linewidth=1.5, label='Clase 2', alpha=0.7)
ax.legend(fontsize=9)

# Después de activación no lineal
ax = axes[2]
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('3. Después de Función de Activación\n(no linealidad)', 
            fontweight='bold', fontsize=11)
ax.set_xlabel('Representación nueva')
ax.set_ylabel('Representación nueva')

# Aplicar ReLU y normalizar
class1_relu = np.maximum(class1_transformed, 0)
class2_relu = np.maximum(class2_transformed, 0)

# Normalizar a [0, 1]
class1_relu_norm = (class1_relu - class1_relu.min(axis=0)) / (class1_relu.max(axis=0) - class1_relu.min(axis=0) + 0.01)
class2_relu_norm = (class2_relu - class2_relu.min(axis=0)) / (class2_relu.max(axis=0) - class2_relu.min(axis=0) + 0.01)

ax.scatter(class1_relu_norm[:, 0], class1_relu_norm[:, 1], c='#AED6F1',
          s=100, edgecolors='#1f77b4', linewidth=1.5, label='Clase 1', alpha=0.7)
ax.scatter(class2_relu_norm[:, 0], class2_relu_norm[:, 1], c='#F5B7B1',
          s=100, edgecolors='#d62728', linewidth=1.5, label='Clase 2', alpha=0.7)

# Línea separadora conceptual
x_sep = np.linspace(0, 1, 100)
y_sep = 0.5 * x_sep + 0.2
ax.plot(x_sep, y_sep, 'g--', linewidth=2, label='Frontera separadora', alpha=0.7)

ax.legend(fontsize=9)
ax.text(0.5, -0.15, 'Datos mucho más separables', ha='center', fontsize=9, 
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFCC', alpha=0.7))

plt.tight_layout()
plt.savefig(img_dir / '10_transformacion_geometrica.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 5 creada: 10_transformacion_geometrica.png")
plt.close()

# ============================================================================
# IMAGEN 6: Jerarquía de Capas - Patrones a Abstracciones
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Jerarquía de Capas: Patrones Simples a Complejos', 
            fontsize=13, fontweight='bold', pad=20)

# Columnas para cada nivel
levels = [
    {
        'title': 'Entrada',
        'items': ['Píxel 1', 'Píxel 2', 'Píxel 3', '...'],
        'x': 2,
        'color': '#AED6F1',
        'desc': 'Datos crudos'
    },
    {
        'title': 'Capa 1',
        'items': ['Bordes', 'Ángulos', 'Líneas', 'Texturas'],
        'x': 5,
        'color': '#D7BDE2',
        'desc': 'Patrones simples'
    },
    {
        'title': 'Capa 2',
        'items': ['Formas', 'Partes', 'Objetos\nsimples'],
        'x': 8.5,
        'color': '#D7BDE2',
        'desc': 'Combinaciones'
    },
    {
        'title': 'Capa 3',
        'items': ['Rostro', 'Auto', 'Gato'],
        'x': 12,
        'color': '#98D8C8',
        'desc': 'Abstracciones'
    }
]

for level in levels:
    x = level['x']
    
    # Título
    ax.text(x, 9.2, level['title'], ha='center', fontweight='bold', fontsize=11)
    ax.text(x, 8.8, level['desc'], ha='center', fontsize=8, style='italic', color='gray')
    
    # Cajas para items
    n_items = len(level['items'])
    y_spacing = 5 / (n_items - 1) if n_items > 1 else 2.5
    y_start = 6 - (n_items - 1) * y_spacing / 2
    
    for i, item in enumerate(level['items']):
        y = y_start + i * y_spacing
        rect = FancyBboxPatch((x - 0.7, y - 0.35), 1.4, 0.7,
                             boxstyle='round,pad=0.05', 
                             edgecolor='black', facecolor=level['color'],
                             linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, y, item, ha='center', va='center', fontsize=8, fontweight='bold')

# Flechas entre niveles mostrando flujo
for i in range(len(levels) - 1):
    x1 = levels[i]['x'] + 0.7
    x2 = levels[i + 1]['x'] - 0.7
    arrow = FancyArrowPatch((x1, 5), (x2, 5),
                           arrowstyle='->', mutation_scale=30, linewidth=2.5, 
                           color='#d62728', alpha=0.7)
    ax.add_patch(arrow)

# Explicación
explanation = (
    "Primera capa detecta patrones simples (bordes, líneas)\n"
    "Capas intermedias combinan estos patrones en estructuras\n"
    "Últimas capas aprenden conceptos abstractos complejos"
)
ax.text(7, 1.5, explanation, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFFCC', alpha=0.8))

# Nota sobre profundidad
ax.text(7, 0.3, 'Esto es por qué agregar más capas aumenta el poder expresivo del modelo',
       ha='center', fontsize=9, style='italic',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8F4F8', alpha=0.8))

plt.tight_layout()
plt.savefig(img_dir / '11_jerarquia_capas.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 6 creada: 11_jerarquia_capas.png")
plt.close()

# ============================================================================
# IMAGEN 7: Pesos y Sesgo - Intuición Geométrica
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Intuición Geométrica: Pesos y Sesgo', fontsize=13, fontweight='bold', y=0.98)

# Pesos - Orientación del hiperplano
ax = axes[0]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Pesos: Orientación del Hiperplano', fontweight='bold', fontsize=11)
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')

# Puntos
ax.scatter([1, 2, 1.5], [1, 2, 1.5], c='#AED6F1', s=150, edgecolors='#1f77b4', linewidth=2)
ax.scatter([-1, -2, -1.5], [-1, -2, -1.5], c='#F5B7B1', s=150, edgecolors='#d62728', linewidth=2)

# Línea separadora (influida por pesos)
x_line = np.linspace(-3, 3, 100)
# Con diferentes pesos (pendientes diferentes)
y_line1 = 1 * x_line  # pendiente 1
y_line2 = 0.5 * x_line  # pendiente 0.5

ax.plot(x_line, y_line1, 'g-', linewidth=2.5, label='w₁=1, w₂=1 (45°)', alpha=0.7)
ax.plot(x_line, y_line2, 'orange', linewidth=2.5, linestyle='--', label='w₁=1, w₂=0.5 (27°)', alpha=0.7)

ax.legend(fontsize=9)
ax.text(-2.8, -2.8, 'Pesos cambian\nla inclinación', fontsize=9,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5CC', alpha=0.7))

# Sesgo - Desplazamiento
ax = axes[1]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Sesgo (Bias): Desplazamiento del Hiperplano', fontweight='bold', fontsize=11)
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')

# Puntos
ax.scatter([1, 2, 1.5], [1, 2, 1.5], c='#AED6F1', s=150, edgecolors='#1f77b4', linewidth=2)
ax.scatter([-1, -2, -1.5], [-1, -2, -1.5], c='#F5B7B1', s=150, edgecolors='#d62728', linewidth=2)

# Línea separadora (influida por sesgo)
x_line = np.linspace(-3, 3, 100)
y_line1 = x_line  # b = 0
y_line2 = x_line + 0.5  # b = 0.5
y_line3 = x_line - 0.5  # b = -0.5

ax.plot(x_line, y_line1, 'g-', linewidth=2.5, label='b = 0', alpha=0.7)
ax.plot(x_line, y_line2, 'blue', linewidth=2.5, linestyle='--', label='b = +0.5', alpha=0.7)
ax.plot(x_line, y_line3, 'purple', linewidth=2.5, linestyle=':', label='b = -0.5', alpha=0.7)

ax.legend(fontsize=9)
ax.text(-2.8, -2.8, 'Sesgo desplaza\nla línea', fontsize=9,
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5CC', alpha=0.7))

plt.tight_layout()
plt.savefig(img_dir / '12_pesos_sesgo_geometria.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 7 creada: 12_pesos_sesgo_geometria.png")
plt.close()

print("\n" + "="*60)
print("✅ TODAS LAS IMÁGENES DEL CAPÍTULO 2 GENERADAS")
print("="*60)
print("\nImágenes disponibles:")
print("  1. 06_neurona_artificial_estructura.png")
print("  2. 07_funciones_activacion.png")
print("  3. 08_capas_red_neuronal.png")
print("  4. 09_feedforward_vs_ciclos.png")
print("  5. 10_transformacion_geometrica.png")
print("  6. 11_jerarquia_capas.png")
print("  7. 12_pesos_sesgo_geometria.png")
