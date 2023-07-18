salarioAtual = float(input("Qual o valor do salario do funcionario: "))

aumento = 15

salarioAumentado = ((salarioAtual / 100) * aumento) + salarioAtual

print("O salario passou de R${} para R${}, sendo um aumento de {}%".format(salarioAtual, salarioAumentado, aumento))