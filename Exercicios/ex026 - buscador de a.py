frase = input("Insira uma frase: ").strip()
fraseFormatada = frase.upper()

input("Quantidade de letras A: {}".format(fraseFormatada.count("A")))
input("Posição da Primeira letra A: {}".format(fraseFormatada.find("A") + 1))
input("Posição da ultima letra A: {}".format(fraseFormatada.rfind("A") + 1))