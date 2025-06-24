from math import hypot
print('-------------------------------------------------------')
print('calculo de catetos de um triangulo-retangulo')
print('--------------------------------------------------------')
opt = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento de um cateto adjacente: '))
print('a hipotenusa desse triangulo é: {:.2f}'.format(hypot(opt,adj)))