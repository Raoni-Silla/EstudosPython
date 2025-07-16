from datetime import date
hoje = date.today()
ano_atual = hoje.year
print('-=-' * 20)
print('Sistema de alistamento militar')
print('-=-' * 20)
nome = str(input('Digite seu nome: '))
nascimento = str(input('Digite seu dia e mes de nascimento: '))
anonasc = int(input('Digite o ano em que voce nasceu: '))
lista = [nascimento, anonasc]
print('-=-' * 20)
resto = ano_atual - anonasc
if resto == 18:
    print('Olá {}, a sua hora de cumprir com o dever militar chegou tendo sua data de nascimento em {}'.format(nome,lista))
elif resto > 18:
    excedente = resto - 18
    print('você{} é refratario, com atraso de {}'.format(nome,excedente))
else:
    print('Você {}, não precisa se alistar, faltando {} anos pra se alistar'.format(nome,18-resto))
print('-=-' * 20)