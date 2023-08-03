import random
import time

jogos = int(input("Quantos jogos serão simulados: "))
lista = list()
listaJogos = list()

for cont in range (0, jogos):
    for cont in range (0, 6):
        lista.append(random.randint(1, 60))
    listaJogos.append(lista[:])
    lista.clear()
print("-=" * 50)
print("SORTEANDO...")

for cont in range (0, jogos):
    print("Jogo", cont + 1, ":", listaJogos[cont])
    time.sleep(0.5)

print("Boa sorte 😀")