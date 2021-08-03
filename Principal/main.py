
import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Football Pong")

#aplicação do placar final
win = pygame.image.load("assets/win.png")

#imagem do placar
score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")

#imagem do campo
field = pygame.image.load("assets/field.png")

#imagens jogadores1 e 2
player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/player2.png")
player2_y = 310

ball = pygame.image.load("assets/ball.png")
#variaveis para inicial bola
ball_x = 617
ball_y = 337
#variavies para direcao e movimento da bola
ball_dir = -20
ball_dir_y = 1


#função movimento do jogador1
def move_player():
    global player1_y

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y -= 0

    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0

#limitação dos jogadores
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

#função para jogador2
def move_player2():
    global player2_y
    player2_y = ball_y


#função movimento da bola
def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score2_img
    global score1_img

    ball_x += ball_dir
    ball_y += ball_dir_y

#verificaçâo para colisao da bola com jogador1
    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1

##verificaçâo para colisao da bola com jogador2
    if ball_x > 1110:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1

#Verificação e condiçoes para limite da boliha dentro de campo
    if ball_y > 685:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

#reeiniciar a bola
#jogador2
    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")
    #jogador1
    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/ " + str(score1) + ".png")



#funçao para plint dos desenhos
def draw():
    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(win, (300,330))

#inicio loop do jogo
loop = True
while loop:
    for events in pygame.event.get():
        #verificaçâo para manter a tela aberta
        if events.type == pygame.QUIT:
                loop = False
        #movimentos jogador1 teclas condições para precionar a tecla
        if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_w:
                    player1_moveup = True
                if events.key == pygame.K_s:
                    player1_movedown = True
        #movimentos jogador1 teclas condições para soltar tecla
        if events.type == pygame.KEYUP:
                if events.key == pygame.K_w:
                    player1_moveup = False
                if events.key == pygame.K_s:
                    player1_movedown = False
    
    #inicialização das funções
    draw()   
    pygame.display.update()

