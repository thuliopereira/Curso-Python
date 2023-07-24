pais = input("Qual seu pais de origem? ")
pais = pais.upper()

if pais == "BRASIL":
    print("Voce é Brasileiro")
elif pais == "ESTADOS UNIDOS":
    print("Voce é Americano")
elif pais == "ARGENTINA":
    print("Voce é Argentino, hermano")
elif pais == "MEXICO":
    print("Voce é Mexicano")
elif pais in "CHINA JAPÃO JAPAO COREIA SINGAPURA TAIWAN":
    print("Voce é Asiatico")
else:
    print("Voce é estrangeiro")
