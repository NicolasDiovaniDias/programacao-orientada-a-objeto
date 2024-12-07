import mysql.connector
from datetime import datetime
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
                id = cursor.lastrowid
                cursor.execute("INSERT INTO historico (historico) values(%s)",(f'o tutor {nome}({id}) foi inserido',))
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
        cursor.execute("SELECT id_animais, nome, fk_tutores, situacao FROM animais")
        resultado = cursor.fetchall()
        id_tutores=Tutor.login()
        ids=[]
        print("segue a lista de dos animais para tutela: ")
        for i in range(len(resultado)):
            if resultado[i][0]is not None and resultado[i][2]!=id_tutores and resultado[i][3] == "A":
                print(f"{i+1} - {resultado[i][1]}")
                ids.append(resultado[i][0])
            else:
                ids.append("indisponivel")
        if not ids:
            print("não tem nenhum animal disponivel! ")
            return
        while True:
            animal_tutelar=int(input("qual animal você quer tutelar? "))
            teste=True
            for i in range(len(resultado)):
                if ids[animal_tutelar-1] == "indisponivel":
                    print("valor invalido")
                    break
                if len(ids)<animal_tutelar-1:
                    if teste==True:
                        print("valor invalido!")
                        teste=False
                elif resultado[animal_tutelar-1][2] != id_tutores or resultado[animal_tutelar-1][2] is None:
                    if resultado[animal_tutelar-1][2] is not None:
                        print("o animal já tem tutor")
                        break
                    print(f"{resultado[animal_tutelar-1][1]} tutelado(a)")
                    
                    cursor.execute("UPDATE animais SET fk_tutores = %s WHERE id_animais = %s", (id_tutores, ids[animal_tutelar-1]))
                    cursor.execute("SELECT id_tutores, nome FROM tutores WHERE id_tutores = %s", (id_tutores,))
                    nome_tutor = cursor.fetchone()
                    cursor.execute("SELECT id_animais, nome FROM animais WHERE id_animais = %s", (ids[animal_tutelar-1],))
                    nome_animal = cursor.fetchone()
                    cursor.execute("INSERT INTO historico (historico) values(%s)",(f'o animal {nome_animal[1]} ({nome_animal[0]}) foi tutelado por {nome_tutor[1]} ({nome_tutor[0]})',))

                    conexao.commit()
                    return
                elif resultado[animal_tutelar-1][2] == id_tutores:
                    print("esse animal já esta sobre sua tutela! ")
                    return
                
    def destutelarAnimal():
        cursor.execute("SELECT id_animais, nome, fk_tutores FROM animais")
        resultado = cursor.fetchall()
        id_tutores=Tutor.login()
        print(resultado, id_tutores)
        ids=[]
        print("segue a lista de dos animais em sua tutela: ")
        for i in range(len(resultado)):
            if resultado[i][2]== id_tutores:
                print(f"{i+1} - {resultado[i][1]}")
                ids.append(resultado[i][0])
        if not ids:
            print("voce não tem nenhum animal em sua tutela! ")
            return()   
        while True:    
            animal_destutelar=int(input("qual animal você quer destutelar? "))
            teste=True
            for i in range(len(resultado)):
                if len(ids)<animal_destutelar-1:
                    if teste==True:
                        print("valor inválido!")
                        teste=False
                elif resultado[animal_destutelar-1][2] == id_tutores:
                    print(f"{resultado[i][1]} destutelado")
                    cursor.execute("UPDATE animais SET fk_tutores = NULL WHERE id_animais = %s",(ids[animal_destutelar-1],))
                    cursor.execute("SELECT id_tutores, nome FROM tutores WHERE id_tutores = %s", (id_tutores,))
                    nome_tutor = cursor.fetchone()
                    cursor.execute("SELECT id_animais, nome FROM animais WHERE id_animais = %s", (ids[animal_destutelar-1],))
                    nome_animal = cursor.fetchone()
                    cursor.execute("INSERT INTO historico (historico) values(%s)",(f'o animal {nome_animal[1]} ({nome_animal[0]}) foi destutelado por {nome_tutor[1]} ({nome_tutor[0]})',))

                    conexao.commit()
                    return
            print("esse animal não está sobre sua tutela")
# Tutor.registrar_tutor()
# Tutor.login()
Tutor.tutelarAnimal() 
# Tutor.destutelarAnimal()
conexao.close() 
#vou jogar com o leo, resolver problema da verificação se o tutor n esta destutelando o animal de outro tutor
