num = 77
num = int(input("Informe um numero entre 0 e 20: "))
while num not in range (0, 20):
    num = int(input("Valor invalido. Por favor, informe um numero entre 0 e 20: "))
tupla = ("zero", "um", "dois", "tres","quatro", "cinco", "seis", "sete","oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

print("Voce digitou o numero {}".format(tupla[num]))