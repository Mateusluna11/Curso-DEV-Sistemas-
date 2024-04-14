#1 - Crie uma classe que modele um quadrado:
#atributos : tamanho do lado 
#metodos: mostrar endereço e alterar endereço 

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        print(f"Endereço: {self.endereco}")

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print("Endereço alterado com sucesso.")

pessoa = Pessoa(nome="Maria", idade=25, endereco="Rua A, 123")
pessoa.mostrar_endereco()

pessoa.alterar_endereco("Avenida B, 456")
pessoa.mostrar_endereco()
