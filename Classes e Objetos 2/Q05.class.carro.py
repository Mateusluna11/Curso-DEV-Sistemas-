#5-) Crie uma classe que modele um carro: (a) Atributos: marca, ano e preco. (b) Metodos: mostrar preco e de exibicao dos dados.

class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        return f"O preço do carro {self.marca} ({self.ano}) é R$ {self.preco}"

    def exibir_dados(self):
        return f"Marca: {self.marca}\nAno: {self.ano}\nPreço: R$ {self.preco}"

carro_exemplo = Carro(marca="Fiat", ano=2022, preco=75000)
print(carro_exemplo.mostrar_preco())
print("\nDetalhes do Carro:")
print(carro_exemplo.exibir_dados())
