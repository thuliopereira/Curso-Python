import random

num = random.randint(1, 10)
res = 0
tentativas = 0

print("O COMPUTADOR VAI SORTEAR UM NUMERO E NÓS VAMOS TENTAR ADIVINHAR")

while res != num:
    res = int(input("Seu palpite é: "))
    tentativas = tentativas + 1

print("PARABENS, voce acertou... Eu tinha pensado em {} e voce levou {} para acertar".format(num, tentativas))