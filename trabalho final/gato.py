# 4. Gato:

# Herda da classe Pet.
# Atributos específicos de gatos (ex: raça, cor da pelagem, características físicas).
# Métodos específicos de gatos (ex: miar, ronronar, subir em árvores).
import pet

class Gato(pet.Pet):
    def __init__(self, nome, raca, especie, genero, idade, tutor, localResgatado, resgatador, abrigo, porte, cor, caracteristicas):
        super().__init__(nome, raca, especie, genero, idade, tutor, localResgatado, resgatador, abrigo, porte, cor, caracteristicas)
    def miar(self):
        print(f"o gato(a) {self.nome} esta miando")
    def ronronar(self):
        print(f"o gato(a) {self.nome} esta ronronando")
    def subirEmArvores(self):
        print(f"o gato(a) {self.nome} subiu uma arvore")