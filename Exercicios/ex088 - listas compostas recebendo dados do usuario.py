galera = []
dado = []
for cont in range (0,3):
    dado.append(input("Informe o nome: "))
    dado.append((int(input("Informe a idade: "))))
    galera.append(dado[:])
    dado.clear()

print(galera)