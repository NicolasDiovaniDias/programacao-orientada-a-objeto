import random
# seed

class Automovel:
    #CLASSE AUTOMÓVEL COM MÉTODO CONSTRUTOR
    def __init__(self, marca, modelo, cilindrada, num_portas, cor):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.num_portas = num_portas
        self.cor = cor
        self.velocidade = 0 # Inicializa a velocidade como zero
        self.sentido = None

    def acelerar(self):
        if self.sentido:
            self.velocidade += 10
        else:
            self.velocidade +=1
        #print(f"O automóvel {self.marca} {self.modelo} está em movimento. Velocidade atual: {self.velocidade} km/h")
        print(self.velocidade)
    def frear(self):
        if self.sentido is True:
            if self.velocidade >= 10 :
                self.velocidade -= 10
         #   print(f"O automóvel {self.marca} {self.modelo} freou. Velocidade atual: {self.velocidade} km/h")
            else:
                print("O automóvel já está parado.")
        else:
            if self.velocidade >= 1 :
                self.velocidade -= 1
            else:
                 print("O automóvel já está parado.")
        print(self.velocidade,self.sentido)
    def parar(self):
        self.velocidade = 0
        print(f"O automóvel {self.marca} {self.modelo} parou. Velocidade atual: {self.velocidade} km/h")

    def situacao(self):
        if self.velocidade > 0:
            print(f"O automóvel {self.marca} {self.modelo} está em movimento, Velocidade atual: {self.velocidade} km/h")

        else:
            print("O automóvel está parado.")
        if self.sentido:
            print ("Andando para FRENTE")
        else:
            print ("Andando para trás (RÉ)")
    def mudarMarcha(self,marcha):
        if marcha=='R':
            self.sentido = False
            self.parar()
        elif self.velocidade >0 and self.sentido is False:
            self.parar()
            self.sentido= True
        else:
            self.sentido = True


# Exemplo de inicialização de objetos e uso dos métodos
carro1 = Automovel("Toyota", "Corolla", 2000, 4, "Prata")
carro2 = Automovel("Honda", "Civic", 1800, 4, "Preto")

marcha=random.randint(1,6)
if marcha == 6:
    marcha='R'
print(marcha)

carro1.mudarMarcha(marcha)

var=int(random.random()*30)
print(f"Vai acelerar {var} x")
for i in range(var):
    print("A")
    carro1.acelerar()
carro1.situacao()

var=int(random.random()*20)
print(f"Vai frear {var} x")
for i in range(var):
    print("F")
    carro1.frear()

carro1.situacao()