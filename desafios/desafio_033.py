sal = float (input('Digite o seu salario funcionario: '))
if sal > 1.250:
    print('seu novo salario é {},com aumento de 10%'.format(sal + (sal * 10/100)))
else:
    print('seu novo salario é {},com aumento de 15%'.format(sal + (sal * 15 / 100)))

