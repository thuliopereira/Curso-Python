valorAtual = float(input("Qual o valor do produto: "))
desconto = 5

valorDesconto = valorAtual - ((valorAtual / 100) * desconto)

print("Com {}% de desconto o produto vai custar: R${:.2f}".format(desconto, valorDesconto))