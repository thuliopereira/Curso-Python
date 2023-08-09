pessoa = dict()
pessoas = list()
media = 0
totidade = 0
while True:
    pessoa["nome"] = input("Nome da pessoa: ")
    pessoa["idade"] = int(input("Idade da pessoa: "))
    pessoa["sexo"] = input("Sexo da pessoa: ").upper()
    pessoas.append(pessoa.copy())
    pessoa.clear()
    res = input("Deseja encerrar o programa [S/N]: ").upper().strip()
    if res == "S":
        break
print("-=" * 50)
print("Numero total de pessoas: {}".format(len(pessoas)))
for cont in range (0, len(pessoas)):
    totidade = totidade + pessoas[cont]["idade"]
    media = totidade / len(pessoas)
print("Media de idade: {}".format(media))
print("Lista com todas as mulheres: ")
for cont in range (0, len(pessoas)):
    if pessoas[cont]["sexo"] == "F":
        print(pessoas[cont]["nome"])
print("Lista com todos com idade maior que a media de idade: ")
for cont in range(0, len(pessoas)):
    if pessoas[cont]["idade"] > media:
        print(pessoas[cont]["nome"])