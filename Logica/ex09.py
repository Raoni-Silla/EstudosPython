frase = 'curso em video'
print(frase[3:13])
print(frase[:13])
print(frase[2:])
print(frase[2::2])
print(frase.upper())
print("""ola mundo, mostra na tela textos grandes usando 3 aspas duplas""")
print(frase.count('o'))
print(len(frase.strip()))
print(frase.replace('video','urso'))
print(frase)#ele não substitui na variavel, apenas na instancia, se quiser salvar a modificação deve mudar a variavel
frase = frase.replace('video','urso')
print(frase)
print('curso' in frase)
print(frase.lower().find('video'))
print(frase.split())
divido = frase.split()
print(divido [0])#mostra o primeiro item da lista
print(divido[2][2])#pega o dividio 2 e mostra a segunda letra

