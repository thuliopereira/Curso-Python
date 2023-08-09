pessoa = dict()

pessoa["nome"] = input("Informe o Nome: ")
pessoa["nasc"] = int(input("Informe o ano de nascimento: "))
pessoa["ctps"] = int(input("Informe o Numero da carteira de trabalho (0 se não tiver): "))
if pessoa["ctps"] != 0:
    pessoa["contrat"] = int(input("Informe o ano de contratação: "))
    pessoa["aposentadoria"] = ((pessoa["contrat"] + 35) - 2023) + (2023 - pessoa["nasc"])
    for key, value in pessoa.items():
        print("O campo ", key, "tem o valor", value)
else:
    print("Ainda não é um trabalhador")