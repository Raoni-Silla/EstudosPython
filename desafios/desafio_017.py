import random
a1 = str(input('Digite o nome do aluno 1:'))
a2 = str (input('Digite o nome do aluno 2:'))
a3 = str(input('Digite o nome do aluno 3:'))
a4 = str(input('digite o nome do aluno 4:'))
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista) #escolhe um da lista
print('o aluno escolhido para apagar o quadro é: {}'.format(escolhido))