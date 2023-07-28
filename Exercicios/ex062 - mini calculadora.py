n1 = int(input("Informe o PRIMEIRO valor: "))
n2 = int(input("Informe o SEGUNDO valor"))
sel = 0

while sel != 6:
    print("-" * 100)
    print("[1] SOMA")
    print("[2] SUBTRAÇÃO")
    print("[3] MULIPLICAÇÃO")
    print("[4] DIVISÃO")
    print("[5] NOVOS VALORES")
    print("[6] SAIR DO PROGRAMA")
    sel = int(input())
    if sel not in [1, 2, 3, 4, 5 , 6]:
        print("Opção Invalida")
    if sel == 1:
        print("A SOMA de {} e {} é {}".format(n1, n2, n1 + n2))
    if sel == 2:
        print("A SUBTRAÇÃO de {} e {} é {}".format(n1, n2, n1 - n2))
    if sel == 3:
        print("A MULTIPLICAÇÃO de {} e {} é {}".format(n1, n2, n1 * n2))
    if sel == 4:
        print("A DIVISÃO de {} e {} é {}".format(n1, n2, n1 / n2))
    if sel == 5:
        n1 = int(input("Informe o PRIMEIRO valor: "))
        n2 = int(input("Informe o SEGUNDO valor"))
print("FIM")