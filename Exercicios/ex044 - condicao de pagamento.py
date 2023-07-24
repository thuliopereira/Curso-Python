valor = float(input("Qual o valor do produto: "))
print("CONDIÇÕES DE PAGAMENTO")
print("1 - A vista no dinheiro ou PIX")
print("2 - A vista no cartão de credito")
print("3 - Em até 3x sem juros no cartão")
print("4 - Acima de 4x com juros no cartão")

selecao = input("Informe como quer pagar: ")
if selecao == "1":
    print("A vista no dinheiro ou PIX: R${}".format((valor - (valor / 100) * 10)))
elif selecao == "2":
    print("A vista no cartão de credito: R${}".format((valor - (valor / 100) * 5)))
elif selecao == "3":
    print("Em até 3 vezes no cartão: R${}".format(valor))
elif selecao == "4":
    print("Acima de 4 vezes no cartão: R${}".format(((valor / 100) * 20) + valor))