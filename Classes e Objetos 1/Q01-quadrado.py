#1 - Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2

quadrado1 = Quadrado(5)
print(f"Lado do quadrado: {quadrado1.retornar_lado()}")
print(f"Área do quadrado: {quadrado1.calcular_area()}")

quadrado1.mudar_lado(7)
print(f"Novo lado do quadrado: {quadrado1.retornar_lado()}")
print(f"Nova área do quadrado: {quadrado1.calcular_area()}")
