import random
from operator import itemgetter
cont = 0
jogador = dict()
jogadoresOrdenados = list()

jogador = {"Jogador 1": random.randint(1,6),
        "Jogador 2": random.randint(1,6),
        "Jogador 3": random.randint(1,6),
        "Jogador 4": random.randint(1,6)}

print("VALORES SORTEADOS")
for k, v in jogador.items():
    print("O {} tirou {} no dado".format(k, v))

jogadoresOrdenados = sorted(jogador.items(), key=itemgetter(1))

print("RANKING")
for k, v in jogadoresOrdenados:
    cont = cont + 1
    print("{}º colocado: {} que tirou {} no dado".format(cont, k, v))