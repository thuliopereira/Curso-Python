alunos = dict()
alunos["nome"] = input("Informe o nome do aluno: ")
alunos["media"] = float(input("Informe a media de {}: ".format(alunos["nome"])))
if alunos["media"] >= 7.0:
    alunos["situação"] = "APROVADO"
else:
    alunos["situação"] = "REPROVADO"

print("O aluno {} tirou media {} e esta {}".format(alunos["nome"], alunos["media"], alunos["situação"]))