import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import matplotlib.cm as cm

def bezier_curve(points, n=100):
    # calcula uma curva Bézier cúbica para 4 pontos de controle
    t = np.linspace(0, 1, n)
    t = t.reshape(-1, 1)  # Corrige o shape para broadcasting correto
    curve = ((1 - t)**3) * points[0] + 3 * ((1 - t)**2) * t * points[1] + 3 * (1 - t) * (t**2) * points[2] + (t**3) * points[3]
    return curve

def random_fluid_shape(offset=0):
    # cria uma forma fluida abstrata com curvas Bézier
    shapes = []
    base_x = np.linspace(-1, 1, 4)
    base_y = np.array([0.0, 0.5, -0.5, 0.0]) + offset
    
    for i in range(3):
        points = np.array([
            [base_x[i], base_y[i]],
            [base_x[i] + 0.3*np.sin(i*5 + offset*3), base_y[i] + 0.5*np.cos(i*3 + offset*2)],
            [base_x[i+1] - 0.3*np.sin(i*4 + offset*4), base_y[i+1] - 0.5*np.cos(i*2 + offset*3)],
            [base_x[i+1], base_y[i+1]]
        ])
        curve = bezier_curve(points)
        shapes.append(curve)
    return shapes

def plot_abstract_water():
    fig, ax = plt.subplots(figsize=(9,6))
    ax.set_facecolor('#001f3f')
    ax.axis('off')
    
    n_layers = 6
    colors = cm.Blues(np.linspace(0.4, 0.9, n_layers))
    
    for i in range(n_layers):
        shapes = random_fluid_shape(offset=i*0.3)
        for shape in shapes:
            path_data = [(Path.MOVETO, shape[0])]
            path_data += [(Path.CURVE4, p) for p in shape[1:]]
            codes, verts = zip(*path_data)
            path = Path(verts, codes)
            patch = PathPatch(path, facecolor=colors[i], alpha=0.3 + i*0.1, lw=0)
            ax.add_patch(patch)
    
    plt.tight_layout()
    plt.show()

plot_abstract_water()
