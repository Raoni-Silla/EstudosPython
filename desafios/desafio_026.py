import random
import time
from time import sleep

nSec = random.randint(0,100)
n = int(input('tente adivinhar o numero entre 0 e 100: '))
while n != nSec:
    if n > nSec:
        print('-=-' * 20)
        print('#####PROCESSANDO#####')
        sleep(3) #sleep faz o computador dormir 3 segundos antes de responder
        print('errado')
        n = int (input('Digite um numero menor: '))
        print('-=-' * 20)
    else:
        print('-=-' * 20)
        print('#####PROCESSANDO#####')
        sleep(3)
        print('errado')
        n = int(input('Digite um numero maior'))
        print('-=-' * 20)
print('#####PROCESSANDO#####')
sleep(3)
print('-/-' * 20)
print('Parabéns você acertou que o numero secreto é {}'.format(nSec))
print('-/-' * 20)
