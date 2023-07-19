import math

num = int(input("Informe um numero: "))
raiz = math.sqrt(num)

input("Raiz Quadrada = {}".format(raiz))
input("Raiz Quadrada Arredondado Acima = {}".format(math.ceil(raiz)))
input("Raiz Quadrada Arredondado Abaixo = {}".format(math.floor(raiz)))

