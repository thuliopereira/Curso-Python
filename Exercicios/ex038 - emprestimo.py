valor = int(input("Qual o valor do imovel: "))
salario = int(input("Qual seu salario: "))
anos = int(input("Quantos anos pagando: "))
valorMes = 0

mes = anos * 12
valorMes = valor / mes


if valorMes <= ((salario / 100) * 30):
    print("Seu emprestimo foi aprovado com uma parcela de {:.2f} reais ao mes,"
          "por {} meses, {} anos, para um imovel de {} reais".format(valorMes, mes, anos, valor))
else:
    print("Emprestimo não aprovado")