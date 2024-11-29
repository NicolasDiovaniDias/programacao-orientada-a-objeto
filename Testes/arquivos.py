
#le o arquivo todo
with open("nicolas.txt","r") as nicolas:
    ler = nicolas.read()
print(ler)
#le linha por linha e as coloca em uma lista, assim podendo pegar linha por linha, o utf-8 permite que vc coloque caracteres especiais
with open("nicolaslinhas.txt","r", encoding="utf-8") as nicolas:
    linhas = nicolas.readlines()
print(linhas)
# muda oq estiver escrito dentro do arquivo para oq voce definir
with open("melzinha.txt", "w") as arquivo:
    arquivo.write("super gordinha")
# adiciona oq voce definir
with open("gatos.txt", "a") as arquivo:
    for i in range(10):
        arquivo.write("super gordinha\n")