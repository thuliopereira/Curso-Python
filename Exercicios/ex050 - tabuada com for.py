x = int(input("Informe o valor desejado: "))

if x > 10:
    x = 10
elif x < 1:
    x = 1

for cont in range(0, 10+1, 1):
    print("{} x {} = {}".format(x, cont, (x * cont)))
