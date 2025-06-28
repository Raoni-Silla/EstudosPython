frase = str(input('Digite uma frase: '))
fraseMin = frase.strip().lower()
print('a letra [a] aparece {} vezes \n aparecendo na posição {} pela primeira vez'.format(fraseMin.count('a'), frase.find('a')))
print('aparecendo na ultima posição {}'.format(fraseMin.rfind('a') ))

