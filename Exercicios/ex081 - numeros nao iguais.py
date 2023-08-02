lista = []
while True:
    num = int(input("Informe um valor: "))
    if num == 0:
        break
    else:
        if num in lista:
            print("Numero não adicionado")
        else:
            lista.append(num)

lista.sort()

print(lista)