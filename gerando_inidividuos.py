'''

Esse código envolve o estudo da geração de indivíduos para posteriormente ser aplicado a técnica de
algoritmos genéticos. O objetivo é entender como gerar os indivíduos tentando minimizar o tempo de
processamento.

Gustavo Yoshimi Yamashita
Youtube: https://www.youtube.com/c/RobotizandoCanal
LinkedIn: https://www.linkedin.com/in/gustavo-yamashita/

'''
import random


def criando_individuos(center_v, center_h, quantidade_individuos):
    nome = "individuo"
    numero = 1
    dic_individuos = {}

    for i in range(quantidade_individuos):
        dna = []
        for y in range(4):
            valor = random.randrange(0, 10, 1)
            valor = valor/10
            dna.append(valor)

        nome_completo = nome + str(numero)
        numero += 1
        dic = {nome_completo: [nome_completo, center_v, center_h, dna, True, [0, 0, 0, 0], 0]}
        dic_individuos.update(dic)
    return dic_individuos
