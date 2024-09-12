import random


class AnimalEstimacao:
    def __init__(self, nome, especie, idade, tutor):
        self.nome=nome
        self.especie=especie
        self.idade=idade
        self.estado=None
        self.tutor=tutor
    def dormir(self):
        self.estado="dormindo"
    def comer(self):
        self.estado="Comendo"
    def brincar(self):
        self.estado="Brincando"
    def listar(self):
        print("******************************")
        print(f'Nome: {self.nome}')
        print(f'Espécie: {self.especie}')
        print(f'Idade: {self.idade}')
        print(f'Estado: {self.estado}')
        print(f'Tutor nome:{self.tutor.nome}')
        print(f'Celular Tutor:{self.tutor.celular}')
        print("******************************\n\n\n")

    def som(self):
        numero_aleatorio = random.random()
        sons=int(numero_aleatorio*10)
        print(f"{self.nome}")
        for i in range(sons):
            if self.especie == "Canino":
                print("Au ",end='')
            elif self.especie == 'Felino':
                print("Miau")
class Tutor:
    def __init__(self,nome,cpf,celular):
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
    def listar(self):
        print('\n')
        print("*"*20, ' Lista Tutor ', '*'*20)
        print(f''' 
        Nome {self.nome}
        CPF {self.cpf}
        Celular{self.celular}
        ''')

tutor1 = Tutor('Pedro','123.456.789-00','(51)9987788')

print("Cria Objeto 20")
pet1=AnimalEstimacao('Maia','Felino',4, tutor1)
pet1.listar()


print("muda estado 23 ")
pet1.dormir()
pet1.listar()
print("muda estado 26")
pet1.comer()
pet1.listar()
print("muda estado 29")
pet1.brincar()
pet1.listar()
pet1.som()
'''
guria=AnimalEstimacao("Guria","Canino",6)
guria.brincar()
guria.listar()
guria.som()
'''