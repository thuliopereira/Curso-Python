matriz = list()
matrizFinal = list()
num = 0
soma = 0
somaTerceira = 0
for cont in range (0, 3):
    for cont2 in range (0, 3):
        num = int(input("Digite o valor para {} {}: ".format(cont, cont2)))
        if num % 2 == 0:
            soma = soma + num
        if cont == 2:
            somaTerceira = somaTerceira + num
        matriz.append(num)
    matrizFinal.append(matriz[:])
    matriz.clear()

for cont in range (0, 3):
    print(matrizFinal[cont])


print("Soma de todos os valores pares da matriz: {}".format(soma))
print("Soma dos valores da terceira coluna: {}".format(somaTerceira))
aux = max(matrizFinal[1])
print("Maior valor da segunda linha: {}".format(aux))