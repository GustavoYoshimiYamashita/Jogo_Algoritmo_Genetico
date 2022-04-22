'''

Criando algoritmo genético

Gustavo Yoshimi Yamashita
Youtube: https://www.youtube.com/c/RobotizandoCanal
LinkedIn: https://www.linkedin.com/in/gustavo-yamashita/

'''

import pygame
from pygame.locals import *
from pygame.transform import *
import individuos

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

# Inicializando a tela do Pygame
surface = pygame.display.set_mode((horizontal, vertical))

# Gerando indivíduos
individuos = gerando_inidividuos.criando_individuos(vertical/2, horizontal/2, 100)


while jogo:

    # Preenchendo a tela inicialmente como preto
    surface.fill(black)

    # Para cada evento dentro do Pygame
    for event in pygame.event.get():
        # Caso detectar o clique no "X" do display, então encerrar o processo
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Atualizando a imagem
    pygame.display.update()
    pygame.display.flip()
