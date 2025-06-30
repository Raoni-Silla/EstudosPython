print('\033[0;33;44;m-=-\033[m' * 20 )
print('\033[0;36;40mAnalisador de triangulos\033[m')
print('-=-' * 20)
r1 = int(input('digite o valor da reta[1]: '))
r2 = int(input('digite o valor da reta[2]: '))
r3 = int(input('digite o valor da reta[3]: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('os segmentos podem formar um triangulo')
else:
    print('eles nao podem formar um triangulo')
