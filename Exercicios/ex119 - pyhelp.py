def pyhelp(comando):
    print("~~~" * 25)
    msg = help(comando)
    return(msg)

while True:
    comando = input("Digite o comando ou a biblioteca: ").lower()
    if comando == "fim":
        break
    pyhelp(comando)

