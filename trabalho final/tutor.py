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
            cursor.execute("SELECT email, senha, id_tutores FROM tutores WHERE email = %s",(email,))
            resultado = cursor.fetchall()
            if(len(resultado)!=0):
                senha=input("digite sua senha: ")
                for i in range(len(resultado)):
                    if(resultado[i][1]==senha):
                        print("acesso liberado")
                        return resultado[i][2]
            else:
                print("email inexistente")
        
    def tutelarAnimal():
        cursor.execute("select id_animais, nome from animais")
        resultado = cursor.fetchall()
        print("que bom que voce quer ser o tutor de um dos nossos animais, aqui segue a lista de animais, primeiro faça login: ")
        ids=[]
        id_tutores=Tutor.login()
        for i in range(len(resultado)):
            print(f"{i+1} - {resultado[i][1]}")
            ids.append(resultado[i][0])
        animal_tutelar = int(input("qual voce quer adotar? "))
        cursor.execute("UPDATE animais SET fk_tutores = %s WHERE id_animais = %s",(id_tutores,ids[animal_tutelar-1]))
        conexao.commit()
        print(f"{resultado[animal_tutelar-1][1]} adotado! ")
    def destutelarAnimal():
        cursor.execute("select id_animais, nome, fk_tutores from animais")
        resultado = cursor.fetchall()
        ids=[]
        id_tutores=Tutor.login()
        print("que segue a lista de dos animais em sua tutela: ")
        for i in range(len(resultado)):
            if resultado[i][2]== id_tutores:
                print(f"{i+1} - {resultado[i][1]}")
                ids.append(resultado[i][0])
        animal_destutelar=int(input("qual animal voce quer destutelar? "))
        cursor.execute("UPDATE animais SET fk_tutores = NULL WHERE id_animais = %s",(ids[animal_destutelar-1],))
        conexao.commit()
# Tutor.login()
# Tutor.tutelarAnimal()
if __name__ == "_tutor__":
    Tutor.destutelarAnimal()
conexao.close() 