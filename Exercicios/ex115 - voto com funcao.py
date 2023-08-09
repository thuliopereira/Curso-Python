import datetime
def analise(ano):
    vota = " "
    idade = anoAtual - ano
    if idade < 16:
        resultado = f"Voce tem {idade} anos e tem voto NEGADO"
    elif idade >= 16 and idade < 18 or idade > 60:
        resultado = f"Voce tem {idade} anos e tem voto OPCIONAL"
    else:
        resultado = f"Voce tem {idade} anos e tem voto OBRIGATORIO"
    return resultado


anoAtual = datetime.date.today().year

ano = int(input("Informe seu ano de nascimento: "))
print(analise(ano))