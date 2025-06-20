Num = int (input('Digite um numero:'))
Num2 = float (input ('Digite outro numero:'))
soma = Num + Num2
print ('a soma vale {}'.format(soma)) #format é mais facil de se usar
print ('a soma vale', soma)# se usa ',' pra concatenar tipos de dados diferentes, e '+' se usa para concatenar strings
print ('a soma vale ' + str(soma)) # transforma a variavel soma em uma string
print(' a soma entre {} e {} vale {}'.format(Num, Num2, soma))