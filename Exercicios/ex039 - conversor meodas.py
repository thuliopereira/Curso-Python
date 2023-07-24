real = float(input("Informe o valor em reais: "))
convertido = 0
dolar = 4.78
yene = 0.034
libra = 6.14
euro = 5.31

print("PARA QUAL MOEDA VOCE DESEJA CONVERTER?")
print("1 - DOLAR")
print("2 - YENE")
print("3 - LIBRA")
print("4 - EURO")
selecao = input("Seleção: ")

if selecao == "1":
    convertido = real / dolar
    input("{} reais em dolares são {:.2f} dolares".format(real, convertido))
elif selecao == "2":
    convertido = real / yene
    input("{} reais em yenes são {:.2f} yenes".format(real, convertido))
elif selecao == "3":
    convertido = real / libra
    input("{} reais em libras são {:.2f} libras".format(real, convertido))
elif selecao == "4":
    convertido = real / euro
    input("{} reais em euros são {:.2f} euros".format(real, convertido))
else:
    print("Opção Invalida")