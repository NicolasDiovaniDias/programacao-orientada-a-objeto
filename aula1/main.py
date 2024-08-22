class Conta:
    numero:"000"
    saldo:0.0
    def listar(self):
        print(self.numero)
        print(self.saldo)
    def sacar(self,saque):
        self.saldo-=saque
        self.listar()
    def depositar(self,depositar):
        self.saldo+=depositar
        self.listar()

if __name__ == '__main__':
    conta_nicolas = Conta()
    conta_nicolas.numero="100"
    conta_nicolas.saldo=1000000
    conta_nicolas.listar()
    conta_pedro = Conta()
    conta_pedro.numero = "200"
    conta_pedro.saldo = 200
    conta_pedro.listar()
    deposito=int(input("quanto voce quer depositar? "))
    conta_nicolas.depositar(deposito)
