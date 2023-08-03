res = "N"
pessoas = list()
lista = list()
contagemPessoas = 0
maiorPeso = 0
nomeMaiorPeso = list()
menorPeso = 999
nomeMenorPeso = list()

while True:
    nome = input("Digite o nome da pessoa: ")
    lista.append(nome)
    peso = float(input("Informe o peso da pessoa: "))
    if peso >= maiorPeso:
        maiorPeso = peso
        nomeMaiorPeso.append(nome)
    elif peso <= menorPeso:
        menorPeso = peso
        nomeMenorPeso.append(nome)
    lista.append(peso)
    pessoas.append(lista[:])
    lista.clear()
    res = input("Deseja encerrar o programa: [S/N]").upper().strip()
    contagemPessoas = contagemPessoas + 1
    if res == "S":
        break
print(nomeMaiorPeso)
print("Quantidade de pessoas cadastradas: {}".format(contagemPessoas))
print("O maior peso foi de {} com {} kilos".format(nomeMaiorPeso, maiorPeso))
print("Pessoa menos pesada é {} com {} kilos".format(nomeMenorPeso, menorPeso))