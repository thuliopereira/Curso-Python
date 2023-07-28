media = 0
soma = 0
maior = 0
menor = 999
num = 0
cont = 0
res = "N"

while res == "N":
    num = int(input("Informe um valor: "))
    cont += 1
    soma = soma + num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    res = input("Deseja encerrar o programa? [S/N]").upper()

media = soma / cont

print("Programa encerrado... Calculando")
print("Media dos valores digitados: {}".format(media))
print("Maior valor digitado: {}".format(maior))
print("Menor valor digitado: {}".format(menor))