import animais
import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='animais_esperanca',
)
cursor=conexao.cursor()
class Gato(animais.Animal):
    def __init__(self, nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo, cor, caracteristicas):
        self.cor = cor
        self.caracteristicas = caracteristicas
        super().__init__(nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo)
    def emitirSom(self):
        print(f"{self.nome} esta miando")
    def buscarObjeto(self):
        print(f"o gato {self.nome} buscou um objeto")
    def correr(self):
        print(f"o gato {self.nome} esta correndo")
def passar_argumentos(animal1, id_animais):
    cor=input(f"qual a cor do {animal1.nome}? ")
    caracteristicas=input(f"quais são as caracteristicas do {animal1.nome}? ")
    cursor.execute("INSERT INTO gatos (nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo, cor, caracteristicas, fk_animais) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(animal1.nome,animal1.raca,animal1.especie,animal1.genero,animal1.idade,animal1.localResgatado,animal1.resgatador,animal1.abrigo,    cor,caracteristicas,id_animais))
    conexao.commit()