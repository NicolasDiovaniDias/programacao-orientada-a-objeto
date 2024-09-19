# Exercício: Classe Televisão
# Objetivo:
# Criar uma classe em linguagem de programação em Python para representar uma televisão. A classe deve ter os seguintes atributos e métodos:
# Atributos:
# modeloTV: String - representa o modelo da televisão
# canal: Inteiro - representa o canal atual
# volume: Inteiro - representa o volume atual
# estado: String - representa o estado da televisão ("ligada" ou "desligada")
# Métodos:
# __init__: método construtor (estado inicial = desligada)
# ligar(): Liga a televisão e define o canal e volume para valores iniciais (especificar os valores iniciais)
# desligar(): Desliga a televisão
# aumentarVolume(): Aumenta o volume em 1 unidade (ou valor customizável)
# diminuirVolume(): Diminui o volume em 1 unidade (ou valor customizável)
# trocarCanal(novoCanal): Muda o canal para o novoCanal (especificar se o canal tem um limite máximo)
# Instruções:
# Crie a classe Televisao com os atributos e métodos descritos.
# Implemente cada método de acordo com sua funcionalidade.
# Crie um objeto Televisao e utilize os métodos para testar a funcionalidade da classe.
# Demonstre como a classe pode ser utilizada em um programa simples, como um menu interativo para controlar a televisão.
# Dicas:
# Utilize comentários para explicar o código e facilitar a compreensão.
# Teste a classe com diferentes valores de entrada para garantir que ela funcione corretamente.
# Explore a possibilidade de adicionar outros atributos e métodos à classe, como controle de brilho, seleção de entrada (HDMI, antena, etc.) e ajuste de imagem.
# Observações:
# Este exercício é direcionado para alunos em introdução à Programação Orientada a Objetos.
# O nível de detalhamento da implementação pode variar de acordo com o conhecimento prévio dos alunos e da linguagem de programação utilizada.
# O professor pode fornecer instruções adicionais ou modificar o enunciado para atender às necessidades específicas da turma.
class Tv:
    def __init__(self,modelo,canal,volume,estado):
        self.modelo=modelo
        self.canal=canal
        self.volume=volume
        self.estado=estado
    canal=0
    volume=0
    def ligar(self):
        self.estado="ligada"
    def desligar(self):
        self.estado="desligada"
    def aumentar_volume(self):
        self.volume+=1 
    def diminuir_volume(self):
        self.volume-=1
    