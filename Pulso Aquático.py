import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def pulso_aquatico_neon_muitas_linhas():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#003366')  # fundo azul ao redor
    ax.set_facecolor('#003366')         # fundo do gráfico azul também

    x = np.linspace(0, 10, 1000)
    ax.set_xlim(0, 10)
    ax.set_ylim(-3.5, 3.5)
    ax.axis('off')

    # Paleta de cores repetida para mais linhas
    cores_base = [
        ('#0a1f44', 0.7),  # azul marinho escuro
        ('#ffffff', 0.8),  # branco
        ('#ff4da6', 0.6)   # rosa neon
    ]

    n_linhas = 30  # número total de linhas
    linhas = []

    for i in range(n_linhas):
        cor, alpha = cores_base[i % len(cores_base)]
        lw = 1.5 + (i * 0.15)  # espessura crescente mas mais fina para não poluir
        linha, = ax.plot([], [], lw=lw, color=cor, alpha=alpha)
        linhas.append(linha)

    def init():
        for linha in linhas:
            linha.set_data([], [])
        return linhas

    def animate(frame):
        for i, linha in enumerate(linhas):
            offset = i * 0.08
            amplitude = 1.5 - (i * 0.04)
            y = (
                np.sin(2 * np.pi * (x * 0.15 + frame * 0.01 + offset)) * amplitude
                + np.cos(x * 0.3 + frame * 0.008 + offset) * 0.2
            )
            linha.set_data(x, y)
        return linhas

    anim = FuncAnimation(fig, animate, init_func=init, frames=300, interval=25, blit=True)
    plt.title("Pulso Aquático: Neon em Movimento — Museu Virtual", fontsize=20, color='#ffffff', pad=20)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    pulso_aquatico_neon_muitas_linhas()
