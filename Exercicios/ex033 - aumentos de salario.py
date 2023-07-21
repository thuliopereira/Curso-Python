print("Calculando aumentos")
salario = float(input("Informe o salario do funcionario: "))

if salario > 1250:
    print("O novo salario do funcionario sera: R${}".format(((salario/100) * 10) + salario))
else:
    print("O novo salario do funcionario sera: R${}".format(((salario/100) * 15) + salario))


