def contador(ini, fim, pas):
    """
    -> Essa função cria um CONTADOR com tres parametros de configuração
    :param ini: Serve para informar o inicio da contagem
    :param fim: Serve para informar o final da contagem
    :param pas: Serve para informar de quanto em quanto sera a contagem
    :return: Não tem retorno
    """
    cont = ini
    while cont <= fim:
        print(cont, end=" ")
        cont = cont + pas


contador(0, 10, 4)