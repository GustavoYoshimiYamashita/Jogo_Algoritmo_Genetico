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

