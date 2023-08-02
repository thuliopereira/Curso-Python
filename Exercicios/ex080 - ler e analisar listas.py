lista = []
maior = 0
maiorPos = 0
menor = 999
menorPos = 0

for cont in range (0, 5):
    lista.append(int(input("Digite um valor na posição {}: ".format(cont))))
    if lista[cont] > maior:
        maiorPos = cont
    elif lista[cont] < menor:
        menorPos = cont

lista.sort()

print(lista)

print("Maior valor da lista foi: {} digitado originalmente na posição {}".format(lista[4], maiorPos))
print("Menor valor da lista foi: {} digitado originalmente na posição {}".format(lista[0], menorPos))