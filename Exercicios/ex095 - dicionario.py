pessoas = {"Nome": "Thulio", "Sexo": "M", "Idade": 26}
print(pessoas)
print("As KEYS desse dicionario são: ", pessoas.keys())
print("Os VALUES desse dicionario são: ", pessoas.values())
print("Os ITEMS desse dicionario são: ", pessoas.items())

print("-=" * 50)

for key, value in pessoas.items():
    print(key, "=", value)

print("-=" * 50)

pessoas["Nome"] = "Thulio Pereira"
print(pessoas)

print("-=" * 50)

del pessoas["Sexo"]
print(pessoas)