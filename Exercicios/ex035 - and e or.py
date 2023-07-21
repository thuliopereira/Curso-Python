idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Voce não pode votar")

if idade >= 18 and idade <= 60:
    print("Voce é obrigado a votar")

if idade >= 16 and idade < 18 or idade > 60:
    print("Voto opcional")

