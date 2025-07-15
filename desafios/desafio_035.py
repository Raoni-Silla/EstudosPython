import time
print('-=-' * 20)
print('Inicializando Sistema')
print('-=-' * 20)
print('Sistema De Calculo Iniciado'),
print('-=-' * 20)
time.sleep( 2)
sal = float(input('Digite o valor do seu salario: '))
valorCasa = float(input('Digite o valor da casa: '))
anos = int(input('Digite a quantidade de anos em que você deseja pagar: '))
print('-=-' * 20)
print('Calculando valor da prestação.......')
time.sleep(3)
print('-=-' * 20)
mensal = valorCasa / 12
print('O preço da prestação mensal ficaria em : {}'.format(mensal))
print('Vamos calcular se isso esta dentro do que vocễ pode pagar: ')
excedente = sal - (sal * 30/100)
if excedente > mensal:
    print('Tudo Certo, Podemos continuar seu emprestimo')
elif mensal > excedente:
    print('Infelizmente não poderemos aprovar sua solicitação, pois a parcela mensal excede 30 % do seu salario')
else:
    print('error')
print('-=-' * 20)