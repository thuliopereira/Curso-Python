import datetime
nascimento = int(input("Informe o seu ano de nascimento: "))

ano = datetime.date.today().year

if (ano - nascimento) <= 17:
    print("Voce ainda vai se alistar no futuro, daqui a {} anos".format(18 - (ano - nascimento)))
elif (ano - nascimento) == 18:
    print("É hora de voce se alistar")
else:
    print("Voce passou do prazo de se alistar por {} anos".format((ano - nascimento) - 18))