def somar(* num):
    print(num)
    print("Total de numeros digitados: {}".format(len(num)))
    s = 0
    for num in num:
        s += num
    print("A soma dos valores digitados é:",s)
    print("----------------------")


somar(1, 2)
somar(1, 2, 5, 9)
somar(2, 6, 9, 13, 56)