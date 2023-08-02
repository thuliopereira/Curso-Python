res = "N"
total = 0
lista = []
while res == "N":
    lista.append(int(input("Digite um valor: ")))
    total += 1
    res = input("Deseja encerrar o programa? [S/N]").upper().strip()
lista.sort(reverse=True)
print("Foram digitados {} valores".format(total))
print("Lista reversa: {}".format(lista))

if 5 in lista:
    print("O valor 5 consta na lista")
else:
    print('O valor 5 não consta na lista')

