
#o termo arquivo guarda as informações do txt dentro da variavel arquivo
#o read serve pra leituras simples, informações unicas, senhas e tokens, emails
#read pega as informações de um arquivo txt e transforma em uma string tudo junto
#o with é um metodo que serve para abrir e fechar arquivos automaticamente
# with open (nome do arquivo, objetivo) as nome do arquivo que recebe as informações do arquivo txt
with open("email.txt", "r", encoding="utf-8") as arquivo:
    email = arquivo.read()
print(email)
# o readline cria uma lista, em que cada item da lista é uma linha
with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
    mensagem = arquivo.readlines()
    for linha in mensagem:
        if "python" in linha:
            print(mensagem)
print(mensagem)
#WRITE CRIA E SUBSTITUI ARQUIVOS DE TEXTOS QUE JA EXISTEM
with open ("senha.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("456789")

with open ("senha_nova.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("456789")

#append serve pra adicionar coisas novas no arquivo txt
with open ("email.txt", "a", encoding="utf-8") as arquivo:
  arquivo.write("\nraonisilla@hotmail.com")#coloca o \n pra quebrar a linha e colocar oque foi adicionado na linha de baixo do txt

