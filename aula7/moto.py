import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, dias, cilindrada):
        self.cilindrada=cilindrada
        super().__init__(marca, modelo, ano, preco_diaria, dias)
    def Calcular_aluguel(self):
        if self.dias>7:
            print(f"o aluguel ficou {(self.preco_diaria*self.dias)*0.95} !")
        else:
            print(f"o aluguel ficou {self.preco_diaria*self.dias} !")