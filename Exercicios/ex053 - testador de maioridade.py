ano = 0
maior = 0
jovem = 0

for cont in range (1, 5+1):
    ano = int(input("Informe o ano de nascimento da pessoa {}: ".format(cont)))
    if 2023 - ano <= 18:
        jovem = jovem + 1
    else:
        maior = maior + 1


print("Maiores de idade: {}".format(maior))
print("Menores de idade: {}".format(jovem))