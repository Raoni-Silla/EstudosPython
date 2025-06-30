n1 = int(input('Digite um numero[1]: '))
n2 = int(input('Digite um numero[2]: '))
n3 = int (input('Digite um numero[3]:'))
print('--------------------------------------------------------')
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print('maior: {}'.format(maior))
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print('menor: {}'.format(menor))

print('---------------------------------------------------------')