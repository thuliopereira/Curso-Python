idades = 0
homemMaisVelhoNome = " "
homemMaisVelhoIdade = 0
mulheresComMenosDeVinte = 0

for cont in range(1, 4+1):
    nome = input("Informe o nome da pessoa {}: ".format(cont)).upper().strip()
    idade = int(input("Informe a idade da pessoa {}: ".format(cont)))
    sexo = input("Informe o sexo da pessoa {} (M/F)".format(cont)).upper().strip()
    idades = idades + idade
    if sexo == "M":
        if idade > homemMaisVelhoIdade:
            homemMaisVelhoIdade = idade
            homemMaisVelhoNome = nome
    elif sexo == "F" and idade < 20:
        mulheresComMenosDeVinte = mulheresComMenosDeVinte + 1


print("Media de idade do grupo é: {}".format(idades / cont))
print("O homem mais velho tem {} e se chama {}".format(homemMaisVelhoIdade, homemMaisVelhoNome))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulheresComMenosDeVinte))