# Objetivo: Criar uma classe em Python para representar animais de estimação, com os métodos:

# Requisitos:

# A classe deve se chamar AnimalEstimacao.
# A classe deve ter os seguintes atributos:
# nome: nome do animal
# especie: espécie do animal (ex: cachorro, gato, peixe)
# idade: idade do animal em anos
# estado: estado que o animal se encontra (´Comendo', 'Dormindo','Brincando')
# A classe deve ter os seguintes métodos:
# __init__(self, nome, especie, idade): método construtor da classe, que inicializa os atributos
# comer(): método que simula o animal comendo
# dormir(): método que simula o animal dormindo
# brincar(): método que simula o animal brincando
# listar(): que retorna uma string com a representação textual do animal (ex: "Nome: Rex, Espécie: Cachorro, Idade: 3 anos,  Estado:Comendo").
# Exemplo de uso


 
# animal = AnimalEstimacao("Rex", "Cachorro", 3)

# animal.comer()
# animal.dormir()
# animal.brincar()
# animal.listar()


# Desafio:

# Adicione mais métodos à classe para representar outros comportamentos dos animais de estimação (ex: latir, miar, nadar)
import random
class animais_estimação:
    def __init__(self, nome, especie, idade, estado):
        self.nome=nome
        self.especie=especie
        self.idade=idade
        self.estado=estado
    nome=''
    especie=''
    idade=0
    estado=''
    def aleatorio(self):
        rand = random.randint(1,3)
        if rand == 1:
            self.comer()
        elif rand == 2:
            self.dormir()
        else:
            self.brincar()
    def comer(self):
        print(f"{self.nome} esta comendo")
        self.estado="comendo"
    
    def dormir(self):
        print(f"{self.nome} esta dormindo (que preguiçoso!)")
        self.estado="dormindo"

    def brincar(self):
        print(f"{self.nome} esta brincalhando")
        self.estado="brincando"
    
    def listar(self):
        print(f"\nnome - {self.nome}\nespecie - {self.especie}\nidade - {self.idade}\nestado - {self.estado}\n")

def retorno():
    nome=input("qual o nome do animal?")
    especie=input("qual a especie do animal?")
    idade=int(input("qual a idade do animal?"))
    while True:
        estado=input("oque o animal esta fazendo?\n1-comendo\n2-dormindo\n3-brincando\n")
        if(estado=="1"):
            estado="dormindo"
            break
        elif(estado=="2"):
            estado="comendo"
            break
        elif(estado=="3"):
            estado="brincando"
            break
        print("voce digitou um valor invalido")
    return(nome,especie,idade,estado)
if __name__ == '__main__':
    nome,especie,idade,estado=retorno()
    animal1=animais_estimação(nome,especie,idade,estado)
    animal2=animais_estimação("chumbinho","gato",4,"parado")
    animal1.listar()
    animal2.aleatorio()
    animal2.listar()