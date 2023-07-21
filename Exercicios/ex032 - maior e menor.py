print("Informe tres numeros a seguir...")
n1 = int(input())
maior = n1
menor = n1
n2 = int(input())
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = int(input())
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print("Dentre os digitados o maior foi: {}".format(maior))
print("Dentre os digitados o menor foi {}".format(menor))
