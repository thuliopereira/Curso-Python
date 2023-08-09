def leiaInt(val):
    msg = f"Voce digitou o numero {val}"
    return msg


valor = input("Digite um valor: ")
while True:
    if valor.isnumeric():
        valor = int(valor)
        break
    else:
        valor = input("ERRO, por favor digite um valor numerico: ")

print(leiaInt(valor))