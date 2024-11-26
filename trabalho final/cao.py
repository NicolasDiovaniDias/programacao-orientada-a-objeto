import animais
import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='animais_esperanca',
)
cursor=conexao.cursor()
class Cao(animais.Animal):
    def __init__(self, nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo, porte, cor, caracteristicas):
        self.porte = porte
        self.cor = cor
        self.caracteristicas = caracteristicas
        super().__init__(nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo)
    def emitirSom(self):
        print(f"{self.nome} esta latindo")
    def buscarObjeto(self):
        print(f"o cao {self.nome} buscou um objeto")
    def correr(self):
        print(f"o cao {self.nome} esta correndo")
def passar_argumentos(animal1, id_animais):
    porte=input(f"qual o porte do {animal1.nome}? ")
    cor=input(f"qual a cor do {animal1.nome}? ")
    caracteristicas=input(f"quais são as caracteristicas do {animal1.nome}? ")
    cursor.execute("INSERT INTO caes (nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo, porte, cor, caracteristicas, fk_animais) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(animal1.nome,animal1.raca,animal1.especie,animal1.genero,animal1.idade,animal1.localResgatado,animal1.resgatador,animal1.abrigo,porte,cor,caracteristicas,id_animais))
    conexao.commit()