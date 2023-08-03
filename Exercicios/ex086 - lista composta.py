galera = [["Thulio"], ["Amanda"], ["Maria"], ["Raissa"]]
print(galera)

print("-=" * 50)

galera = [["Thulio", 26, "Masculino"], ["Amanda", 27, "Feminino"], ["Maria", 24, "Feminino"], ["Raissa", 24, "Feminino"]]
print(galera)

print("-=" * 50)

print(galera[0][0])
print(galera[1][0])
print(galera[2][2])
print(galera[3])

print("-=" * 50)

galera[3][1] = 25
print(galera)

print("-=" * 50)

for cont in range (0, 4):
    print("{} tem {} anos de idade e é do sexo {}".format(galera[cont][0], galera[cont][1], galera[cont][2]))