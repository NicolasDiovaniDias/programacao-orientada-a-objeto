class Veiculo:
    def __init__(self, marca, modelo, ano, preco_diaria, dias):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.preco_diaria=preco_diaria
        self.dias=dias
    def Dias(self):
        self.dias=int(input("quantos dias voce usou o veiculo? "))
    def Calcular_aluguel(self):
        print(f"o aluguel ficou {self.preco_diaria*self.dias} !")