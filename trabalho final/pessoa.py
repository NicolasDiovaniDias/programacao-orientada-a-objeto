import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="animais_esperanca"
)
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome=nome
        self.cpf=cpf
        self.telefone=telefone