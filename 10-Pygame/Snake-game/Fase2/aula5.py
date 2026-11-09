#Objetivo da aula: Mais eventos e movimentação
#Importá os comandos pygame
import pygame
from random import randint


branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

try:
    #Iniciá o jogo
    pygame.init()
except :
    print("O modulo do pygame não foi iniciado com sucesso")

#Configura a janela
altura = 400 
largura = 400
tamanho = 100
pos_x=randint(0,(largura-tamanho)/10)*10
pos_y=randint(0,(altura-tamanho)/10)*10
velocidade_x = 0
velocidade_y = 0

fundo = pygame.display.set_mode((altura,largura))
pygame.display.set_caption ('Snake')

sair=True
while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        #Checando qual tecla foi apertada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidade_x=-0.5
                velocidade_y=0
            if event.key == pygame.K_RIGHT:
                velocidade_x=0.5
                velocidade_y=0
            if event.key == pygame.K_UP:
                velocidade_x=0
                velocidade_y=-0.5
            if event.key == pygame.K_DOWN:
                velocidade_x=0
                velocidade_y=0.5    
    fundo.fill(branco)
    pygame.draw.rect(fundo,preto,[pos_x,pos_y,tamanho,tamanho])
    pos_x+=velocidade_x
    pos_y+=velocidade_y
    pygame.display.update()
pygame.quit()