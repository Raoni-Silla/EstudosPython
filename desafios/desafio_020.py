nome = str(input('Digite qual é o seu nome completo: '))
print('Seu nome com todas as letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome com todas as letras minusculas: {}'.format(nome.lower()))
semEspaco = nome.replace(" ", "")
print('O total de letras que tem seu nome: {} '.format(len(semEspaco)))
primeiroNome = nome.split()
print('o seu primeiro nome tem {} letras'.format(len(primeiroNome[0])))


