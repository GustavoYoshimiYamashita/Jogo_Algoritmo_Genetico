'''

Esse código envolve o estudo da geração de indivíduos para posteriormente ser aplicado a técnica de
algoritmos genéticos. O objetivo é entender como gerar os indivíduos tentando minimizar o tempo de
processamento.

Gustavo Yoshimi Yamashita
Youtube: https://www.youtube.com/c/RobotizandoCanal
LinkedIn: https://www.linkedin.com/in/gustavo-yamashita/

'''


import pygame
from pygame.locals import *
from pygame.transform import *
from datetime import datetime
import random

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

# Variáveis geração
quantidade_individuos = 100
dic_individuos = {}
dna = []
mortos = []
valores = [0, 0, 0, 0]

nome_completo = ""

# Individuo = {(posiçãoX), (posiçãoY), (código genético), (integridade), (distancia), (pontuação)}
individuo = {"individuo1": [nome_completo, center_v, center_h, dna, True, [0, 0, 0, 0], 0]}


def criando_individuos(quantidade_individuos):
    nome = "individuo"
    numero = 1

    for i in range(quantidade_individuos):
        dna = []
        for y in range(4):
            binario = random.randrange(0, 2, 1)
            dna.append(binario)

        nome_completo = nome + str(numero)
        numero += 1
        dic = {nome_completo: [nome_completo, center_v, center_h, dna, True, [0, 0, 0, 0], 0]}
        dic_individuos.update(dic)


def movimento_aleatorio(velocidade):
    nome = "individuo"
    numero = 1

    for i in range(quantidade_individuos):
        x = random.randrange(-velocidade, velocidade + 1, 1)
        y = random.randrange(-velocidade, velocidade + 1, 1)

        nome_completo = nome + str(numero)
        numero += 1

        if dic_individuos[nome_completo][1] >= 594 or dic_individuos[nome_completo][1] <= 6 or \
                dic_individuos[nome_completo][2] >= 594 or dic_individuos[nome_completo][2] <= 6:
            dic_individuos[nome_completo][4] = False
            mortos.append(dic_individuos[nome_completo])

            pygame.draw.circle(surface, red, (dic_individuos[nome_completo][1], dic_individuos[nome_completo][2]), 6)
        else:
            pygame.draw.circle(surface, white, (dic_individuos[nome_completo][1], dic_individuos[nome_completo][2]), 6)

        if dic_individuos[nome_completo][4] == True:
            dic_individuos[nome_completo][1] = dic_individuos[nome_completo][1] + x
            dic_individuos[nome_completo][2] = dic_individuos[nome_completo][2] + y

        try:
            valores = verifica_distancia(dic_individuos[nome_completo][1], dic_individuos[nome_completo][2], 50)
            dic_individuos[nome_completo][5] = valores
            # print(f"inidividuo: {dic_individuos[nome_completo][0]}, valores: {dic_individuos[nome_completo][5]}")
        except:
            pass

        if dic_individuos[nome_completo][5] == [1, 1, 1, 1]:
            dic_individuos[nome_completo][4] = False
            dic_individuos[nome_completo][6] += 1000


def verifica_distancia(inicioX, inicioY, dist):
    inicioXpositive = inicioX
    inicioXnegative = inicioX
    inicioYpositive = inicioY
    inicioYnegative = inicioY

    verificadorX = inicioX + dist
    verificadorY = inicioY + dist

    if verificadorX > 600:
        verificadorX = 600
    if verificadorY > 600:
        verificadorY = 600

    # dist = verificadorX - inicioX

    # x positio, y positivo, x negativo, y negativo

    valores = [0, 0, 0, 0]

    # print(f"inicioX: {inicioX}, inicioY: {inicioY}, color: {surface.get_at((int(inicioX), int(inicioY)))[:3]}")

    if surface.get_at((int(inicioX), int(inicioY)))[:3] == red:
        valores = [1, 1, 1, 1]
    else:
        for x in range(int(dist + 6)):
            inicioXpositive += 1
            inicioYpositive += 1
            inicioXnegative -= 1
            inicioYnegative -= 1

            if surface.get_at((int(inicioXpositive), int(inicioY)))[:3] == red:
                valores = [1, 0, 0, 0]
            if surface.get_at((int(inicioXnegative), int(inicioY)))[:3] == red:
                valores = [0, 0, 1, 0]
            if surface.get_at((int(inicioX), int(inicioYpositive)))[:3] == red:
                valores = [0, 1, 0, 0]
            if surface.get_at((int(inicioX), int(inicioYnegative)))[:3] == red:
                valores = [0, 0, 0, 1]

    return valores


criando_individuos(quantidade_individuos)

now = datetime.now()


while jogo:

    surface.fill(black)
    pygame.draw.circle(surface, red, (center_v, center_h + 200), 20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # if (datetime.now() - now).seconds > 5:
    #    exit()

    movimento_aleatorio(5)

    pygame.display.update()
