lista = []
listaPar = []
listaImpar = []
for cont in range(0, 10):
    lista.append(int(input("Informe um valor: ")))

for cont in range(0, 10):
    if lista[cont] % 2 == 0:
        listaPar.append(lista[cont])
    else:
        listaImpar.append(lista[cont])

print("Lista normal:", lista)
print("Lista Par: ", listaPar)
print("Lista Impar: ", listaImpar)
