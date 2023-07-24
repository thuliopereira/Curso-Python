letra = input("Nos informe uma letra: ")
letra = letra.upper()

if letra in "A E I O U":
    print("Vogal")
else:
    print("Invalido ou numeral")