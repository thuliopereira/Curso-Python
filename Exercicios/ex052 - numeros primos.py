num = int(input("Informe um valor e analisaremos se ele é primo: "))
print("AZUL = PRIMO")
print("VERMELHO = NÃO PRIMO")
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\33[34m', end="")
    else:
        print('\33[31m', end="")
    print("{}".format(cont))