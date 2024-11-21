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
# from tkinter import *
import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='animais_esperanca',
)
cursor=conexao.cursor()
cursor.execute("select * from animais where nome = 'joao'")
resultado = cursor.fetchall()
print(resultado)
class Animal:
    def __init__(self, nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo):
        self.nome=nome
        self.raca=raca
        self.especie=especie
        self.genero=genero
        self.idade=idade
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
        print(f"nome: {self.nome}\nraça: {self.raca}\nespecie: {self.especie}\ngenero: {self.genero}\nidade: {self.idade}\nlocalResgatado: {self.localResgatado}\nresgatador: {self.resgatador}\nabrigo: {self.abrigo}")
def retorno():
    nome = input(f"qual o nome do animal? ")
    raca = input(f"qual a raca do(a) {nome} ? ") 
    especie= input(f"qual a especie do(a) {nome} ? ")
    while True:
        genero=input(f"qual o genero do(a) {nome} ?\n1-Macho\n2-Femea\n") 
        if (genero=="1"):
            genero="M"
            break
        elif (genero=="2"):
            genero="F"
            break
        print("valor invalido")
    idade = input(f"qual a idade do(a) {nome} ? ")
    localResgatado = input(f"onde o(a) {nome} foi resgatado(a) ? ")
    resgatador = input(f"quem resgatou o(a) {nome} ? ") 
    abrigo = input(f"em que abrigo o(a) {nome} esta ? ")
    # while True:
    #     adotado=(input("o animal já foi adotado?\n1-sim\n2-não"))
    #     if(adotado=="1"):
    #         tutor.Tutor.adotarAnimal()
    #         print("animal adotado! ")
    #         break
    #     elif(adotado=="2"):
    #         print("animal já foi adotado")
    #         adotado=("")
    #         return()
    #     print("voce digitou um valor invalido")
    return (nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo)
nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo = retorno()
animal1=Animal(nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo)
cursor.execute("INSERT INTO animais (nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo))
conexao.commit()
conexao.close()
animal1.toString()   
animal1.comer()     
# janela = Tk()
# janela.mainloop()

