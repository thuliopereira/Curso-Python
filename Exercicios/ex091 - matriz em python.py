matriz = list()
matrizFinal = list()
for cont in range (0, 3):
    for cont2 in range (0, 3):
        matriz.append(int(input("Digite o valor para {} {}: ".format(cont, cont2))))
    matrizFinal.append(matriz[:])
    matriz.clear()

for cont in range (0, 3):
    print(matrizFinal[cont])
