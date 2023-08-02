print("LIGAR DUAS LISTAS")
a = [1, 2, 3, 4]
b = []
b = a
b.append(5)
print("Lista A: {}".format(a))
print("Lista B: {}".format(b))

print("-=" * 50)

print("COPIAR DUAS LISTAS")
a = [1, 2, 3, 4]
b = []
b = a[:]
b.append(5)
print("Lista A: {}".format(a))
print("Lista B: {}".format(b))