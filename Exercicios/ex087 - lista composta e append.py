lista1 = list() ## DECLARAÇÃO VIA METODO. NÃO PERMITE ESPECIFICAR POSIÇÃO (POR EXEMPLO LISTA[2]) LOGO DE INICIO, POIS NÃO SÃO CRIADAS AS POSIÇÕES LOGO DE CARA COMO EM OUTRAS DECLARAÇÕES, DEPENDENDO DE APPENDS
lista2 = [[], []] ##DECLARÇÃO JA ESPECIFICANDO QUANTAS POSIÇÕES VAMOS PRECISAR, DE MODO QUE PODEMOS LOGO DE CARA JA ESPECIFICAR POR EXEMPLO AS POSIÇÕES COM LISTA2[0] E LISTA2[1]. É A FORMA MAIS RECOMENDA QUANDO FOR POSSIVEL SABER LOGO DE CARA QUANTAS POSIÇÕES VAMOS PRECISAR E A MAIS RECOMENDADA PARA USAR COM ESTRUTRAS FOR E PRINCIPALMENTE ESTRUTURAS FOR ENCADEADAS
lista3 = [] ##DECLARAÇÃO GENERICA ONDE ESPECIFICAMOS APENAS QUE É UMA LISTA E NÃO QUANTAS LISTAS QUEREMOS DENTRO DESSA LISTA, ENTÃO ELA TAMBEM NÃO PODE SER REFERENCIADA COM UM LISTA3[2] POR EXEMPLO, POIS A POSIÇÃO NÃO É CRIADA LOGO DE INICIO, DEPENDENDO DE APPENDS


##ABAIXO TEREMOS EXEMPLOS DE DECLARAÇÃO E DE COMO REFERENCIAR AS POSIÇÕES COM CADA TIPO DE DECLARAÇÃO
##VEREMOS QUE DUAS DEPENDEN DE APPEND E APENAS A ESTRUTURA QUE JA DECLARAMOS A LISTA COM AS POSIÇÕES DESEJADAS PERMITE REFERENCIAR POSIÇÕES LOGO DE CARA SEM APPEND, SENDO A MAIS RECOENDADA PARA TRABALHAR, PRINCIPALMENTE SE FORMOS USAR LAÇOS FOR E FOR ENCADEADOS

##EXEMPLO DE USO DE DECLARAÇÃO COM LIST()
teste = list()
##teste[3] = "TOP" ESSA LINHA ESTA COMENTADA POIS ELA VAI DAR ERRO, COM O LIST() A POSIÇÃO 3 NÃO É CRIADA DE INICIO E SÓ PODE SER REFERENCIADA SE JA TIVER SIDO CRIADA POR UM APPEND
teste.append("Thulio")
teste.append(26)
galera = list()
galera.append(teste[:])
print(galera)

teste[0] = "Maria"
teste[1] = 24
galera.append(teste[:]) ##ATENÇÃO A ESSES DOIS PONTOS, SEM ELES CRIAMOS UMA LIGAÇÃO E NÃO UMA COPIA
print(galera)


##EXEMPLO DE DECLARAÇÃO JA CRIANDO AS POSIÇÕES QUE QUEREMOS
lista2[0] = "TOP"
lista2[1] = "Daora" ##ESSA LINHA NÃO VAI DAR ERRO COMO A COMENTADA LA EM CIMA POIS JA CRIAMOS A LISTA COM ESSA POSIÇÃO DECLARADA DE INICIO, DE MODO QUE PODEMOS REFERENCIALA SEM PROBLEMAS
print(lista2[0])
print(lista2[1])

##EXEMPLO DE DECLARAÇÃO GENERICA SEM CRIAR AS POSIÇÕES QUE QUEREMOS
##lista3[1] = "Bolado" ESSA LINHA TAMBEM ESTA COMENTADA POIS VAI DAR ERRO, PORQUE CRIAMOS A LISTA COMO APENAS UMA POSIÇÃO, UMA LISTA GENERICA, ENTÃO NÃO PODEMOS REFERENCIAR UMA POSIÇÃO NA LISTA POIS ELA AINDA NÃO EXISTE
lista3.append("Bolado")
print(lista3)