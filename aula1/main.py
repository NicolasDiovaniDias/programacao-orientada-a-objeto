class Conta:
    def __init__(self,saldo,numero):
        self.numero=numero
        self.saldo=saldo
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

def retorno():
    saldo=int(input("quanto voce quer de saldo? "))
    numero=int(input("quanto voce quer de numero? "))
    return (saldo,numero)
if __name__ == '__main__':
    numero,saldo=retorno()
    conta_nicolas=Conta(saldo,numero)
    conta_nicolas.listar()
    deposito=int(input("quanto voce quer depositar? "))
    conta_nicolas.depositar(deposito)
