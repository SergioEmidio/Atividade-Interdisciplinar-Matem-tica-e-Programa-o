matriz = []

for i in range(1, 4):
    linha = []

    for j in range(1, 5):

        if i > j:
            valor = i + j
        else:
            valor = i - 2 * j

        linha.append(valor)

    matriz.append(linha)



for linha in matriz:
    for valor in linha:
        print(f'{valor:^5}', end='')
    print()
