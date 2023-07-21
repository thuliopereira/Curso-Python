velocidadeMedida = int(input("Qual a velocidade medida no radar: "))
multa = 0.0

if velocidadeMedida > 80:
    print("Voce foi multado")
    multa = (velocidadeMedida - 80) * 7
    print("Cada quilometro acima do limite te custara R$7")
    print("Sua multa vai custar {:.2f} reais".format(multa))

print("FIM")