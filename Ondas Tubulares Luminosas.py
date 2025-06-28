import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

def vortex_drops(num_drops=50, radius=1.0, time=0):
    # Gera posições em torno de um círculo com efeito de vórtice em movimento
    angles = np.linspace(0, 2*np.pi, num_drops, endpoint=False)
    drops = []
    
    for i, angle in enumerate(angles):
        # Variação radial com movimento ondulado para simular fluxo da água
        r = radius * (0.7 + 0.3 * np.sin(4 * angle + 3 * time + i))
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        
        # Variação do tamanho da gota para dar sensação 3D
        drop_radius = 0.07 + 0.03 * np.cos(6 * angle + 5 * time + i)
        
        drops.append((x, y, drop_radius))
    return drops

def plot_vortex_water():
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Fundo gradiente azul para azul claro
    gradient = np.linspace(0,1,256).reshape(1,-1)
    ax.imshow(gradient, aspect='auto', cmap='Blues', extent=[-1.5,1.5,-1.5,1.5], alpha=1, zorder=0)
    
    time = 0
    drops = vortex_drops(num_drops=70, radius=1.2, time=time)
    
    patches = []
    colors = []
    for i, (x, y, r) in enumerate(drops):
        circle = Circle((x, y), r)
        patches.append(circle)
        
        # Cor variando do azul escuro para azul claro, com transparência e brilho
        base_color = np.array([0.2, 0.5, 0.9])
        light_color = np.array([0.7, 0.9, 1.0])
        mix = (np.sin(i * 0.3 + time) + 1)/2
        color = base_color * (1 - mix) + light_color * mix
        colors.append(color)
    
    collection = PatchCollection(patches, facecolors=colors, edgecolors='white', linewidths=0.6, alpha=0.7)
    ax.add_collection(collection)
    
    plt.tight_layout()
    plt.show()

plot_vortex_water()
