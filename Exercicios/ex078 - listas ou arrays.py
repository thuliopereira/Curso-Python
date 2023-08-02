lista = [1, 2, 3, 4]
lista[0] = 8
print(lista)

print("-=" * 50)

lista.append(5) ##adiciona um elemento ao final da LISTa
print(lista)
lista.insert(3, 50)
print(lista)

print("-=" * 50)

lista.pop()
print(lista)
lista.pop(3)
print(lista)
lista.remove(2)
print(lista)

print("-=" * 50)

print(sorted(lista)) ##ordena apenas a exibição com print
lista.sort() ##ordena de fato a LISTA, mudando a ordem dos elementos
print(lista)
lista.sort(reverse=True) ##ordena de maneira REVERSA
print(lista)