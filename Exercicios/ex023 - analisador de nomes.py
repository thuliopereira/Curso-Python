nome = input("Informe o seu nome completo: ")

print("Nome Maiusculo: {}".format(nome.upper()))
print("Nome minusculo: {}".format(nome.lower()))
print("Quantidade de letras sem espaços: {}".format(len(nome) - nome.count(" ")))
print("Quantidade de letras do primeiro nome: {}".format(nome.find(" ")))