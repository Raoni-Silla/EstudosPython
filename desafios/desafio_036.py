import time
print('-=-' * 20)
print('Sistema de calculo de base numericas iniciando.....')
time.sleep(3)
print('-=-' * 20)
print('Sistema de calculo iniciado com sucesso')
N = int(input('Digite Um Numero Que Deseja Converter: '))
print('Calculando pra bases hexadecimais, binarias e octal....')
print('Aguarde um instante')
time.sleep(3)
print('-=-' * 20)
resultado_bin = ""
resultado_oct = ""
resultado_hexa = ""
NB = N
NH = N
NC = N

while NB > 0:
    resto = int(NB % 2)
    NB = NB // 2
    resultado_bin = str (resto) + resultado_bin
while NC > 0:
    restoOct = int(NC % 8)
    NC = NC // 8
    resultado_oct = str(restoOct) + resultado_oct
while NH > 0:
    restoH = int (NH % 16)
    NH = NH // 16
    if restoH == 10:
        resultado_hexa = 'A' + resultado_hexa
    elif restoH == 11:
        resultado_hexa = 'B' + resultado_hexa
    elif restoH == 12:
        resultado_hexa = 'C' + resultado_hexa
    elif restoH == 13:
        resultado_hexa = 'D' + resultado_hexa
    elif restoH == 14:
        resultado_hexa = 'E' + resultado_hexa
    elif restoH == 15:
        resultado_hexa = 'F' + resultado_hexa
    else:
        resultado_hexa = str(restoH) + resultado_hexa

print(f'O número {N} em binário é: {resultado_bin}')
print(f'O número {N} em octal é: {resultado_oct}')
print(f'O número {N} em hexadecimal é: {resultado_hexa}')
print('-=-' * 20)
#esse foi dificil