'''

Apenas alguns testes envolvendo o Pygame

Gustavo Yoshimi Yamashita
Youtube: https://www.youtube.com/c/RobotizandoCanal
LinkedIn: https://www.linkedin.com/in/gustavo-yamashita/

'''

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

# Inicializando a tela do Pygame
surface = pygame.display.set_mode((horizontal, vertical))

# carregando a imagem para imprimir na tela
image = pygame.image.load(r'C:\Users\gusta\Desktop\VideoAula1\imagens\robo-removebg-preview.png')

# Modificando o tamanho da imagem
IMAGE_SMALL = pygame.transform.scale(image, (133.5, 116.75))

print(individuos)

while jogo:

    # Preenchendo a tela inicialmente como preto
    surface.fill(black)

    # Para cada evento dentro do Pygame
    for event in pygame.event.get():
        # Caso detectar o clique no "X" do display, então encerrar o processo
        if event.type == QUIT:
            pygame.quit()
            exit()
        # Caso detectar o clique na tecla de seta para direita e para esquerda, aumentar ou diminuir o ângulo
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                angle+=1
            if event.key == pygame.K_LEFT:
                angle-=1

    # Rotacionando a imagem
    rotated = pygame.transform.rotate(IMAGE_SMALL, angle)
    surface.blit(rotated, (0, 0))

    # Atualizando a imagem
    pygame.display.update()
    pygame.display.flip()
