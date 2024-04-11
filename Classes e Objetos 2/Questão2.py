2-) Crie uma classe que modele uma aluno:

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        return self.curso

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
        return "Curso alterado com sucesso"

aluno1 = Aluno("Maria", "123456", "Engenharia")
print("Curso atual:", aluno1.mostrar_curso())

aluno1.alterar_curso("Ciência da Computação")
print("Novo curso:", aluno1.mostrar_curso())
