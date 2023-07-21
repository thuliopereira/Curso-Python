dist = int(input("Distancia da viagem: "))
valor = 0.0
if dist <= 200:
    valor = dist * 0.5
    print("Sua passagem vai custar R${}".format(valor))
else:
    valor = dist * 0.45
    print("Sua passagem vai custar R${}".format(valor))
