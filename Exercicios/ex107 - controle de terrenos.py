def calArea(a, b):
    area = a * b
    print("A area de um terreno com {} por {} é de {}".format(a, b, area))


print("CONTROLE DE TERRENOS")
print("---------------------")
larg = float(input("Informe a LARGURA do terreno: "))
comp = float(input("Infome o COMPRIMENTO do terreno: "))
calArea(larg, comp)
