soma = 0
for cont in range(1, 6+1):
    val = int(input("Informe um numero: "))
    if val % 2 == 0:
        soma = soma + val

print(soma)