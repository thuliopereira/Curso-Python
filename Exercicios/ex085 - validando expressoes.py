frase = []

frase.append(input("Digite uma frase: "))

parentesesAbertos = parentesesFechados = 0

parentesesAbertos = frase[0].count("(")
parentesesFechados = frase[0].count(")")

if parentesesAbertos == parentesesFechados:
    print("Sua frase esta formatada corretamente")
else:
    print("Sua frase não esta formatada corretamente")