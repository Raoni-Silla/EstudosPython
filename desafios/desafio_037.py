print('-=-' * 20)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2 :
    print('O primeiro numero {} > {}'.format(n1,n2))
elif n1 == n2 :
    print('Os dois são iguais {} = {}'.format(n1,n2))
else:
    print('o segundo numero digitado {} > {}'.format(n2,n1))
print('-=-' * 20)