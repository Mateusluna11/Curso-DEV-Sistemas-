#2 - Crie uma classe que modele um retangulo:

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)

if __name__ == "__main__":
    lado_a_local = float(input("Informe o comprimento do local: "))
    lado_b_local = float(input("Informe a largura do local: "))

    local = Retangulo(lado_a_local, lado_b_local)
    area_local = local.calcular_area()
    perimetro_local = local.calcular_perimetro()
    quantidade_pisos = area_local // 1
    quantidade_rodapes = perimetro_local // 1

    print(f"\nQuantidade de pisos necessários: {quantidade_pisos}")
    print(f"Quantidade de rodapés necessários: {quantidade_rodapes}")
