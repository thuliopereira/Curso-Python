import random

numeroPC = random.randint(1, 5)
print("Sortiei um numero entre 1 e 5, tente acertar :)")
numero = int(input("Qual seu palpite: "))

if numeroPC == numero:
    print("PARABENS, voce acertou!!! Eu sortiei {}".format(numeroPC))
else:
    print("Voce errou, chutou o numero {} e eu sortiei o numero {}".format(numero, numeroPC))