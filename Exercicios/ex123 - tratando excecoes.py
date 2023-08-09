def leia():
    while True:
        try:
            num = int(input("Digite um numero: "))
        except:
            print("ERRO, digite um numero valido")
            continue
        else:
            print("Numero validado")
            break


leia()