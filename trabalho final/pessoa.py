import mysql.connector
from datetime import datetime
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="animais_esperanca"
)
cursor = conexao.cursor()
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome=nome
        self.cpf=cpf
        self.telefone=telefone
def registrar_pessoa():
        nome=input("qual o seu nome? ")
        telefone=input("qual o seu telefone? ")
        cpf=input("qual o seu cpf? ")
        email=input("qual é seu gmail? ")
        while True:
            senha=input("qual vai ser sua senha? ")
            repeat_senha=input("repita sua senha: ")
            if(senha==repeat_senha):
                print("usuario cadastrado!")
                cursor.execute("INSERT INTO pessoas (nome, telefone, cpf, email, senha) VALUES(%s,%s,%s,%s,%s)",(nome, telefone, cpf, email, senha))
                id = cursor.lastrowid
                cursor.execute("INSERT INTO historico (historico) values(%s)",(f'a pessoa {nome}({id}) foi inserida',))
                conexao.commit()
                break
            else:
                print("valores diferentes! ")
def login():
        print("##LOGIN##")
        while True:
            email=input("qual seu email? ")
            cursor.execute("SELECT email, senha, id_pessoas FROM pessoas WHERE email = %s",(email,))
            resultado = cursor.fetchall()
            if(len(resultado)!=0):
                senha=input("digite sua senha: ")
                for i in range(len(resultado)):
                    if(resultado[i][1]==senha):
                        print("acesso liberado")
                        return resultado[i][2]
            else:
                print("email inexistente")
def adotar_animal():
    cursor.execute("SELECT id_animais, nome, idade, especie, raca, fk_pessoas, situacao FROM animais")
    resultado = cursor.fetchall()
    id_pessoas=login()
    ids=[]
    print(resultado)
    print("segue a lista de dos animais para adoção: ")
    for i in range(len(resultado)):
        if resultado[i][0]is not None and resultado[i][5]!=id_pessoas and resultado[i][6] == "A":
            print(f"{i+1} - {resultado[i][1]}")
            ids.append(resultado[i][0])
        else:
            ids.append("indisponivel")
    while True:
        animal_adotar=int(input("qual animal você quer adotar? "))
        for i in range(len(resultado)):
            if ids[animal_adotar-1] == "indisponivel":
                print("valor invalido")
                break
            if len(ids)<animal_adotar-1:
                if teste==True:
                    print("valor invalido!")
                    teste=False
            if len(ids)>animal_adotar-1 or resultado[animal_adotar-1][5] is not None:
                cursor.execute("UPDATE animais SET situacao = 'I', fk_tutores = NULL WHERE id_animais = %s;",(resultado[animal_adotar-1][0],))    
                cursor.execute("INSERT INTO animais_adotados (nome, idade, especie, raca, fk_pessoas) VALUES(%s,%s,%s,%s,%s)",(resultado[animal_adotar-1][1],resultado[animal_adotar-1][2],resultado[animal_adotar-1][3],resultado[animal_adotar-1][4],id_pessoas ))
                cursor.execute("UPDATE animais SET fk_pessoas = %s WHERE id_animais = %s", (id_pessoas, ids[animal_adotar-1]))
                print(f"{resultado[animal_adotar-1][1]} adotado")
                cursor.execute("SELECT id_pessoas, nome FROM pessoas WHERE id_pessoas = %s", (id_pessoas,))
                nome_tutor = cursor.fetchone()
                cursor.execute("SELECT id_animais, nome FROM animais WHERE id_animais = %s", (ids[animal_adotar-1],))
                nome_animal = cursor.fetchone()
                cursor.execute("INSERT INTO historico (historico) values(%s)",(f'o animal {nome_animal[1]} ({nome_animal[0]}) foi adotado por {nome_tutor[1]} ({nome_tutor[0]})',))
                conexao.commit()
                return
            else:
                print("nicolas")
registrar_pessoa()
# adotar_animal()
    