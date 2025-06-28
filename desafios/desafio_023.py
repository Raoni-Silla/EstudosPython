nome = str(input('Digite seu nome completo: '))
nome_min = nome.lower()
testeNome = 'silva' in nome_min
print('é {} que seu nome tem silva, começando na letra (lembre-se que começa do 0) {}'.format(testeNome, nome_min.find('silva')))