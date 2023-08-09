from time import sleep

def contador(ini, fim, pas):
    print("~" * 50)
    print("Contagem de 1 em 1 até 10: ")
    ini = 0
    fim = 10
    pas = 1
    for cont in range (ini, fim+1, pas):
        print(cont, end=" ")
        sleep(0.2)
    print(" ")
    print("~" * 50)
    pas = 2
    print("Contagem de 10 a 0 de 2 em 2")
    for cont2 in range (fim, ini-1, - pas):
        print(cont2, end=" ")
        sleep((0.2))
    print(" ")
    print("~" * 50)
    print("Agora é sua vez de contar")
    ini = int(input("Informe o inicio: "))
    fim = int(input("Informe o fim: "))
    pas = int(input("Informe o passe: "))
    if pas <= 0:
        pas = 1
    if ini > fim:
        for cont3 in range(ini, fim, - pas):
            print(cont3, end=" ")
            sleep(0.2)
    if ini < fim:
        for cont3 in range(ini, fim, pas):
            print(cont3, end=" ")
            sleep(0.2)



contador(1, 10, 1)
