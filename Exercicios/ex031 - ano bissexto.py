import datetime

ano = datetime.date.today().year
mes = datetime.date.today().month
dia = datetime.date.today().day
diaSemana = datetime.date.today().weekday()


print("Estamos no ano de {}".format(ano))
print("Estamos no mes de {}".format(mes))
print("Estamos no dia {}".format(dia))
print("Estamos no dia da semana {}".format(diaSemana))
