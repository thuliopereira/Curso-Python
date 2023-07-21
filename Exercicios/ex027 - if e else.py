ano = int(input("Qual o ano do seu carro? "))
idadeCarro = 2023 - ano

if idadeCarro <= 3:
    print("Seu carro tem {} e esta bem novinho".format(idadeCarro))
else:
    print("Seu carro tem {} anos e já não é mais tão novo".format(idadeCarro))
