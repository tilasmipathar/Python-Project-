import pygame
import random
from pygame import mixer
SCORE = 0
pygame.init()
def game_start():
        start = True
        while start:
            screen = pygame.display.set_mode((600,800))
            gs_img =pygame.image.load('startgame.png')
            screen.blit(gs_img,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        space_adventure()
                        start = False
                    if event.key == pygame.K_q:
                        start = False
            pygame.display.update()
def space_adventure():
    screen = pygame.display.set_mode((600,800))
    WIDTH = 600
    HEIGHT = 800
    GAME_VEL = 0.3
    class obj:
        def __init__(self,x,y,img,xc,yc):
            self.x = x
            self.y = y
            self.img = img
            self.xc = xc
            self.yc = yc
            

    #Icon and Title
    pygame.display.set_caption("Space Adventure")
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)

    #Player
    player1 = obj(268,650,pygame.image.load('player.png'),0,0)

    #Asteroid
    asteroid_list = []
    asteroid_list.append(obj(268,16,pygame.image.load('asteroid.png'),0,0))
    asteroid_list.append(obj(60,16,pygame.image.load('asteroid.png'),0,0))
    asteroid_list.append( obj(WIDTH-60,16,pygame.image.load('asteroid.png'),0,0))
    asteroid_list.append(obj(164,16,pygame.image.load('asteroid.png'),0,0))

    #Background Image
    bg_img = pygame.image.load('background.png')

    #Background Music
    mixer.music.load('bgsound.wav')
    mixer.music.play(-1)

    #Game Over Image
    go_img = pygame.image.load('gameover.png')
    #Print Score
    score_font = pygame.font.SysFont(None,48)



    def player(x,y):
        screen.blit(player1.img,(x,y))

    def player_movements():
        player_pos_list = [60,164,268,WIDTH-224,WIDTH-124]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.xc = -1
            if event.key == pygame.K_RIGHT:
                player1.xc = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1.xc = 0
        player1.x += player1.xc
        #Restricting player movement boundaries
        if player1.x<=0:
            player1.x=0
        elif player1.x>=WIDTH-64:
            player1.x=WIDTH-64

    def asteroid(asteroid,x,y):
        screen.blit(asteroid.img,(x,y))

    def asteroid_movements(asteroid,y_speed):
        ast_pos_list = [60,164,268,WIDTH-224,WIDTH-124]
        asteroid.yc = y_speed
        asteroid.y+=asteroid.yc
        if asteroid.y >= HEIGHT:
            asteroid.y = -64
            pos = random.randint(0,4)
            asteroid.x = ast_pos_list[pos]
            global SCORE
            SCORE+=1

    def collision(asteroid,player):
        if (asteroid.y >= 586 and asteroid.y <= 650) and (player1.x >= asteroid.x-64 and player1.x <= asteroid.x+64):
            return True
        return False
    
    def game_over():
        over = True
        explosion_sound = mixer.Sound('explosion.wav')
        explosion_sound.play()
        while over:
            global SCORE
            screen.fill((255,255,255))
            screen.blit(go_img,(0,0))
            score_font = pygame.font.SysFont(None,60)
            score_img = score_font.render('Score:'+str(SCORE),True,(255,255,255))
            screen.blit(score_img,(210,40))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        SCORE = 0
                        space_adventure()
                        over = False
                    if event.key == pygame.K_q:
                        over = False
            pygame.display.update()
    
    
    #Game Loop
    running = True
    while running:
        screen.blit(bg_img,(0,0))
        score_img = score_font.render('Score:'+str(SCORE),True,(255,255,255))
        screen.blit(score_img,(20,20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_movements()
        player(player1.x,player1.y)
        for asteroid_ele in asteroid_list:
            asteroid_movements(asteroid_ele,GAME_VEL)
            asteroid(asteroid_ele,asteroid_ele.x,asteroid_ele.y)
        for asteroid_ele in asteroid_list:
            if collision(asteroid_ele,player1):
                    GAME_VEL = 0
                    game_over()
                    running = False
        GAME_VEL+=SCORE/1000000
        pygame.display.update()
game_start()