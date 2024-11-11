# nome: Nome do animal.
# raca: Raça do animal (ex: Labrador Retriever, SRD).
# especie: Espécie do animal (ex: Cão, Gato).
# genero: Sexo do animal (ex: macho, fêmea).
# idade: Idade do animal em meses ou anos.
# tutor: Objeto da classe Tutor que representa o dono do animal (se houver).
# localResgatado: Local onde o animal foi resgatado.
# resgatador: Objeto da classe Pessoa ou Entidade que resgatou o animal.
# abrigo: Objeto da classe Abrigo que representa o abrigo onde o animal está.
# Métodos:
# comer(): Simula o animal comendo.
# brincar(): Simula o animal brincando.
# emitirSom(): Simula o animal emitindo som (latido, miado, etc.).
# toString(): Retorna uma string com as informações do animal
class Animal:
    def __init__(self, nome, raca, especie, genero, idade, tutor, localResgatado, resgatador, abrigo):
        self.nome=nome
        self.raca=raca
        self.especie=especie
        self.genero=genero
        self.idade=idade
        self.tutor=tutor
        self.localResgatado=localResgatado
        self.resgatador=resgatador
        self.abrigo=abrigo
    def comer(self):
        print(f"o animal {self.nome} esta comendo")
    def brincar(self):
        print(f"o animal {self.nome} esta brincando")
    def emitirSom(self):
        print(f"AU! AU! AU! AU! AU! AU! AU! AU!")
    def toString(self):
        print(f"nome: {self.nome}\nraça: {self.raca}\nespecie: {self.especie}\ngenero: {self.genero}\nidade: {self.idade}\ntutor: {self.tutor}\nlocalResgatado: {self.localResgatado}\nresgatador: {self.resgatador}\nabrigo: {self.abrigo}")
# animal1=Animal('nicolas','humano','homem','macho',18,'deus','eldorado','samu','casa')
# animal1.toString()   
# animal1.comer()     
