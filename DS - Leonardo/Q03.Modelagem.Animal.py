#Modele uma Classe animal
class Animal:
    def _init_(self, nome, dono, sexo, patas):
        self.nome = nome
        self.idade = dono
        self.sexo = sexo
        self.patas = patas
    def emitir_som(self):
        pass
    def mover(self):
        pass

class Dog(Animal):
    def _init_(self, nome, dono, sexo, patas, raca):
        super()._init_(nome, dono, sexo, patas, raca)
        self.raca = raca
    def emitir_som(self):
        return "Woof!"
    print(" Au au! ")
    print(" ")
    def mover(self):
        return "Correndo como um cachorro"
    print("Determine o movimento do animal!")
