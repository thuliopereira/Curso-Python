maior = 0
menor = 9999

for cont in range(1, 5+1):
    peso = float(input("Informe o peso do cidadão: "))
    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print("Maior peso encontrado: {}".format(maior))
print("Menor peso encontrado: {}".format(menor))