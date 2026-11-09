## Fazendo os carros aparecer aleatoriamente
## Basicamente é isso

import pygame
pygame.init()

# Configurações dos carros

x= 400
y= 300
pos_x = 200
pos_y = 300


velocidade = 10
velocidade_ia= 20

## Imagens dos carros e do fundo

fundo = pygame.image.load('fundo.png')
carro = pygame.image.load('carro.png')
policia = pygame.image.load('policia.png')
ambulancia = pygame.image.load('ambulancia.png')
carro_preto = pygame.image.load('carro_preto.png')

janela = pygame.display.set_mode(800,600)
pygame.display.set_caption("Criando jogo com python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
         
    ## Movimentação do jogador

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade

    if comandos[pygame.K_DOWN]:
        y+= velocidade

    if comandos[pygame.K_RIGHT]:
        x+= velocidade

    if comandos[pygame.K_LEFT]:
        x-= velocidade
    
    ## IA movimentação
    if (pos_x <- -200):
        pos_y = 600

    pos_y -= velocidade_ia

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(policia,(pos_x,pos_y))
    janela.blit(ambulancia,(pos_x + 150,pos_y))
    janela.blit(carro_preto,(pos_x + 270,pos_y))
    pygame.display.update()*0