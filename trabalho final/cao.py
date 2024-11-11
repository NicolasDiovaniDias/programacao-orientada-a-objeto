# 3. Cão:

# Herda da classe Pet.
# Atributos específicos de cães (ex: raça, porte, características físicas).
# Métodos específicos de cães (ex: latir, buscar objetos, correr).
import pet

class Cao(pet.Pet):
    def __init__(self, nome, raca, especie, genero, idade, tutor, localResgatado, resgatador, abrigo, porte, cor, caracteristicas):
        super().__init__(nome, raca, especie, genero, idade, tutor, localResgatado, resgatador, abrigo, porte, cor, caracteristicas)
    def latir(self):
        print(f"o cao {self.nome} esta latindo")
    def buscarObjeto(self):
        print(f"o cao {self.nome} buscou um objeto")
    def correr(self):
        print(f"o cao {self.nome} esta correndo")