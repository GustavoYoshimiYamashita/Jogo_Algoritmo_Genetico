'''

Estudando os movimentos de um objeto utilizando o Pygame.

Gustavo Yoshimi Yamashita
Youtube: https://www.youtube.com/c/RobotizandoCanal
LinkedIn: https://www.linkedin.com/in/gustavo-yamashita/

'''

import pygame
from pygame.locals import *
from pygame.transform import *
from datetime import datetime

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

surface = pygame.display.set_mode((horizontal, vertical))

now = datetime.now().second
contador = 0
contador2 = 0
center_h = (horizontal / 2)
center_v = (vertical / 2)

while jogo:
    surface.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                contador += 0.01
            elif event.key == K_LEFT:
                contador -= 0.01
            elif event.key == K_DOWN:
                contador2 += 0.01
            elif event.key == K_UP:
                contador2 -= 0.01

    center_h = center_h + contador
    center_v = center_v + contador2

    pygame.draw.circle(surface, white, (center_h, center_v), 5)

    pygame.display.update()