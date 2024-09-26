# Crie uma classe Produto que represente um produto em um sistema de vendas. A classe deve ter os seguintes atributos:

# codigo: inteiro que representa o código único do produto                                      ex.1
# nome: string que representa o nome do produto                                                    ex. CAMISA
# categoria: string que representa a categoria do produto                                        ex. Vestuário
# preco: valor real que representa o preço do produto                                               ex. 79.90
# quantidadeEstoque: inteiro que representa a quantidade do produto em estoque  ex. 75
# E os seguintes métodos:

# __init__(self, codigo, nome, descricao, preco, quantidadeEstoque): construtor da classe que inicializa todos os atributos
# get_codigo(self): retorna o código do produto
# get_nome(self): retorna o nome do produto
# get_categoria(self): retorna a descrição do produto
# get_preco(self): retorna o preço do produto
# get_quantidade_estoque(self): retorna a quantidade do produto em estoque
# set_preco(self, novo_preco): define o novo preço do produto
# vender(self, quantidade_vendida): diminui a quantidade do produto em estoque de acordo com a quantidade vendida (deve verificar se há estoque suficiente antes de realizar a venda
#                  listar

# nome,
# a categoria,
# quantidade_vendida,
# preco e
# total_venda =    o valor da venda quantidade_vendida * preco 
# comprar(self, quantidade_comprada): aumenta (soma) na quantidade do produto em estoque de acordo com a quantidade comprada. 
class Produto:
    def __init__(self,codigo,nome,descricao,preco,quantidadeEstoque,vendas):
        self.codigo=codigo
        self.nome=nome
        self.descricao=descricao
        self.preco=preco
        self.quantidadeEstoque=quantidadeEstoque
        self.vendas=vendas
    def get_codigo(self):
        print(f"codigo = {self.codigo}")
    def get_nome(self):
        print(f"nome = {self.nome}")
    def get_categoria(self):
        print(f"descricao = {self.descricao}")
    def get_preco(self):
        print(f"preco = {self.preco}")
    def get_quantidade_estoque(self):
        print(f"quantidade no estoque = {self.quantidadeEstoque}")
    def set_preco(self):
        novo_preco=float(input(f"qual o novo preco de {self.nome}? "))
        self.preco=novo_preco
    def vender(self):
        vendas=int(input("quantos produtos foram vendidos? "))
        self.quantidadeEstoque-=vendas
        self.vendas+=vendas
    def comprar(self):
        compras=int(input("quantos produtos foram comprados? "))
        self.quantidadeEstoque+=compras
    def listar(self):
        print(f'''
        codigo = {self.codigo}
        nome = {self.nome}
        descricao = {self.descricao}
        preco = {self.preco}
        quantidade no estoque = {self.quantidadeEstoque}
        vendas = {self.vendas}
        total em vendas = {self.vendas*preco}
        ''')
def inserir():
    codigo=input("qual o codigo do produto? ")
    nome=input("qual o nome do produto? ")
    descricao=input(f"qual a descricao de {str(nome)}? ")
    preco=float(input(f"qual o preco de {str(nome)}? "))
    quantidadeEstoque=int(input(f"qual a quantidade de {str(nome)} no estoque? "))
    vendas=0
    return(codigo,nome,descricao,preco,quantidadeEstoque,vendas)
codigo,nome,descricao,preco,quantidadeEstoque,vendas=inserir()
produto1=Produto(codigo,nome,descricao,preco,quantidadeEstoque,vendas)
produto1.get_preco()
produto1.vender()
produto1.get_quantidade_estoque()
produto1.comprar()
produto1.get_quantidade_estoque()
produto1.set_preco()
produto1.listar()