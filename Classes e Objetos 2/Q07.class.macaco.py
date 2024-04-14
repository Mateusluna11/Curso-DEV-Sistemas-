#7-) Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
#Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
#Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}!")

    def ver_bucho(self):
        if self.bucho:
            print(f"{self.nome} tem na barriga: {', '.join(self.bucho)}")
        else:
            print(f"{self.nome} está com fome.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada para comer.")

macaco1 = Macaco(nome="Cesar - Me dá? Não!!!")
macaco2 = Macaco(nome="Jorge - O Curioso")

macaco1.comer("banana")
macaco2.comer("maçã")
macaco1.comer("Mamão")

macaco1.ver_bucho()
macaco2.ver_bucho()

macaco1.digerir()
macaco2.digerir()

macaco1.ver_bucho()
macaco2.ver_bucho()
