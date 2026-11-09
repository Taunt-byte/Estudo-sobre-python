#Objetivo da aula: Cores, variáveis e desenho
#Importá os comandos pygame
import pygame

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
pos_x=largura/2
pos_y=altura/2


fundo = pygame.display.set_mode((altura,largura))
pygame.display.set_caption ('Snake')

sair=True
while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self =False
    fundo.fill(branco)
    pygame.draw.rect(fundo,preto,{pos_x,pos_y,tamanho,tamanho})
    pygame.display.update()
pygame.quit()