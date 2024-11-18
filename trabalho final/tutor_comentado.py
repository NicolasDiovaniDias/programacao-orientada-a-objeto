import mysql.connector  # Importa o módulo para conectar ao banco de dados MySQL

# Configura a conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",  # Endereço do servidor MySQL
    user="root",       # Nome do usuário do MySQL
    password="",       # Senha do usuário do MySQL
    database="animais_esperanca"  # Nome do banco de dados
)
cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL

# Define a classe Tutor para representar tutores no sistema
class Tutor():
    # Construtor da classe que inicializa os atributos do tutor
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    # Método para registrar um novo tutor
    def registrar_tutor():
        nome = input("Qual o seu nome? ")  # Solicita o nome do tutor
        telefone = input("Qual o seu telefone? ")  # Solicita o telefone do tutor
        endereço = input("Qual o seu endereço? ")  # Solicita o endereço do tutor
        email = input("Qual é seu email? ")  # Solicita o email do tutor
        
        # Loop para validar se a senha foi confirmada corretamente
        while True:
            senha = input("Qual vai ser sua senha? ")  # Solicita a senha
            repeat_senha = input("Repita sua senha: ")  # Solicita a confirmação da senha
            if senha == repeat_senha:  # Verifica se as senhas são iguais
                print("Usuário cadastrado!")  # Exibe mensagem de sucesso
                # Insere os dados do tutor na tabela 'tutores'
                cursor.execute("INSERT INTO tutores (nome, telefone, endereco, email, senha) VALUES(%s,%s,%s,%s,%s)", 
                               (nome, telefone, endereço, email, senha))
                conexao.commit()  # Confirma a transação
                break
            else:
                print("Valores diferentes!")  # Exibe mensagem de erro

    # Método para realizar login de um tutor
    def login():
        print("##LOGIN##")  # Exibe o cabeçalho do login
        while True:
            email = input("Qual seu email? ")  # Solicita o email do tutor
            # Consulta o banco para verificar se o email existe
            cursor.execute("SELECT email, senha, id_tutores FROM tutores WHERE email = %s", (email,))
            resultado = cursor.fetchall()  # Obtém os resultados da consulta
            if len(resultado) != 0:  # Verifica se há resultados
                senha = input("Digite sua senha: ")  # Solicita a senha
                for i in range(len(resultado)):
                    if resultado[i][1] == senha:  # Verifica se a senha está correta
                        print("Acesso liberado")  # Exibe mensagem de sucesso
                        return resultado[i][2]  # Retorna o ID do tutor logado
            else:
                print("Email inexistente")  # Exibe mensagem de erro

    # Método para associar um tutor a um animal
    def tutelarAnimal():
        # Consulta os animais disponíveis no banco
        cursor.execute("SELECT id_animais, nome FROM animais")
        resultado = cursor.fetchall()  # Obtém os resultados da consulta
        print("Que bom que você quer ser o tutor de um dos nossos animais, aqui segue a lista de animais. Primeiro faça login: ")
        ids = []  # Lista para armazenar os IDs dos animais
        id_tutores = Tutor.login()  # Realiza o login do tutor
        
        # Exibe a lista de animais disponíveis
        for i in range(len(resultado)):
            print(f"{i+1} - {resultado[i][1]}")  # Exibe o índice e o nome do animal
            ids.append(resultado[i][0])  # Armazena o ID do animal na lista
        
        animal_tutelar = int(input("Qual você quer adotar? "))  # Solicita a escolha do animal
        # Atualiza o registro do animal para associá-lo ao tutor
        cursor.execute("UPDATE animais SET fk_tutores = %s WHERE id_animais = %s", (id_tutores, ids[animal_tutelar-1]))
        conexao.commit()  # Confirma a transação
        print(f"{resultado[animal_tutelar-1][1]} adotado! ")  # Exibe mensagem de sucesso

    # Método para desassociar um tutor de um animal
    def destutelar_animal():
        # Consulta os animais e seus tutores
        cursor.execute("SELECT id_animais, nome, fk_tutores FROM animais")
        resultado = cursor.fetchall()  # Obtém os resultados da consulta
        id_tutores = Tutor.login()  # Realiza o login do tutor
        
        print("Segue a lista dos animais em sua tutela: ")
        # Exibe os animais que estão sob tutela do tutor logado
        for i in range(len(resultado)):
            if resultado[i][2] == id_tutores:  # Verifica se o tutor é o responsável pelo animal
                print(f"{i+1} - {resultado[i][1]}")  # Exibe o índice e o nome do animal
        
        animal_destutelar = int(input("Qual animal você quer destutelar? "))  # Solicita a escolha do animal
        # Atualiza o registro do animal para remover o tutor associado
        cursor.execute("UPDATE animais SET fk_tutores = NULL WHERE id_animais = %s", (resultado[animal_destutelar-1][0],))
        conexao.commit()  # Confirma a transação

# Exemplo de chamada de métodos (descomente para executar)
# Tutor.login()
# Tutor.destutelar_animal()

# Fecha a conexão com o banco de dados
conexao.close()
