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
        for y in range(10):
            peso = random.randrange(0, 10, 1)
            peso = peso/10
            dna.append(peso)

        nome_completo = nome + str(numero)
        numero += 1
        dic = {nome_completo: [nome_completo, center_v, center_h, dna, True, [0, 0, 0, 0], 0]}
        dic_individuos.update(dic)
    return dic_individuos

individuos = criando_individuos(quantidade_individuos)


def cruzando_metade_aleatoria_metodo1(individuos):
    primeiros_5_ind1 = individuos["individuo1"][3][:5]
    ultimos_5_ind1 = individuos["individuo1"][3][5:]
    primeiros_5_ind2 = individuos["individuo2"][3][:5]
    ultimos_5_ind2 = individuos["individuo2"][3][5:]

    print(f"5 primeiros pesos do individuo 1: {primeiros_5_ind1}")
    print(f"5 ultimos pesos do individuo 1: {ultimos_5_ind1}")
    print(f"5 primeiros pesos do individuo 2: {primeiros_5_ind2}")
    print(f"5 ultimos pesos do individuo 2: {ultimos_5_ind2}")

    primeiro_descendente = []
    segundo_descendente = []

    for i in range(5):
        primeiro_descendente.append(primeiros_5_ind1[i])
        primeiro_descendente.append(ultimos_5_ind2[i])
        segundo_descendente.append(primeiros_5_ind2[i])
        segundo_descendente.append(ultimos_5_ind1[i])

    print()
    print(f"Primeiro descendente: {primeiro_descendente}")
    print(f"Segundo descendente: {segundo_descendente}")


def cruzando_metade_aleatoria_metodo2(individuos):
    primeiros_5_ind1 = individuos["individuo1"][3][:5]
    ultimos_5_ind1 = individuos["individuo1"][3][5:]
    primeiros_5_ind2 = individuos["individuo2"][3][:5]
    ultimos_5_ind2 = individuos["individuo2"][3][5:]

    print(f"5 primeiros pesos do individuo 1: {primeiros_5_ind1}")
    print(f"5 ultimos pesos do individuo 1: {ultimos_5_ind1}")
    print(f"5 primeiros pesos do individuo 2: {primeiros_5_ind2}")
    print(f"5 ultimos pesos do individuo 2: {ultimos_5_ind2}")

    primeiro_descendente = []
    segundo_descendente = []

    for i in range(5):
        primeiro_descendente.append(primeiros_5_ind1[i])
    for i in range(5):
        primeiro_descendente.append(ultimos_5_ind2[i])
    for i in range(5):
        segundo_descendente.append(primeiros_5_ind2[i])
    for i in range(5):
        segundo_descendente.append(ultimos_5_ind1[i])

    print()
    print(f"Primeiro descendente: {primeiro_descendente}")
    print(f"Segundo descendente: {segundo_descendente}")





cruzando_metade_aleatoria_metodo2(individuos)



