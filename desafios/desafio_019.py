import pygame #biblioteca para criação de jogos
pygame.init() #serve pra inicializar o pygame, sempre que for mexer com ele
pygame.mixer.music.load('d019.mp3') #seleciona que musica ira tocar
pygame.mixer.music.play()#diz pra tocar a musica
pygame.event.wait() #espera a musica terminar pra encerrar o programa

