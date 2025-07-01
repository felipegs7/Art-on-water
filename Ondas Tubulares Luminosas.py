import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as pe

def create_wave_petals(amplitude=0.3, n_points=300, n_petals=6, phase=0):
    t = np.linspace(0, 2*np.pi, n_points)
    r = 0.5 + amplitude * np.sin(n_petals * t + phase)
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

def plot_wave_flowers():
    fig, ax = plt.subplots(figsize=(6,6))

    # Fundo degradê azul horizontal
    gradient = np.linspace(0, 1, 256)
    gradient = np.tile(gradient, (256,1))
    cmap = LinearSegmentedColormap.from_list('blue_gradient', ['#00305a', '#0073c2'])
    ax.imshow(gradient, aspect='auto', cmap=cmap, extent=[-1,1,-1,1])

    ax.axis('off')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_aspect('equal')

    n_flowers = 8
    for i in range(n_flowers):
        angle = 2 * np.pi * i / n_flowers
        x, y = create_wave_petals(amplitude=0.3, n_petals=7, phase=angle)
        x_rot = x * np.cos(angle) - y * np.sin(angle)
        y_rot = x * np.sin(angle) + y * np.cos(angle)

        # Linha base - brilho (mais grossa, quase branca e transparente)
        ax.plot(x_rot, y_rot, color='white', linewidth=10, alpha=0.12, solid_capstyle='round')

        # Linha principal azul clara
        ax.plot(x_rot, y_rot, color='#b3d9ff', linewidth=5, alpha=0.8, solid_capstyle='round',
                path_effects=[pe.SimpleLineShadow(shadow_color='white', alpha=0.4, rho=1.2),
                              pe.Normal()])

        # Linha fina branca para borda 3D brilhante
        ax.plot(x_rot, y_rot, color='white', linewidth=1.5, alpha=0.9, solid_capstyle='round')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_wave_flowers()

