lista = []
for cont in range (0, 7):
    num = int(input("Digite o {} valor: ".format(cont+1)))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print("Valores Par: {}".format(lista[0]))
print("Valores Impar: {}".format(lista[1]))
print("Lista Completa: {}".format(lista))