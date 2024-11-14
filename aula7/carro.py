import veiculo

class Carro(veiculo.Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, dias, num_portas):
        self.num_portas=num_portas
        super().__init__(marca, modelo, ano, preco_diaria, dias)
    def Calcular_aluguel(self):
        if self.dias>7:
            print(f"o aluguel ficou {(self.preco_diaria*self.dias)*0.90} !")
        else:
            print(f"o aluguel ficou {self.preco_diaria*self.dias} !")