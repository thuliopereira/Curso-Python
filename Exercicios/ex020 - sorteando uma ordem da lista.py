import random
n1 = input("Informe o primeiro aluno: ")
n2 = input("Informe o segundo aluno: ")
n3 = input("Informe o terceiro aluno: ")
n4 = input("Informe o quarto aluno: ")

lista = [n1, n2, n3, n4]
random.shuffle(lista)


print("A sequencia de alunos é... {}".format(lista))