import pygame
import random
from pygame import mixer
SCORE_SPACE_ADVENTURE = 0
pygame.init()
def game_start():
    mixer.music.load('space_adventure/bgsound.wav')
    mixer.music.play(-1)
    start = True
    screen = pygame.display.set_mode((600,800))
    while start:
        gs_img =pygame.image.load('space_adventure/startgame.png')
        screen.blit(gs_img,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start=False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    return space_adventure()
                    start = False
                if event.key == pygame.K_q:
                    start = False
        pygame.display.update()
def space_adventure():

    global SCORE_SPACE_ADVENTURE
    SCORE_SPACE_ADVENTURE = 0
    screen = pygame.display.set_mode((600,800))
    WIDTH = 600
    HEIGHT = 800
    GAME_VEL = 0.3
    running = True
    class obj:
        def __init__(self,x,y,img,xc,yc):
            self.x = x
            self.y = y
            self.img = img
            self.xc = xc
            self.yc = yc
            

    #Icon and Title
    pygame.display.set_caption("Space Adventure")
    icon = pygame.image.load('space_adventure/icon.png')
    pygame.display.set_icon(icon)

    #Player
    player1 = obj(268,650,pygame.image.load('space_adventure/player.png'),0,0)

    #PowerUP
    power_up = obj(268,650,pygame.image.load('space_adventure/down.png'),0,0)

    #Asteroid
    asteroid_list = []
    asteroid_list.append(obj(268,16,pygame.image.load('space_adventure/asteroid.png'),0,0))
    asteroid_list.append(obj(60,16,pygame.image.load('space_adventure/asteroid.png'),0,0))
    asteroid_list.append( obj(WIDTH-60,16,pygame.image.load('space_adventure/asteroid.png'),0,0))
    asteroid_list.append(obj(164,16,pygame.image.load('space_adventure/asteroid.png'),0,0))

    #Background Image
    bg_img = pygame.image.load('space_adventure/background.png')

    #Print Score
    score_font = pygame.font.SysFont(None,48)



    def player(x,y):
        screen.blit(player1.img,(x,y))

    def player_movements():
        player_pos_list = [60,164,268,WIDTH-224,WIDTH-124]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.xc = -0.8
            if event.key == pygame.K_RIGHT:
                player1.xc = 0.8
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
            global SCORE_SPACE_ADVENTURE
            SCORE_SPACE_ADVENTURE+=1

    def powerUp():
        global SCORE_SPACE_ADVENTURE
        if(int(SCORE_SPACE_ADVENTURE%24)==0 and int(SCORE_SPACE_ADVENTURE)!=0):
            screen.blit(power_up.img,(asteroid_list[0].x,power_up.y))
            if(player1.x >= asteroid_list[0].x-64 and player1.x <= asteroid_list[0].x +64):
                SCORE_SPACE_ADVENTURE+=4
                mixer.Sound('space_adventure/powerup.wav').play()
                return True

    
    def collision(asteroid,player):
        if (asteroid.y >= 608 and asteroid.y <= 650) and (player1.x >= asteroid.x-60 and player1.x <= asteroid.x+60):
            return True
        return False
    
    #Game Loop
    while running:
        screen.blit(bg_img,(0,0))
        score_img = score_font.render('Score:'+str(SCORE_SPACE_ADVENTURE),True,(255,255,255))
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
                    running = False
                    GAME_VEL = 0
                    explosion_sound = mixer.Sound('space_adventure/explosion.wav')
                    explosion_sound.play()
                    pygame. mixer. music. stop()
                    pygame.time.delay(1500)
                    pygame.display.update()
        if(powerUp()):
            GAME_VEL = GAME_VEL/2           
        GAME_VEL+=SCORE_SPACE_ADVENTURE/1000000
        pygame.display.update()
    print(SCORE_SPACE_ADVENTURE)
    return SCORE_SPACE_ADVENTURE
if __name__=='__main__':
    game_start()
