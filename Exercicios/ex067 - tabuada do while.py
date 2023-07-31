while True:
    num = int(input("Quer ver a tabuada de qual numero: "))
    if num < 0:
        break
    print("-" * 70)
    for cont in range (1, 10+1):
        print("{} x {} = {}".format(num, cont, (num * cont)))
    print("Numeros negativos encerram o programa")