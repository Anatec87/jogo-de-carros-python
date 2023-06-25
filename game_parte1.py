import pygame
from random import randint
pygame.init()
x = 35
y = 70
pos_x = 240
pos_y = 1200
pos_y_a = 2000
pos_y_c = 800

timer = 0
tempo_segundo = 0

velocidade = 10
velocidade_outros = 12

fundo = pygame.image.load('tela1.jpeg')
carro = pygame.image.load('carro vermelho.png')
policia = pygame.image.load('policia.png')
ambulancia = pygame.image.load('ambulancia.png')
taxi = pygame.image.load('taxi.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (80,50)

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um  jogo com Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()


    if comandos[pygame.K_RIGHT] and x<= 165:
       x += velocidade
    if comandos[pygame.K_LEFT] and x >= -85:
       x -= velocidade

        #detecta a colisão

    if ((x+80 > pos_x and y +423 > pos_y)):
        y = 1200
    if ((x-567 > pos_x -270 and y +423 > pos_y_a)): #colisão lado esquerdo
        y = 1200
    if ((x+567 > pos_x -225 and y +423 > pos_y_c)) and ((x+567 < pos_x -225 and y +423 > pos_y_c)):
        y = 1200

    if (pos_y <= -500) :
       pos_y = randint(1200, 1800)

    if ((pos_y_a <= -500)):
       pos_y_a = randint(2000, 2500)

    if ((pos_y_c <= -500)):
       pos_y_c = randint(800, 1300)

    if (timer <40):
        timer += 1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +3
    pos_y_c-= velocidade_outros +15

    janela.blit(fundo, (0,0))
    janela.blit(carro, (x,y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(ambulancia, (pos_x - 270, pos_y_a))
    janela.blit(taxi, (pos_x - 225, pos_y_c))
    janela.blit(texto,pos_texto)

    pygame.display.update()

pygame.quit()
