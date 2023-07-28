cont = 1
uni = 0
dec = 0
cen = 0
while cont != 0:
    cont = int(input("Informe uma valor: "))
    if cont > 0 and cont < 10:
        uni = uni + 1
    elif cont >= 10 and cont < 100:
        dec = dec + 1
    elif cont >= 100:
        cen = cen + 1

print("FORAM DIGITADOS")
print("{} valores unitarios".format(uni))
print("{} valores decimais".format(dec))
print("{} valores centecimais".format(cen))
print("FIM")