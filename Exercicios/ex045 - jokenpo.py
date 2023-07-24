import random
import time

numero = random.randint(1, 3)
if numero == 1:
    cpu = "pedra"
elif numero == 2:
    cpu = "papel"
else:
    cpu = "tesoura"

print("JOKENPO")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
selecao = int(input("ESCOLHA COM SABEDORIA: "))

if selecao == 1:
    jogador = "pedra"
elif selecao == 2:
    jogador = "papel"
else:
    jogador = "tesoura"

print("JO-KEN-PO!!!")

time.sleep(3)

print("Jogador escolheu: {}".format(jogador))
print("CPU escolheu: {}".format(cpu))

if (jogador == "pedra" and cpu == "tesoura") or (jogador == "tesoura" and cpu == "papel") or (jogador == "papel" and cpu == "pedra"):
    print("JOGADOR GANHOU")
elif (jogador == "tesoura" and cpu == "pedra") or (jogador == "papel" and cpu == "tesoura") or (jogador == "pedra" and cpu == "papel"):
    print("COMPUTADOR GANHOU")
else:
    print("Empate")