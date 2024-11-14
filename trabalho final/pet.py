# 2. Pet:

# Herda da classe Animal.
# Atributos específicos de cada espécie (ex: porte, cor da pelagem, características físicas).
# Métodos específicos de cada espécie (ex: latir, miar, ronronar).

import animais

class Pet(animais.Animal):
    def __init__(self, nome, raca, especie, genero, idade, tutor, localResgatado, resgatador, abrigo, porte, cor, caracteristicas):
        self.porte=porte
        self.cor=cor
        self.caracteristicas=caracteristicas
        super().__init__(nome, raca, especie, genero, idade, tutor, localResgatado, resgatador, abrigo)
    