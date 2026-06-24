"""
Script para generar imágenes ilustrativas del Capítulo 1
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

# Crear directorio para imágenes si no existe
img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

# Configuración general
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'sans-serif'

# ============================================================================
# IMAGEN 1: ML Clásico vs Redes Neuronales
# ============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Machine Learning Clásico vs Redes Neuronales', fontsize=14, fontweight='bold', y=0.98)

# ML Clásico
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('ML Clásico', fontsize=12, fontweight='bold', pad=20)

# Datos entrada
rect1 = FancyBboxPatch((0.5, 8), 2, 1, boxstyle="round,pad=0.1", 
                        edgecolor='#1f77b4', facecolor='#AED6F1', linewidth=2)
ax1.add_patch(rect1)
ax1.text(1.5, 8.5, 'Datos', ha='center', va='center', fontweight='bold')

# Feature engineering
rect2 = FancyBboxPatch((0.5, 5.5), 2, 1.5, boxstyle="round,pad=0.1",
                        edgecolor='#ff7f0e', facecolor='#F8B88B', linewidth=2)
ax1.add_patch(rect2)
ax1.text(1.5, 6.25, 'Feature\nEngineering\n(manual)', ha='center', va='center', fontweight='bold', fontsize=10)

# Algoritmo
rect3 = FancyBboxPatch((0.5, 3), 2, 1.5, boxstyle="round,pad=0.1",
                        edgecolor='#2ca02c', facecolor='#98D8C8', linewidth=2)
ax1.add_patch(rect3)
ax1.text(1.5, 3.75, 'Algoritmo\nML', ha='center', va='center', fontweight='bold')

# Predicción
rect4 = FancyBboxPatch((0.5, 0.5), 2, 1, boxstyle="round,pad=0.1",
                        edgecolor='#d62728', facecolor='#F5B7B1', linewidth=2)
ax1.add_patch(rect4)
ax1.text(1.5, 1, 'Predicción', ha='center', va='center', fontweight='bold')

# Flechas
for y_start, y_end in [(7.5, 7), (5, 4.5), (2.5, 1.5)]:
    arrow = FancyArrowPatch((1.5, y_start), (1.5, y_end),
                           arrowstyle='->', mutation_scale=30, linewidth=2, color='gray')
    ax1.add_patch(arrow)

ax1.text(3.5, 5.5, 'Ingeniero\ncrea features', ha='left', fontsize=9, style='italic', color='#d62728')

# Redes Neuronales
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Redes Neuronales', fontsize=12, fontweight='bold', pad=20)

# Datos entrada
rect1 = FancyBboxPatch((0.5, 8), 2, 1, boxstyle="round,pad=0.1",
                        edgecolor='#1f77b4', facecolor='#AED6F1', linewidth=2)
ax2.add_patch(rect1)
ax2.text(1.5, 8.5, 'Datos', ha='center', va='center', fontweight='bold')

# Representación interna
rect2 = FancyBboxPatch((0.2, 4.5), 2.6, 2.5, boxstyle="round,pad=0.1",
                        edgecolor='#9467bd', facecolor='#D7BDE2', linewidth=2)
ax2.add_patch(rect2)
ax2.text(1.5, 5.75, 'Red Neuronal\n(aprende\nrepresentaciones)', 
         ha='center', va='center', fontweight='bold', fontsize=9)

# Predicción
rect3 = FancyBboxPatch((0.5, 2), 2, 1, boxstyle="round,pad=0.1",
                        edgecolor='#d62728', facecolor='#F5B7B1', linewidth=2)
ax2.add_patch(rect3)
ax2.text(1.5, 2.5, 'Predicción', ha='center', va='center', fontweight='bold')

# Flechas
arrow1 = FancyArrowPatch((1.5, 7.5), (1.5, 7.2),
                        arrowstyle='->', mutation_scale=30, linewidth=2, color='gray')
ax2.add_patch(arrow1)
arrow2 = FancyArrowPatch((1.5, 4.2), (1.5, 3),
                        arrowstyle='->', mutation_scale=30, linewidth=2, color='gray')
ax2.add_patch(arrow2)

ax2.text(3.5, 6, 'Modelo\naprende\nauto.', ha='left', fontsize=9, style='italic', color='#d62728')

plt.tight_layout()
plt.savefig(img_dir / '01_ML_clasico_vs_RNA.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 1 creada: 01_ML_clasico_vs_RNA.png")
plt.close()

# ============================================================================
# IMAGEN 2: Redes Neuronales como subconjunto de Deep Learning
# ============================================================================

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Círculo grande para Machine Learning (fondo)
circle_ml = plt.Circle((5, 5), 4.5, color='#E8F4F8', ec='#1f77b4', linewidth=3, alpha=0.7, zorder=1)
ax.add_patch(circle_ml)
ax.text(1.5, 9, 'Machine Learning', fontsize=13, fontweight='bold', color='#1f77b4')

# Círculo medio para Redes Neuronales
circle_rn = plt.Circle((5, 5), 3, color='#E8F0F8', ec='#9467bd', linewidth=3, alpha=0.8, zorder=2)
ax.add_patch(circle_rn)
ax.text(5, 7.5, 'Redes Neuronales\nArtificiales', fontsize=11, fontweight='bold', 
        ha='center', color='#9467bd')

# Círculo pequeño para Deep Learning
circle_dl = plt.Circle((6.5, 4), 1.8, color='#FFE5CC', ec='#ff7f0e', linewidth=3, alpha=0.9, zorder=3)
ax.add_patch(circle_dl)
ax.text(6.5, 4, 'Deep\nLearning', fontsize=10, fontweight='bold', 
        ha='center', va='center', color='#ff7f0e')

# Leyenda con ejemplos
legend_y = 1.5
ax.text(0.5, legend_y, 'Ejemplos ML clásico:', fontweight='bold', fontsize=10)
ax.text(0.7, legend_y-0.4, '• Linear Regression', fontsize=9)
ax.text(0.7, legend_y-0.8, '• Decision Trees', fontsize=9)
ax.text(0.7, legend_y-1.2, '• Random Forest, SVM', fontsize=9)

ax.text(5.5, legend_y, 'Ejemplos RNA:', fontweight='bold', fontsize=10)
ax.text(5.7, legend_y-0.4, '• Perceptrón', fontsize=9)
ax.text(5.7, legend_y-0.8, '• MLP (Multilayer)', fontsize=9)

ax.text(5.5, legend_y-1.8, 'Ejemplos DL:', fontweight='bold', fontsize=10)
ax.text(5.7, legend_y-2.2, '• CNN', fontsize=9)
ax.text(5.7, legend_y-2.6, '• RNN, LSTM', fontsize=9)
ax.text(5.7, legend_y-3, '• Transformers', fontsize=9)

plt.tight_layout()
plt.savefig(img_dir / '02_RNA_vs_DeepLearning.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 2 creada: 02_RNA_vs_DeepLearning.png")
plt.close()

# ============================================================================
# IMAGEN 3: Arquitectura simple de una Red Neuronal
# ============================================================================

fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 8)
ax.axis('off')
ax.set_title('Estructura de una Red Neuronal Simple (MLP)', fontsize=13, fontweight='bold', pad=20)

# Capas
layer_positions = [1, 4.5, 8]
layer_names = ['Capa de\nEntrada\n(Input)', 'Capa\nOculta\n(Hidden)', 'Capa de\nSalida\n(Output)']
neurons_per_layer = [3, 4, 2]
colors = ['#AED6F1', '#98D8C8', '#F8B88B']

# Dibujar neuronas
neuron_positions = {}
for layer_idx, (x, name, n_neurons, color) in enumerate(zip(layer_positions, layer_names, neurons_per_layer, colors)):
    # Título de capa
    ax.text(x, 7.5, name, ha='center', fontweight='bold', fontsize=10)
    
    # Neuronas
    y_spacing = 6 / (n_neurons - 1) if n_neurons > 1 else 3
    y_start = 6 - (n_neurons - 1) * y_spacing / 2
    
    positions = []
    for i in range(n_neurons):
        y = y_start + i * y_spacing
        circle = plt.Circle((x, y), 0.35, color=color, ec='black', linewidth=2, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, str(i+1), ha='center', va='center', fontweight='bold', fontsize=9)
        positions.append((x, y))
    
    neuron_positions[layer_idx] = positions

# Conexiones (pesos/weights)
for layer1_idx in range(len(neuron_positions) - 1):
    layer1_neurons = neuron_positions[layer1_idx]
    layer2_neurons = neuron_positions[layer1_idx + 1]
    
    for (x1, y1) in layer1_neurons:
        for (x2, y2) in layer2_neurons:
            ax.plot([x1 + 0.35, x2 - 0.35], [y1, y2], 'gray', linewidth=0.8, alpha=0.5, zorder=1)

# Anotaciones
ax.text(2.75, -0.3, 'Pesos (w)', ha='center', fontsize=9, style='italic', color='gray')
ax.text(6.25, -0.3, 'Pesos (w)', ha='center', fontsize=9, style='italic', color='gray')

# Flecha de dirección
arrow = FancyArrowPatch((0.2, -0.7), (9.8, -0.7),
                       arrowstyle='->', mutation_scale=30, linewidth=2.5, color='#d62728')
ax.add_patch(arrow)
ax.text(5, -0.85, 'Dirección de cálculo (Forward Pass)', ha='center', fontsize=9, color='#d62728', fontweight='bold')

plt.tight_layout()
plt.savefig(img_dir / '03_arquitectura_RNA_simple.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 3 creada: 03_arquitectura_RNA_simple.png")
plt.close()

# ============================================================================
# IMAGEN 4: Proceso de entrenamiento (iterativo)
# ============================================================================

fig, ax = plt.subplots(figsize=(11, 7))
ax.set_xlim(0, 11)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Proceso de Entrenamiento de una Red Neuronal', fontsize=13, fontweight='bold', pad=20)

# Cajas del ciclo
steps = [
    ('1. Forward Pass\n(Predicción)', 2, 7, '#AED6F1'),
    ('2. Cálculo de\nPérdida', 5, 7, '#F8B88B'),
    ('3. Backpropagation\n(Gradientes)', 8, 7, '#D7BDE2'),
    ('4. Actualización\nPesos', 5, 3, '#98D8C8'),
]

box_width = 1.8
box_height = 1.2

for label, x, y, color in steps:
    rect = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                         boxstyle="round,pad=0.1", edgecolor='black', 
                         facecolor=color, linewidth=2, zorder=2)
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center', fontweight='bold', fontsize=9)

# Flechas del ciclo
arrows = [
    ((2 + box_width/2, 7), (5 - box_width/2, 7)),      # 1 -> 2
    ((5 + box_width/2, 7), (8 - box_width/2, 7)),      # 2 -> 3
    ((8, 7 - box_height/2), (6, 3 + box_height/2)),   # 3 -> 4
    ((4, 3), (2, 7 - box_height/2)),                    # 4 -> 1
]

for (x1, y1), (x2, y2) in arrows:
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25, linewidth=2.5, color='#d62728', zorder=1)
    ax.add_patch(arrow)

# Anotaciones
ax.text(0.3, 7, '📊\nDatos', ha='center', va='center', fontsize=10)
ax.text(10.7, 7, '✓\nResultado', ha='center', va='center', fontsize=10)

# Nota sobre iteraciones
ax.text(5, 1, 'Este ciclo se repite múltiples veces (épocas) hasta que el modelo converge', 
        ha='center', fontsize=10, style='italic', 
        bbox=dict(boxstyle='round', facecolor='#FFFFCC', alpha=0.7, pad=0.5))

# Recuadro explicativo
explanation = (
    "Clave: El modelo aprende ajustando automáticamente sus pesos\n"
    "mediante el cálculo de derivadas (gradientes)"
)
ax.text(5, 9, explanation, ha='center', fontsize=9,
        bbox=dict(boxstyle='round', facecolor='#E8F4F8', alpha=0.9, pad=0.7),
        color='#1f77b4', fontweight='bold')

plt.tight_layout()
plt.savefig(img_dir / '04_proceso_entrenamiento.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 4 creada: 04_proceso_entrenamiento.png")
plt.close()

# ============================================================================
# IMAGEN 5: Comparación: Características manualmente diseñadas vs Aprendidas
# ============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Aprendizaje de Características: ML Clásico vs Redes Neuronales', 
             fontsize=13, fontweight='bold', y=0.98)

# ML Clásico - Características manuales
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('ML Clásico: Diseño Manual', fontsize=11, fontweight='bold', pad=15)

boxes1 = [
    ('Datos\nCrudos', 1.5, 8.5, '#AED6F1'),
    ('Feature 1\n(media)', 1.5, 6.5, '#FFE5CC'),
    ('Feature 2\n(desv std)', 1.5, 5, '#FFE5CC'),
    ('Feature 3\n(max-min)', 1.5, 3.5, '#FFE5CC'),
    ('Modelo ML\n(SVM, RF...)', 1.5, 1.5, '#98D8C8'),
]

for label, x, y, color in boxes1:
    rect = FancyBboxPatch((x-0.9, y-0.5), 1.8, 1, boxstyle="round,pad=0.05",
                         edgecolor='black', facecolor=color, linewidth=1.5)
    ax1.add_patch(rect)
    ax1.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold')

# Flechas
for y1, y2 in [(7.5, 7), (6, 5.5), (4.5, 4), (3, 2)]:
    arrow = FancyArrowPatch((1.5, y1), (1.5, y2),
                           arrowstyle='->', mutation_scale=20, linewidth=1.5, color='gray')
    ax1.add_patch(arrow)

ax1.text(3.2, 5, 'Ingeniero decide\nqué features\nson relevantes', 
         fontsize=8, style='italic', color='#d62728')

# Redes Neuronales - Características aprendidas
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Redes Neuronales: Aprendizaje Automático', fontsize=11, fontweight='bold', pad=15)

boxes2 = [
    ('Datos\nCrudos', 1.5, 8.5, '#AED6F1'),
    ('Capa 1\n(Repr. 1)', 1.5, 6.8, '#D7BDE2'),
    ('Capa 2\n(Repr. 2)', 1.5, 5.2, '#D7BDE2'),
    ('Capa 3\n(Repr. 3)', 1.5, 3.6, '#D7BDE2'),
    ('Salida\n(Pred.)', 1.5, 1.5, '#98D8C8'),
]

for label, x, y, color in boxes2:
    rect = FancyBboxPatch((x-0.9, y-0.5), 1.8, 1, boxstyle="round,pad=0.05",
                         edgecolor='black', facecolor=color, linewidth=1.5)
    ax2.add_patch(rect)
    ax2.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold')

# Flechas
for y1, y2 in [(7.5, 7.3), (6.3, 5.7), (4.7, 4.1), (3.1, 2)]:
    arrow = FancyArrowPatch((1.5, y1), (1.5, y2),
                           arrowstyle='->', mutation_scale=20, linewidth=1.5, color='gray')
    ax2.add_patch(arrow)

ax2.text(3.2, 5, 'Red aprende\nrepresentaciones\nintermediatas', 
         fontsize=8, style='italic', color='#d62728')

plt.tight_layout()
plt.savefig(img_dir / '05_caracteristicas_manual_vs_aprendidas.png', dpi=300, bbox_inches='tight')
print("✓ Imagen 5 creada: 05_caracteristicas_manual_vs_aprendidas.png")
plt.close()

print("\n" + "="*60)
print("✅ TODAS LAS IMÁGENES GENERADAS CORRECTAMENTE")
print("="*60)
print("\nImágenes disponibles en la carpeta 'images/':")
print("  1. 01_ML_clasico_vs_RNA.png")
print("  2. 02_RNA_vs_DeepLearning.png")
print("  3. 03_arquitectura_RNA_simple.png")
print("  4. 04_proceso_entrenamiento.png")
print("  5. 05_caracteristicas_manual_vs_aprendidas.png")
