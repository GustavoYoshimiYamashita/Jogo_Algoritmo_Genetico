import pygame
from pygame.locals import *
from pygame.transform import *


# Booleano para o while do labirinto
jogo = True

# Inicializando cor
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
white = (255, 255, 255)
vertical = 600
horizontal = 600

center_h = (horizontal / 2)
center_v = (vertical / 2)

surface = pygame.display.set_mode((horizontal, vertical))

distancia = [0, 0, 0, 0]
valor = 0
color = []

def verifica_distancia(inicioX, inicioY):
    for x in range(100):
        color = surface.get_at((int(inicioX), int(inicioY)))[:3]
        if color == red:
            print("red")
        inicioX += 1

    for y in range(100):
        color = surface.get_at((int(inicioX), int(inicioY)))[:3]
        if color == red:
            print("red")
        inicioY += 1

    for z in range(100):
        color = surface.get_at((int(inicioX), int(inicioY)))[:3]
        if color == red:
            print("red")
        inicioX -= 1

    for h in range(100):
        color = surface.get_at((int(inicioX), int(inicioY)))[:3]
        if color == red:
            print("red")
        inicioY -= 1

while jogo:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    surface.fill(black)
    pygame.draw.circle(surface, red, (center_v, center_h + 200), 20)

    verifica_distancia(center_v, center_h)

    pygame.display.update()


