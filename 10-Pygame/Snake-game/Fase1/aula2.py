#Objetivo da aula: Loop e eventos
#Importá os comandos pygame
import pygame

try:
    #Iniciá o jogo
    pygame.init()
except :
    print("O modulo do pygame não foi iniciado com sucesso")

#Largura da janela e define a largura da janela
altura = 400 
largura = 400
#Cria uma janela
pygame.display.set_mode((altura,largura))
#Nome da Janela
pygame.display.set_caption ('Snake')

sair=True
while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self =False
    
    pygame.display.update()
pygame.quit()
