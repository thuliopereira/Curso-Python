def num(lista):
    pos = 0
    maior = 0
    for num in lista:
        print(num, end=" ")
        if lista[pos] > maior:
            maior = lista[pos]
        pos = pos + 1
    print(" ")
    print("O maior dessa lista é {}".format(maior))


lista1 = [1, 6, 2, 68, 6]
num(lista1)
print("-----------")
lista2 = [6, 6646, 2, 649, 41]
num(lista2)
