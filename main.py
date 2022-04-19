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

angle = 30

surface = pygame.display.set_mode((horizontal, vertical))
image = pygame.image.load(r'C:\Users\gusta\Desktop\VideoAula1\imagens\robo-removebg-preview.png')
IMAGE_SMALL = image #pygame.transform.scale(image, (133.5, 116.75))

while jogo:
    surface.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                angle+=1
            if event.key == pygame.K_LEFT:
                angle-=1

    rotated = pygame.transform.rotate(IMAGE_SMALL, angle)
    surface.blit(rotated, (0, 0))
    pygame.display.update()
    pygame.display.flip()



    # Desenhando uma seta

