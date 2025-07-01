import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

def agua_realista():
    # Gerar grade 2D
    x = np.linspace(-3, 3, 600)
    y = np.linspace(-3, 3, 600)
    X, Y = np.meshgrid(x, y)

    # Função de altura simulando ondas suaves
    Z = (
        0.5 * np.sin(3 * X + 1.5 * Y) +
        0.3 * np.sin(5 * X - 2 * Y) +
        0.2 * np.cos(7 * X + 3 * Y)
    )

    # Cria luz para simular reflexo e relevo
    ls = LightSource(azdeg=45, altdeg=65)
    rgb = ls.shade(Z, cmap=plt.cm.ocean, vert_exag=1, blend_mode='soft')

    plt.figure(figsize=(8, 8))
    plt.imshow(rgb, extent=(-3,3,-3,3))
    plt.axis('off')
    plt.title('Superfície Realista de Água — Museu Virtual', fontsize=18, color='#034f84', pad=20)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    agua_realista()
