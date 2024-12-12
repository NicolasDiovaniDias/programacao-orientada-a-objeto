import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='animais_esperanca',
)

cursor=conexao.cursor()
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
        print(f"o animal {self.nome} esta emitindo som")
        
def retorno():
    nome = input(f"qual o nome do animal? ")
    while True:
        especie= input(f"qual a especie do(a) {nome} ?\n1-cão\n2-gato ")
        if especie=="1":
            especie="cão"
            break
        elif especie=="2":
            especie="gato"
            break
        print("valor invalido")
    raca = input(f"qual a raca do(a) {nome} ? ") 
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
    cursor.execute("SELECT id_abrigos,nome FROM abrigos")
    resultado = cursor.fetchall()  
    while True:
        check=False
        for i in range(len(resultado)):
            print(f'{resultado[i][0]} - {resultado[i][1]}')
        abrigo = input(f"em que abrigo o(a) {nome} esta ?")
        try:
            numero=int(abrigo)
            for i in range(len(resultado)):
                if resultado[i][0]==int(abrigo):
                    check=True
            if check==True:
                break
            print("valor invalido")
        except:
            print("valor invalido")
            
    
    return (nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo)

def enviar_banco():
    nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo = retorno()
    animal1=Animal(nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo)
    cursor.execute("INSERT INTO animais (nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo))
    id = cursor.lastrowid
    cursor.execute("INSERT INTO historico (historico) values(%s)",(f'o animal {animal1.nome} do id: {id} foi inserido',))
    conexao.commit()
    if animal1.especie == "cão":
        import cao
        cao.passar_argumentos(animal1,id)
    elif animal1.especie == "gato":
        import gato
        gato.passar_argumentos(animal1,id)
    return animal1
    
def toString():
    pesquisa_animal=input("qual o nome do animal que voce quer ver os dados? ")
    cursor.execute("SELECT id_animais, nome, raca, especie, genero, idade, localResgatado, resgatador, abrigo FROM animais WHERE nome = %s",(pesquisa_animal,))
    resultado = cursor.fetchall()    
    if len(resultado)==0:
        print("nenhuma animal encontrado! ")
    elif len(resultado)==1: 
        print(f'''
            {'nome:' :<16}{resultado[0][1]}
            {'raca:' :<16}{resultado[0][2]}
            {'especie:' :<16}{resultado[0][3]}
            {'genero:' :<16}{resultado[0][4]}
            {'idade:' :<16}{resultado[0][5]}
            {'LocalResgatado:' :<16}{resultado[0][6]}
            {'resgatador:' :<16}{resultado[0][7]}
            {'abrigo:' :<16}{resultado[0][8]}
            ''')
    else:
        print("foram encontrados mais de uma animal com esse nome")
        for i in range(len(resultado)):
            print(f'''
                    {'nome:' :<16}{resultado[i][1]}
                    {'raca:' :<16}{resultado[i][2]}
                    {'especie:' :<16}{resultado[i][3]}
                    {'genero:' :<16}{resultado[i][4]}
                    {'idade:' :<16}{resultado[i][5]}
                    {'LocalResgatado:' :<16}{resultado[i][6]}
                    {'resgatador:' :<16}{resultado[i][7]}
                    {'abrigo:' :<16}{resultado[i][8]}''')
    # print(f"nome: {self.nome}\nraça: {self.raca}\nespecie: {self.especie}\ngenero: {self.genero}\nidade: {self.idade}\nlocalResgatado: {self.localResgatado}\nresgatador: {self.resgatador}\nabrigo: {self.abrigo}")
if __name__ == "__main__":
    animal1=enviar_banco()
    # toString()   
    # animal1.comer()     
    # janela = Tk()
    # janela.mainloop()
    # data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(data_hora)
    # cursor.execute("INSERT INTO historico (historico, data)values('aaaaaaaaaaaaaaa nicolas',%s)",(data_hora,))
    conexao.commit()
    conexao.close()