largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura

print("Cada litro de tinta pinta 2m²")
print(("Cada lada de tinta contem 10 litros"))
print("Litros de tinta necessarios: {}".format(area / 2))
print("Quantidade de latas: {}".format((area / 2) / 10))
