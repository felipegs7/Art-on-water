import numpy as np
import matplotlib.pyplot as plt

def circulo_3d(ax, x, y, raio, cor_centro, cor_borda, sombra_offset=0.1):
    n = 30
    for i in range(n, 0, -1):
        alpha = (1 - i/n) * 0.8
        raio_i = raio * (i / n)
        cor = (
            cor_centro[0] + (cor_borda[0] - cor_centro[0]) * (i / n),
            cor_centro[1] + (cor_borda[1] - cor_centro[1]) * (i / n),
            cor_centro[2] + (cor_borda[2] - cor_centro[2]) * (i / n),
            alpha
        )
        circ = plt.Circle((x, y - sombra_offset), raio_i, color=cor, linewidth=0)
        ax.add_patch(circ)
    sombra = plt.Circle((x + sombra_offset, y - sombra_offset), raio, color='black', alpha=0.15)
    ax.add_patch(sombra)

def arte_respingo_3d_gradiente():
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Fundo da figura (tela inteira)
    fig.patch.set_facecolor('#0a1f44')  # azul escuro
    ax.set_facecolor('#0a1f44')          # mesmo azul escuro para os eixos
    
    centro = (0, 0)
    max_raio = 3.5
    n_ondas = 6

    cor_centro = (0.6, 0.85, 1.0)  # azul claro
    cor_borda = (0.1, 0.3, 0.55)   # azul escuro suave

    # Desenha as ondas
    for i in range(n_ondas):
        raio = max_raio * (i + 1) / n_ondas
        circulo_3d(ax, centro[0], centro[1], raio, cor_centro, cor_borda, sombra_offset=0.05*i)

    # Desenha gotas aleatórias
    np.random.seed(42)
    gotas_x = np.random.uniform(-3, 3, 15)
    gotas_y = np.random.uniform(-3, 3, 15)
    tamanhos = np.random.uniform(0.1, 0.25, 15)

    for x, y, t in zip(gotas_x, gotas_y, tamanhos):
        circulo_3d(ax, x, y, t, (0.7, 0.9, 1.0), (0.15, 0.35, 0.65), sombra_offset=0.07)

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('Respingo 3D em Água — Museu Virtual', fontsize=20, color='#a0cfff', pad=20)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    arte_respingo_3d_gradiente()
