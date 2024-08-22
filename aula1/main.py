class Conta:
    numero:"000"
    saldo:0.0
    def listar(self):
        print(self.numero)
        print(self.saldo)
if __name__ == '__main__':
    conta_nicolas = Conta()
    conta_nicolas.numero="100"
    conta_nicolas.saldo=1000000
    conta_nicolas.listar()
    conta_pedro = Conta()
    conta_pedro.numero = "200"
    conta_pedro.saldo = 200
    conta_pedro.listar()