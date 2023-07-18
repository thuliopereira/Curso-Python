nomeAluno = input("Qual o nome do Aluno: ")
prova1 = float(input("Informe a nota da primeira prova do aluno {}: ".format(nomeAluno)))
prova2 = float(input("Informe a nota da segunda prova do aluno {}:".format(nomeAluno)))
media = (prova1 + prova2) / 2
print("O aluno {} ficou com média {}".format(nomeAluno, media))