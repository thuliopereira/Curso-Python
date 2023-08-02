a = b = c = d = 77
while a not in range(0, 9+1):
    a = int(input("Informe um valor: "))
while b not in range(0, 9+1):
    b = int(input("Informe um valor: "))
while c not in range(0, 9+1):
    c = int(input("Informe um valor: "))
while d not in range(0, 9+1):
    d = int(input("Informe um valor: "))


tupla = (a, b, c, d)

print("Quantas vezes o numero 9 aparece na Tupla: {}".format(tupla.count(9)))
if 3 in tupla:
    print("Qual a posição do primeiro numero 3 na Tupla: {}".format(tupla.index(3)))
else:
    print("Nenhum numero 3 foi digitado nessa Tupla")
print("Quais foram os numeros PARES da Tupla: ",end=" ")
for cont in range(0,4):
    if tupla[cont] % 2 == 0:
        print(tupla[cont], end="")