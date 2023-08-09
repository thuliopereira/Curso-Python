jogador = dict()
golsDic = dict()
gols = list()
totgols = 0

jogador["nome"] = input("Informe o nome do jogador: ")
jogador["partidas"] = int(input("Quantas partidas jogou: "))
for cont in range(0, jogador["partidas"]):
    golsDic["gols"] = int(input("Quantos gols marcou na partida {}: ".format(cont)))
    totgols = totgols + golsDic["gols"]
    gols.append(golsDic.copy())
print("-=" * 50)
print("Jogador {} jogou {} partidas".format(jogador["nome"], jogador["partidas"]))
print("Marcou ao todo {} gols".format(totgols))
print("RELAÇÃO DE PARTIDAS E GOLS")

for cont in range(0, jogador["partidas"]):
    print(f'Partida = {cont}  //  Gols = {gols[cont]["gols"]}')