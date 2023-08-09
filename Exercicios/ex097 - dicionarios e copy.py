estado = dict()
brasil = list()

for cont in range (0, 3):
    estado["uf"] = input("Unidade federativa: ")
    estado["sigla"] = input("Sigla: ")
    brasil.append(estado.copy())

for cont in range (0, 3):
    print(brasil[cont])