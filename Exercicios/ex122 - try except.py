try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (TypeError, ValueError):
    print("Problemas com o TIPO que foi digitado")
except ZeroDivisionError:
    print("Não é possivel dividir por zero")
except KeyboardInterrupt:
    print("O usuario encerrou a execução do programa")
except Exception as erro:
    print("Infelizmente tivemos um problema. O erro foi {}".format(erro.__class__))
else:
    print("Operação concluida com sucesso. Resultado: ", r)
finally:
    print("Encerrando")