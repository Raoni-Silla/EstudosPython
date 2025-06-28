nome = str(input('digite seu nome: '))
nomeMin = nome.lower()
nomeMin = nomeMin.split()
print('seu primeiro nome é {} e seu ultimo nome é {}'.format(nomeMin[0], nomeMin[-1]))