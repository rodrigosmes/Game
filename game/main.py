import pygame
import random

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode ((x,y))
pygame.display.set_caption ('Meu jogo em python')

bg = pygame.image.load('imagens/fundo.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

alien = pygame.image.load('imagens/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alien, (70, 50))

playerImg = pygame.image.load('imagens/space.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50, 50))#conversao do tamanho da nave
playerImg = pygame.transform.rotate(playerImg,  0)

missil = pygame.image.load('imagens/missile.png').convert_alpha()
missil = pygame.transform.scale(missil, (20, 20))#conversao do tamanho da nave
missil = pygame.transform.rotate(missil,  -45)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

ajuste_centro_missil = 10

vel_x_missil = 0
pos_missil_x = pos_player_x + ajuste_centro_missil
pos_missil_y = pos_player_y + ajuste_centro_missil


pontos = 10

triggered = False

rodando = True

font = pygame.font.SysFont('fonts')

#criar imagem > objeto

player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
missil_rect  = missil.get_rect()


#funcoes 

def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawn_missil():
    triggered = False
    pos_missil_x = pos_player_x + ajuste_centro_missil
    pos_missil_y = pos_player_y + ajuste_centro_missil
    vel_x_missil = 0 
    return [pos_missil_x, pos_missil_y, triggered, vel_x_missil]

def colisions ():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos += 1
        return True
    else:
        return False
    
    
    
#loop rodando
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    screen.blit(bg, (0,0)) 
    
    #criar background continuo
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0)) 
    if rel_x < 1280:
        screen.blit(bg, (rel_x,0))
    
    #teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -=1    
        if not triggered:
            pos_missil_y -= 1
    
    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 1
        if not triggered:
            pos_missil_y += 1
    
    if tecla[pygame.K_SPACE]:
        triggered = True    
        vel_x_missil = 3  
    
    #respawn
    
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    if pos_missil_x >= 1300:
        pos_missil_x, pos_missil_y, triggered, vel_x_missil = respawn_missil()
        
    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    #posicao rect
    
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    alien_rect.y = pos_alien_y
    alien_rect.x = pos_alien_x
    
    missil_rect.y = pos_missil_y
    missil_rect.x = pos_missil_x
    
    
    #movimento   
    x-= 0.5
    
    pos_alien_x -= 1
    
    pos_missil_x += vel_x_missil
    
    
    pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), missil_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), alien_rect, 4)

    
    #criar imagens
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    print(pontos)
    
    pygame.display.update()

