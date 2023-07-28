primeiro = int(input("Informe o inicio da contagem: "))
razao = int(input("Informe a razão da contagem: "))
cont = 0
mais = 10
contador = 0
while mais != 0:
    while cont < mais:
        print(" ", primeiro, " ->", end="")
        primeiro = primeiro + razao
        cont += 1
        contador += 1
    mais = int(input(" Quantos valores a mais voce deseja contar: "))
    cont = 0

print("Total de termos mostrados {}".format(contador))