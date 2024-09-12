class Aluno:
    def __init__(self,nota1,nota2,nome):
        self.nota1=nota1
        self.nota2=nota2
        self.nome=nome
        # self.disciplina=disciplina
        # self.exame=exame
    nota1=0.0
    nota2=0.0
    nome=""
    # exame=None
    def media(self):
        media=(self.nota1+self.nota2)/2
        if(media>7):
            print(f"{self.nome} passou com media: {media}")
        else:
            print(f"{self.nome} reprovou com media: {media}")
        

def retorno():
    nota1=int(input("qual foi a primeira nota?"))
    nota2=int(input("qual foi a segunda nota?"))
    nome=input("qual o nome do aluno?")
    return(nota1,nota2,nome)
if __name__ == '__main__':
    nota1,nota2,nome=retorno()
    aluno_nicolas=Aluno(nota1,nota2,nome)
    
    aluno_nicolas.media()