import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="animais_esperanca"
)
cursor = conexao.cursor()
class Tutor():
    def __init__(self, nome, telefone, endereco):
        self.nome=nome
        self.telefone=telefone
        self.endereco=endereco
    def registrar_tutor():
        nome=input("qual o seu nome? ")
        telefone=input("qual o seu telefone? ")
        endereço=input("qual o seu endereço? ")
        email=input("qual é seu gmail? ")
        while True:
            senha=input("qual vai ser sua senha? ")
            repeat_senha=input("repita sua senha: ")
            if(senha==repeat_senha):
                print("usuario cadastrado!")
                cursor.execute("INSERT INTO tutores (nome, telefone, endereco, email, senha) VALUES(%s,%s,%s,%s,%s)",(nome, telefone, endereço, email, senha))
                conexao.commit()
                break
            else:
                print("valores diferentes! ")
                
        
    def login():
        print("##LOGIN##")
        while True:
            email=input("qual seu email? ")
            cursor.execute("SELECT email,senha FROM tutores WHERE email = %s",(email,))
            resultado = cursor.fetchall()
            if(len(resultado)!=0):
                senha=input("digite sua senha: ")
                for i in range(len(resultado)):
                    if(resultado[i][1]==senha):
                        print(resultado[i])
                        print("acesso liberado")
                        return
            else:
                print("email inexistente")
        
    def adotarAnimal():
        cursor.execute("select id, nome from animais")
        resultado = cursor.fetchall()
        print("que bom que voce quer adotar um dos nossos animais, aqui segue a lista de animais pra adocao: ")
        ids=[]
        for i in range(len(resultado)):
            print(f"{i+1} - {resultado[i][1]}")
            ids.append(resultado[i][0])
            conexao.commit()
# Tutor.registrar_tutor()            
Tutor.registrar_tutor()