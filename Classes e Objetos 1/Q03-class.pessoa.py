#3 - Crie uma classe que modele uma pessoa:

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self, cm):
        self.altura += cm

    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")

pessoa1 = Pessoa("João", 18, 70, 170)
pessoa1.imprimir_informacoes()

pessoa1.envelhecer(3)
pessoa1.engordar(5)
pessoa1.crescer(2)
pessoa1.imprimir_informacoes()
