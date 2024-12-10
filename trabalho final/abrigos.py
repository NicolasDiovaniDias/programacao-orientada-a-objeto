import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='animais_esperanca',
)

cursor=conexao.cursor()
class Abrigos:
    def __init__(self, nome, endereco, capacidade):
        self.nome=nome
        self.endereco=endereco
        self.capacidade=capacidade
def adicionarAbrigo():
    nome=input("qual o nome do abrigo? ")
    endereco=input("qual o endereço? ")
    capacidade=int(input("qual a capacidade do abrigo? "))
    return nome, endereco, capacidade
nome, endereco, capacidade=adicionarAbrigo()
cursor.execute("INSERT INTO abrigos (nome, endereco, capacidade) VALUES(%s,%s,%s)",(nome, endereco, capacidade))
conexao.commit()
Abrigos1= Abrigos(nome, endereco, capacidade)
