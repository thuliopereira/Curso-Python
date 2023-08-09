def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos] * 2
        pos = pos + 1


lista = [1, 5, 10, 4]
dobra(lista)
print(lista)