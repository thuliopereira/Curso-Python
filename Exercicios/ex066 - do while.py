num = 0
soma = 0
while True:
    num = int(input("Informe um valor: "))
    soma += soma + num
    if num == 0:
        break

print("Total dos valores digitados: {}".format(soma))
print("FIM")

