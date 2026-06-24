import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrowPatch

# Parámetros
learning_rate = 0.1 + np.random.rand() * 0.2
num_iterations = 50
stop_tolerance = 1e-2
show_path = True
frame_interval_ms = 900

# Función cuadrática con perturbaciones
pert_a = 0.6
pert_b = 3.0
pert_c = 0.3
pert_d = 1.0

def f(x):
    return x**2 + pert_a * np.sin(pert_b * x) + pert_c * np.sin(pert_d * x)

# Derivada de la función
def df(x):
    return 2 * x + pert_a * pert_b * np.cos(pert_b * x) + pert_c * pert_d * np.cos(pert_d * x)

# Inicialización
x = np.linspace(-3, 3, 100)

# Puntos iniciales
x0 = 2.0

# Configuración de la figura
fig, ax = plt.subplots()
line, = ax.plot(x, f(x), label='f(x)')
point, = ax.plot([], [], 'ro')
path_line, = ax.plot([], [], 'r-', alpha=0.5, lw=1)
path_points, = ax.plot([], [], 'ro', ms=4, alpha=0.6)
line_tangent, = ax.plot([], [], 'g--', label='Tangente')

arrow_derivative = FancyArrowPatch((0, 0), (0, 0),
                                   color='blue', mutation_scale=15, lw=2)
arrow_descent = FancyArrowPatch((0, 0), (0, 0),
                                color='orange', mutation_scale=15, lw=2)
ax.add_patch(arrow_derivative)
ax.add_patch(arrow_descent)

ax.set_xlim(-3, 3)
ax.set_ylim(-1, 10)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.legend()
lr_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, ha='left', va='top')

# Función de inicialización para la animación
def init():
    point.set_data([], [])
    path_line.set_data([], [])
    path_points.set_data([], [])
    line_tangent.set_data([], [])
    arrow_derivative.set_positions((0, 0), (0, 0))
    arrow_descent.set_positions((0, 0), (0, 0))
    lr_text.set_text(f'lr = {learning_rate:.3f}')
    return point, path_line, path_points, line_tangent, arrow_derivative, arrow_descent, lr_text

# Función de actualización para la animación
history_x = []
history_y = []

def update(frame):
    global x0
    # Calcular la función y la derivada en el punto actual
    y0 = float(f(x0))
    slope = float(df(x0))
    if abs(slope) <= stop_tolerance or x0 < ax.get_xlim()[0] or x0 > ax.get_xlim()[1]:
        if 'ani' in globals():
            ani.event_source.stop()
        return point, path_line, path_points, line_tangent, arrow_derivative, arrow_descent, lr_text
    # Actualizar la posición del punto
    point.set_data(x0, y0)
    history_x.append(x0)
    history_y.append(y0)
    if show_path:
        path_line.set_data(history_x, history_y)
        path_points.set_data(history_x, history_y)
    else:
        path_line.set_data([], [])
        path_points.set_data([], [])
    # Calcular la recta tangente
    tangent_x = np.array([x0 - 0.5, x0 + 0.5])
    tangent_y = y0 + slope * (tangent_x - x0)
    line_tangent.set_data(tangent_x, tangent_y)
    # Flechas de derivada y descenso
    sign = 1.0 if slope >= 0 else -1.0
    direction = np.array([1.0, slope]) * sign
    direction /= np.linalg.norm(direction)
    arrow_len = 0.8
    start = np.array([x0, y0])
    end_deriv = start + arrow_len * direction
    end_descent = start - arrow_len * direction
    arrow_derivative.set_positions(start, end_deriv)
    arrow_descent.set_positions(start, end_descent)
    # Actualizar el punto para el siguiente paso
    x0 -= learning_rate * slope
    return point, path_line, path_points, line_tangent, arrow_derivative, arrow_descent, lr_text

# Crear la animación
ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_iterations,
    init_func=init,
    blit=True,
    interval=frame_interval_ms
)
plt.show()