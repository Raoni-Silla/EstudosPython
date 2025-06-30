km = float(input('Digite a distância de uma viagem em km: '))
if km <= 200:
    print('o preço da sua viagem é R$ {:.2f}'.format(0.50 * km))
else:
    print('o preço da sua viagem é R$: {:.2f}'.format(0.45 * km))