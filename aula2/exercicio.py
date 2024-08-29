class Automovel:
    def __init__(self, marca, modelo, cilindrada, num_portas, cor, marcha, sentido):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.num_portas = num_portas
        self.cor = cor
        self.velocidade = 0  # Inicializa a velocidade como zero
        self.marcha = marcha
        self.sentido = sentido
    def acelerar(self):
        if(self.marcha!="R"):
            self.velocidade += 10 * self.marcha
        print(f"O automóvel {self.marca} {self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h")
    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
            print(f"O automóvel {self.marca} {self.modelo} freou. Velocidade atual: {self.velocidade} km/h")
        else:
            print("O automóvel já está parado.")
    def parar(self):
        self.velocidade = 0
        print(f"O automóvel {self.marca} {self.modelo} parou. Velocidade atual: {self.velocidade} km/h")
    def situacao(self):
        if self.velocidade>0:
            print(f'o automovel {self.marca} {self.modelo} esta a {self.velocidade} km/h')
        else:
            print(f'o automovel {self.marca}{self.modelo} esta parado')
    def marcha_mais(self):
        if(self.marcha=="R"):
            self.marcha=1
        else:
            self.marcha+=1
        print(f'a marcha do carro esta em {self.marcha}')
    def marcha_menos(self):
        if(self.marcha=="R"):
            print("o carro ja esta em Ré")
        elif(self.marcha==1):
            self.marcha="R"
        else:
            self.marcha-=1
        print(f'a marcha do carro esta em {self.marcha}')
    def sentido(self):
        if(self.velocidade>0):
            self.sentido="frente"
        elif(self.velocidade<0):
            self.sentido="tras"
        else:
            self.sentido="parado"
        if(self.sentido=="parado"):
            print(f"o carro esta{self.sentido}")
        else:
            print(f"o carro esta andando pra {self.sentido}")
        


# Exemplo de inicialização de objetos e uso dos métodos
carro1 = Automovel("Toyota", "Corolla", 2000, 4, "Prata","R","parado")
carro2 = Automovel("Honda", "Civic", 1800, 4, "Preto","R","parado")
carro1.marcha_mais()
carro2.marcha_mais()
carro2.marcha_mais()
carro2.marcha_mais()
carro2.marcha_mais()
carro2.marcha_mais()
carro2.marcha_mais()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.parar()
carro2.acelerar()
carro2.acelerar()
carro2.acelerar()
carro2.acelerar()
carro2.acelerar()
carro2.frear()
carro2.frear()
carro1.situacao()
carro2.situacao()