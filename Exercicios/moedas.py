def aumentar(x, pc):
    resultado = ((x / 100) * pc) + x
    return resultado

def diminuir(x, pc):
    resultado = x - ((x / 100) * pc)
    return resultado

def dobro(x):
    resultado = x * 2
    return resultado

def metade(x):
    resultado = x / 2
    return resultado

def resumo(x, y, z):
    print("~~" * 25)
    print("RESUMO DO VALOR")
    print("~~" * 25)
    print(f"Metade de {x} é {metade(x)}")
    print(f"dobro de {x} é {dobro(x)}")
    print(f"Aumentando {y}% de {x} temos {aumentar(x, y)}")
    print(f"Diminuindo {z}% de {x} temos {diminuir(x, z)}")