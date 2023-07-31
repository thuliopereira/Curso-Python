import random
vit = 0
while True:
    cpu = random.randint(0, 5)
    jogadorEscolha = "kkkk"
    jogadorNumero = 0
    while jogadorEscolha not in "IMPAR, PAR":
        jogadorEscolha = input("Voce quer IMPAR ou PAR? ").upper().strip()

    jogadorNumero = int(input("Qual numero deseja jogar: "))

    if jogadorNumero > 5:
        jogadorNumero = 5
    elif jogadorNumero < 0:
        jogadorNumero = 0

    soma = jogadorNumero + cpu
    print("CPU jogou {}".format(cpu))
    print("A soma dos valores deu {}".format(soma))
    imparPar = soma % 2
    if imparPar == 0:
        print("PAR")
        imparPar = "PAR"
    else:
        print("IMPAR")
        imparPar = "IMPAR"

    if jogadorEscolha == imparPar:
        print("VITORIA")
        vit = vit + 1
        print("-" * 70)
    elif jogadorEscolha != imparPar:
        print("Voce perdeu :/")
        print("Vitoria antes da derrota {}".format(vit))
        break