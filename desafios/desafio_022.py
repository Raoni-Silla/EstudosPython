city = str(input('qual é a sua cidade: '))
city_lower = city.lower()
divido = city_lower.split()
teste = 'santo' in divido[0]
print('é {} que sua cidade começa com o nome santo'.format(teste))