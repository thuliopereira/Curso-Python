res = "l"
adultos = 0
homens = 0
mulheres = 0
sexo = "        "
idade = 0


while True:
    sexo = "l"
    idade = 0
    while sexo not in "M, F":
        sexo = input("Informe o sexo [M/F]: ").upper().strip()

    while idade == 0:
        idade = int(input("Informe a idade: "))

    if idade >= 18:
        adultos += 1

    if sexo == "M":
        homens += 1

    if sexo == "F" and idade >= 20:
        mulheres += 1

    res = "l"
    while res not in "S, N":
        res = input("Deseja encerrar o programa? [S/N]: ").upper().strip()

    if res == "S":
        break

print("Total de adultos (maiores de 18 anos): {}".format(adultos))
print("Total de homens: {}".format(homens))
print("Total de mulheres com mais de 20 anos: {}".format(mulheres))