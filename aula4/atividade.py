class carro:
    def __init__(self, marca, modelo, ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.proprietario=None
    def listar(self):
        print(f'''
            marca = {self.marca}
            modelo = {self.modelo}
            ano = {self.ano}
            nome_proprietario = {self.proprietario.nome}
            idade_proprietario = {self.proprietario.idade}
        ''')
    def definir_proprietario(self,proprietario):
        self.proprietario=proprietario
class proprietario:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
def retorno():
    nome=input("qual o nome do dono do carro? ")
    idade=int(input("qual a idade do dono? "))
    return (nome,idade)
nome,idade=retorno()
proprietario1=proprietario(nome,idade)
carro1=carro("bmw","sandero","1023")
carro1.definir_proprietario(proprietario1)
carro1.listar()
