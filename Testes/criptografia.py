from cryptography.fernet import Fernet
# chave = Fernet.generate_key()
# with open('chave.key', 'wb') as filekey:
#     filekey.write(chave)
with open('chave.key', 'rb') as chave:
    filekey = chave.read()
fer = Fernet(filekey)
with open("melzinha.txt", "rb") as arquivo:
    conteudo = arquivo.read()
criptografado = fer.encrypt(conteudo)
with open("melzinha.txt","wb") as arquivo:
    arquivo.write(criptografado)
# with open("melzinha.txt","rb") as arquivo:
#     decrypt = arquivo.read()
# descriptografado = fer.decrypt(decrypt)
# with open("melzinhadecrypt.txt","wb") as arquivo:
#     arquivo.write(descriptografado)