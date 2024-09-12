class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.proprietario = None

    # Definir ou alterar o proprietário do carro
    def definir_proprietario(self, pessoa):
        self.proprietario = pessoa

    def mostrar_informacoes(self):
        print("******************************")
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano de Lançamento: {self.ano}')
        if self.proprietario:
            print(f'Nome do Proprietário: {self.proprietario.nome}')
            print(f'idade do Proprietário: {self.proprietario.idade}')
        else:
            print("Este carro não possui proprietário.")
        print("******************************\n")

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carros = []  # Lista de carros que a pessoa possui

    # Adicionar um carro à lista de carros da pessoa
    def adicionar_carro(self, carro):
        self.carros.append(carro)
        carro.definir_proprietario(self)

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Carros de {self.nome}:')
        print('\n')
        for carro in self.carros:
            carro.mostrar_informacoes()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pessoa1 = Pessoa("Alex", "25 anos")

    carro1 = Carro("volkswagen", "Virtus", 2024)
    carro2 = Carro("CAOA CHERY", "Tiggo 8 PRO", 2024)

    pessoa1.adicionar_carro(carro1)
    pessoa1.adicionar_carro(carro2)

    pessoa1.mostrar_informacoes()