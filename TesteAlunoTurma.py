from Aluno import Aluno
from Turma import Turma

aluno1 = Aluno("João")
turma1 = Turma("Turma A")
turma2 = Turma("Turma B")

aluno1.adicionarTurma(turma1)
aluno1.adicionarTurma(turma2)

print(f"Aluno: {aluno1.nome}")
print("Turmas do aluno:", [t.nome for t in aluno1.turmas])
print("Alunos da Turma A:", [a.nome for a in turma1.alunos])
