res = "N"
res2 = 5555
alunos = list()
alunosFinal = list()
qtdAlunos = 0
while True:
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    nota1 = float(input("Informe a nota de {}: ".format(nome)))
    alunos.append(nota1)
    nota2 = float(input("Informe a segunda nota de {}: ".format(nome)))
    alunos.append(nota2)
    media = (nota1 + nota2) / 2
    alunos.append(media)
    alunosFinal.append(alunos[:])
    alunos.clear()
    qtdAlunos = qtdAlunos + 1
    res = input("Deseja encerrar o envio de notas: [S/N]").upper().strip()
    if res == "S":
        break
print("NUMERO   NOME    MEDIA")
for cont in range (0, qtdAlunos):
    print("{}       {}    {}".format(cont, alunosFinal[cont][0], alunosFinal[cont][3]))

while True:
    print("-=" * 50)
    res2 = int(input("Quer exibir as notas de qual aluno: "))
    if res2 == 999:
        break
    else:
        print("As notas de {} são {} e {}".format(alunosFinal[res2][0], alunosFinal[res2][1], alunosFinal[res2][2]))

print("Encerrando")