# Enunciado do Exercício:
# Crie um sistema simples de gerenciamento de uma transportadora utilizando programação orientada a objetos em Python.
# Requisitos:
# Classe Caminhão:
# Atributos: modelo, placa, capacidade_carga.

# Métodos: carregar(peso), descarregar(peso). O método carregar deve verificar se o peso a ser carregado não excede a capacidade do caminhão.

# Classe Motorista:
# Atributos: nome, idade, CNH. dataValidade

# Métodos: dirigir(caminhao). Este método deve imprimir uma mensagem indicando que o motorista está dirigindo o caminhão.
# verificarValidade(motorista)

# Associação entre as classes:
# Um caminhão deve ser dirigido por apenas um motorista.
# Um motorista pode dirigir vários caminhões.
# Exercícios:
# Crie pelo menos 3 objetos da classe Caminhão e 2 objetos da classe Motorista.
# Atribua um motorista a cada caminhão.
# Simule a carga e descarga de um caminhão.
# verifique se a CNH do Motorista é stá valida, caso estiver para vencer em 30 dias ou vencida verificar se o motorista está associado a um caminhão e avisar para renovar a CNH
# Imprima na tela informações sobre os caminhões e seus respectivos motoristas.
# Dicas:
# Utilize a associação entre as classes para conectar um objeto caminhão a um objeto motorista.
# Explore os métodos de cada classe para simular as ações da transportadora.
# Utilize a orientação a objetos para modelar o problema de forma clara e organizada.
# Exemplo de saída:
# Caminhão:
#   Modelo: Mercedes Benz
#   Placa: AAA-1234
#   Capacidade de carga: 10000 kg
#   Motorista: João Silva
#   Carga atual: 5000 kg

# Caminhão:
#   ...
# Desafios:
# Adicione um atributo "carga_atual" à classe Caminhão para controlar o peso carregado.
# Implemente um método para calcular o frete de um transporte com base na distância e no peso da carga.
# Crie uma classe "Viagem" para armazenar informações sobre as viagens realizadas pelos caminhões.
# Este exercício tem como objetivo:
# Fortalecer a compreensão sobre a associação entre classes em Python.
# Aplicar os conceitos de programação orientada a objetos em um cenário real.
# Desenvolver a lógica de programação e a capacidade de resolver problemas.
# Bons estudos!
# Observações:
# Este enunciado pode ser adaptado para níveis de complexidade diferentes, adicionando mais classes, atributos e métodos.
# Incentive os alunos a utilizarem boas práticas de programação, como nomes de variáveis e funções significativos, comentários e formatação do código.
# Possíveis extensões:
# Adicionar uma classe "Cliente" para representar os clientes da transportadora.
# Implementar um sistema de login para os motoristas.
# Criar um relatório com as informações de todos os caminhões e motoristas.
# Com este exercício, os alunos poderão explorar os conceitos de orientação a objetos de forma prática e divertida, aplicando seus conhecimentos para criar um sistema simples, mas funcional.
import re
import os
from datetime import datetime as dt
class caminhao:
    def __init__(self,modelo, placa, capacidade, carga_atual):
        self.modelo=modelo
        self.placa=placa
        self.capacidade=capacidade
        self.carga_atual=carga_atual
        self.motorista=None
    def carregar_peso(self):
        if(self.capacidade>self.carga_atual+10):
            print("voce não pode ultrapassar o limite de peso")
        self.carga_atual+=10
    def descarregar_peso(self):
        if self.carga_atual==0:
            print("voce ja esvaziou todo o caminhao")
        self.carga_atual-=10
    def definir_proprietario(self, pessoa):
        self.motorista=pessoa
    def listar(self):
        print(f'''
        modelo: {self.modelo}
        placa: {self.placa}
        capacidade: {self.capacidade}
        carga atual: {self.carga_atual}
        ''')
        
class motorista:
    def __init__(self,nome, idade, cnh, data_validade, caminhoes):
        self.nome=nome
        self.idade=idade
        self.cnh=cnh
        self.data_validade=data_validade
        self.caminhoes=[]
    def adicionar_caminhao(self,caminhao):
        self.caminhoes.append(caminhao)
    def dirigir(self):
        print(f"{self.nome} esta dirigindo!")
    def listar(self):
        print(f'''
        nome: {self.nome}
        idade: {self.idade}
        cnh: {self.cnh}
        data de validade: {self.data_validade}
        caminhoes:
        ''')
        for i in range(len(self.caminhoes)):
            self.caminhoes[i].listar()
caminhao1=caminhao("caminhoneta","red4453",210,180)
caminhao2=caminhao("carreta","sdf8923",200,150)
caminhao3=caminhao("carretao","gfe2323",210,190)
motorista1=motorista("jair",54,"possui","23092026",[caminhao1,caminhao2])
motorista2=motorista("carlos",64,"possui","22052030",[caminhao3])
motorista1.adicionar_caminhao(caminhao1)
motorista1.adicionar_caminhao(caminhao2)
motorista2.adicionar_caminhao(caminhao3)
caminhao1.carregar_peso()
caminhao1.carregar_peso()
caminhao1.carregar_peso()
caminhao1.carregar_peso()
motorista1.listar()
motorista2.listar()
