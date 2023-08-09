import random

def sorteio(lista):
    for cont in range(0, 5):
        lista[cont] = random.randint(1, 9)
    print("Valores sorteados foram: ", lista)

def somar(lista):
    s = 0
    for cont in range(0, 5):
        s = s + lista[cont]
    print("Soma dos valores é: ", s)


lista = [0, 0, 0, 0, 0]
sorteio(lista)
somar(lista)