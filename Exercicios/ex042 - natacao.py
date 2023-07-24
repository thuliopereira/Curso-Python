import datetime

nascimento = int(input("Informe sua data de nascimento: "))

ano = datetime.date.today().year

idade = ano - nascimento

if idade <= 9:
    categoria = "mirim"
elif idade <= 14:
    categoria = "infantil"
elif idade <= 19:
    categoria = "junior"
elif idade <= 20:
    categoria = "senior"
else:
    categoria = "master"

print("Voce é um nadador selecionavel para a categoria {}".format(categoria))
