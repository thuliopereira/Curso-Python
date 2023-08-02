lanche = ("hamburguer", "suco", "pizza", "pudim")
print(lanche)
print(lanche[2])
print(lanche[0:2])
print(lanche[2:])
print("#" * 70)

cont = 0
for cont in range (0, 4):
    print("Eu vou comer {}".format(lanche[cont]))

print("#" * 70)

for cont in lanche:
    print("Eu disse que vou comer {}".format(cont))

print("#" * 70)

print(sorted(lanche))

print("#" * 70)

a = (1, 2, 3)
b = (4, 5, 6, 7, 8, 9)
c = a + b
print(c)

print("#" * 70)

x = (1, 1, 5, 5, 5, 8, 6, 9, 5, 1, 5, 2, 5)
print(x.count(5))
print(x.index(8))

print("#" * 70)

pessoa = ("Thulio", 26, "Masculino", 1.78)
print(pessoa)

print("#" * 70)

estados = ("SP", "MG", "RJ", "BH")
del(estados)
print(estados)