import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Chuva - Gotas de água caindo")

# Cor de fundo (céu cinza)
COR_FUNDO = (30, 30, 40)

# Classe que representa uma gota de água
class Gota:
    def __init__(self):
        self.x = random.randint(0, LARGURA)
        self.y = random.randint(-100, -10)
        self.raio = random.randint(2, 5)
        self.velocidade = random.uniform(4, 10)
        self.cor = (30, 144, 255, 180)  # Azul translúcido

    def cair(self):
        self.y += self.velocidade
        if self.y > ALTURA:
            self.x = random.randint(0, LARGURA)
            self.y = random.randint(-100, -10)
            self.velocidade = random.uniform(4, 10)
            self.raio = random.randint(2, 5)

    def desenhar(self, surface):
        # Desenha círculo azul claro com transparência simulada
        pygame.draw.circle(surface, (30, 144, 255), (int(self.x), int(self.y)), self.raio)

# Criar várias gotas
num_gotas = 100
gotas = [Gota() for _ in range(num_gotas)]

# Loop principal
clock = pygame.time.Clock()
rodando = True

while rodando:
    clock.tick(60)  # FPS = 60
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(COR_FUNDO)

    # Atualizar e desenhar gotas
    for gota in gotas:
        gota.cair()
        gota.desenhar(tela)

    pygame.display.flip()

pygame.quit()
