def notas(notas):
    pos = 0
    quanti = len(notas)
    maior = 0
    menor = 999
    media = 0
    soma = 0
    for cont in range (0, len(notas)):
        if notas[pos] > maior:
            maior = notas[pos]
        if notas[pos] < menor:
            menor = notas[pos]
        soma = soma + notas[pos]
        media = soma / len(notas)
        pos = pos + 1
    resp = f"Foram digitadas {quanti} notas, sendo {maior} a maior, {menor} a menor e {media} a media"
    return resp



resp = notas([1.0, 2.0, 9.5, 6.5, 10])
print(resp)