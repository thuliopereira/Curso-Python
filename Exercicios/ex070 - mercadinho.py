nome = ""
preco = 0.0
soma = 0.0
itemMilhar = 0
itemBarato = 9999
nomeItemBarato = ""
while True:
    res = "kkkk"
    nome = input("Informe o nome do produto: ").upper().strip()
    preco = float(input("Qual o valor do produto: "))
    soma += preco
    if preco > 1000:
        itemMilhar = itemMilhar + 1
    if preco < itemBarato:
        itemBarato = preco
        nomeItemBarato = nome
    while res not in "S, N":
        res = input("Deseja encerrar o programa [S/N]").upper().strip()
    if res == "S":
        break

print("Valor total: {}".format(soma))
print("Produto mais barato: {}".format(nomeItemBarato))
print("Produtos que custam mais de 1000 reais: {}".format(itemMilhar))