def nomeEGol(nomenf, golsnf=0):
    if len(nomenf) == 0:
        nomenf = "<desconhecido>"
    msg = f"O jogador {nomenf} fez {golsnf} gols"
    return msg


nomenf = input("Informe o nome do jogador: ").strip()
golsnf = input("Informe a quantidade de gols do jogador: ")
if golsnf.isnumeric():
    golsnf = int(golsnf)
else:
    golsnf = 0


print(nomeEGol(nomenf, golsnf))