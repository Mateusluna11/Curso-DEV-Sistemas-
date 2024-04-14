#3-) Crie uma classe representando os alunos de um determinado curso.
#A classe deve conter os atributos matrícula do aluno, nome, nota da primeira prova, nota da segunda prova e nota da terceira prova.
#Crie metodos para acessar o nome e a media do aluno.

class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def status_aprovacao(self):
        media = self.calcular_media()
        return "Aprovado" if media >= 6 else "Reprovado"

alunos = []

for _ in range(5):
    matricula = input("Matrícula do aluno: ")
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota da primeira prova: "))
    nota2 = float(input("Nota da segunda prova: "))
    nota3 = float(input("Nota da terceira prova: "))

    aluno = Aluno(matricula, nome, nota1, nota2, nota3)
    alunos.append(aluno)

melhor_aluno = max(alunos, key=lambda x: x.calcular_media())
pior_aluno = min(alunos, key=lambda x: x.calcular_media())

print(f"\nMelhor aluno:\nNome: {melhor_aluno.nome}\nMatrícula: {melhor_aluno.matricula}\nMédia: {melhor_aluno.calcular_media()}\nStatus: {melhor_aluno.status_aprovacao()}\n")
print(f"Pior aluno:\nNome: {pior_aluno.nome}\nMatrícula: {pior_aluno.matricula}\nMédia: {pior_aluno.calcular_media()}\nStatus: {pior_aluno.status_aprovacao()}\n")
