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


def cruzando_metade_aleatoria_metodo1(individuos):
    primeiros_5_ind1 = individuos["individuo1"][3][:2]
    ultimos_5_ind1 = individuos["individuo1"][3][2:]
    primeiros_5_ind2 = individuos["individuo2"][3][:2]
    ultimos_5_ind2 = individuos["individuo2"][3][2:]

    print(f"5 primeiros pesos do individuo 1: {primeiros_5_ind1}")
    print(f"5 ultimos pesos do individuo 1: {ultimos_5_ind1}")
    print(f"5 primeiros pesos do individuo 2: {primeiros_5_ind2}")
    print(f"5 ultimos pesos do individuo 2: {ultimos_5_ind2}")

    primeiro_descendente = []
    segundo_descendente = []

    for i in range(2):
        primeiro_descendente.append(primeiros_5_ind1[i])
        primeiro_descendente.append(ultimos_5_ind2[i])
        segundo_descendente.append(primeiros_5_ind2[i])
        segundo_descendente.append(ultimos_5_ind1[i])

    print()
    print(f"Primeiro descendente: {primeiro_descendente}")
    print(f"Segundo descendente: {segundo_descendente}")


def cruzando_metade_aleatoria_metodo2(individuos):
    primeiros_5_ind1 = individuos["individuo1"][3][:2]
    ultimos_5_ind1 = individuos["individuo1"][3][2:]
    primeiros_5_ind2 = individuos["individuo2"][3][:2]
    ultimos_5_ind2 = individuos["individuo2"][3][2:]

    print(f"Pesos do individuo 1: {primeiros_5_ind1}{ultimos_5_ind1}")
    print(f"Pesos do individuo 2: {primeiros_5_ind2}{ultimos_5_ind2}")

    primeiro_descendente = []
    segundo_descendente = []

    for i in range(2):
        primeiro_descendente.append(primeiros_5_ind1[i])
    for i in range(2):
        primeiro_descendente.append(ultimos_5_ind2[i])
    for i in range(2):
        segundo_descendente.append(primeiros_5_ind2[i])
    for i in range(2):
        segundo_descendente.append(ultimos_5_ind1[i])

    print()
    print(f"Primeiro descendente: {primeiro_descendente}")
    print(f"Segundo descendente: {segundo_descendente}")

