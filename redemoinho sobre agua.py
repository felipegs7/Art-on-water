import pygame
import numpy as np
import math
import sys

# Configurações iniciais
WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 60
TOTAL_POINTS = 1000
NUM_SPIRALS = 8
TURNS = 5
WAVES = 7

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Redemoinho Aquático")
clock = pygame.time.Clock()

def generate_spiral(t, i):
    theta = np.linspace(0, 2 * math.pi * TURNS, TOTAL_POINTS)
    r = np.linspace(20, 280, TOTAL_POINTS)
    r += 12 * np.sin(WAVES * theta + 2.5 * t)

    x = r * np.cos(theta + t + i * 0.4)
    y = r * np.sin(theta + t + i * 0.4)

    return [(int(CENTER[0] + xi), int(CENTER[1] + yi)) for xi, yi in zip(x, y)]

def draw_spirals(time):
    for i in range(NUM_SPIRALS):
        points = generate_spiral(time, i)
        color = (102, 204, 255) if i % 2 == 0 else (180, 240, 255)
        alpha = int(80 + 40 * math.sin(time + i))
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.lines(surface, color + (alpha,), False, points, 3)
        screen.blit(surface, (0, 0))

# Loop principal
t = 0
running = True
while running:
    screen.fill((0, 30, 60))  # fundo azul escuro
    draw_spirals(t)
    pygame.display.flip()
    t += 0.02

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)

pygame.quit()
sys.exit()
