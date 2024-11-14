import mysql.connector
from mysql.connector import Error
try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Adicione sua senha aqui
        database='animais_esperanca'  # Certifique-se de que o banco 'usuarios' já existe
    )

    if conexao.is_connected():
        cursor = conexao.cursor()

        # SQL para criar a tabela `usuario`
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Animais (
            id_animais INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            raca VARCHAR(50) NOT NULL,
            especie VARCHAR(50) NOT NULL,
            genero VARCHAR(1) NOT NULL,
            idade VARCHAR(2) NOT NULL,
            localResgatado VARCHAR(50) NOT NULL,
            resgatador VARCHAR(50) NOT NULL,
            abrigo VARCHAR(50) NOT NULL
        );
        '''
        conexao.commit()
        # Executa o comando de criação da tabela
        cursor.execute(create_table_query)
        print("Tabela 'Animais' criada com sucesso.")

except Error as e:
    print(f"Erro ao conectar ou criar tabela: {e}")
if conexao.is_connected():
    cursor.close()
    conexao.close()