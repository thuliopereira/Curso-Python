frase = "Ola mundo!"

print(frase[4]) ##Renderizar uma unica posição
print(frase[0:4]) ##Renderizar um intervale de psoições
print(frase[0:8:2]) ##Renderizar um intervalo de psoições, mas especificando um intervalo

print(len(frase)) ##Retorna o tamnho da String
print(frase.count("o")) ##Retorna a quantidade de elementos na STRING
print(frase.find("ndo")) ##Retorna a posição em que encontrar o elemento buscado
print("Ola" in frase) ##Retorna TRUE se existir o elemento
print("ola" in frase) ##Retorna False se não existir o elemento

print(frase.replace("mundo", "universo")) ##Troca uma plavra da STRING por outra
print(frase.upper()) ##Muda tudo para maiusculo
print(frase.lower()) ##Muda tudo para minusculo
print(frase.capitalize()) ##Deixa tudo em minusculo, mas a primeira letra da STRING fica maiuscula
print(frase.title()) ##Deixa tudo em minusculo, mas a primeira letra de cada palabra da STRING fica maiuscula
print(frase.strip()) ##Remove espaços em branco no começo e final da STRING

print(frase.split()) ##Separa a STRING em uma LISTA usando de referencia o que for passado (espaços por padrão)
print("_".join(frase)) ##Une a STRING com uso de algum caractere ou simbolo