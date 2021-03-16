import pygame
from pygame import mixer
class menu_obj:
    def __init__(self,img,x,y):
        self.img = img
        self.x = x
        self.y = y

def menu(highscore_list):
    pygame.init()
    pygame.display.set_caption("Space Adventure Menu")
    WIDTH = 1500
    HEIGHT = 1000
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    bg = menu_obj(pygame.transform.scale(pygame.image.load('space_adventure/bg.jpg'),(WIDTH,HEIGHT)),0,0)
    font = pygame.font.Font('freesansbold.ttf', 50)
    font_play = font.render('PLAY', True, (255,255,255))
    font_highscore = font.render('HIGHSCORES', True, (255,255,255))
    font_quit = font.render('QUIT', True, (255,255,255))
    running = True
    highscore_state = False #needs to updated after sucessful completion of 1 game

    #Background music
    mixer.music.load('space_adventure/menu_bg_sound.wav')
    mixer.music.play(-1)
    def highscore():    #display highscores from highscores list
        string = ""
        y=1
        h=50
        for x in highscore_list: 
            font_score = font.render(str(y)+") "+str(x), True, (255,255,255))
            screen.blit(font_score,(WIDTH/2+100,h))
            y+=1
            h+=70
    
    while running:
        screen.blit(bg.img,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        mouse = pygame.mouse.get_pos()
        mouse_clk_pos = (0,0)
        if(pygame.mouse.get_pressed()[0]):      #get mouse pos on mouseclick
            mouse_clk_pos = pygame.mouse.get_pos()
        
        #Handles buttons
        if WIDTH/10 <= mouse[0] <= WIDTH/10+400 and HEIGHT/10 <= mouse[1] <= HEIGHT/10+70:  
            pygame.draw.rect(screen,(20,20,240),[WIDTH/10,HEIGHT/10,400,70],10,10)
        elif WIDTH/10 <= mouse[0] <= WIDTH/10+400 and HEIGHT/10+120 <= mouse[1] <= HEIGHT/10+70+120:
            pygame.draw.rect(screen,(20,20,240),[WIDTH/10,HEIGHT/10+120,400,70],10,10)
        elif WIDTH/10 <= mouse[0] <= WIDTH/10+400 and HEIGHT/10+240 <= mouse[1] <= HEIGHT/10+70+240:
            pygame.draw.rect(screen,(20,20,240),[WIDTH/10,HEIGHT/10+240,400,70],10,10)
        else:  
            pygame.draw.rect(screen,(10,120,240),[WIDTH/10,HEIGHT/10,400,70])
            pygame.draw.rect(screen,(10,120,240),[WIDTH/10,HEIGHT/10+120,400,70])
            pygame.draw.rect(screen,(10,120,240),[WIDTH/10,HEIGHT/10+240,400,70])
        
        #Handle clicks
        if WIDTH/10 <= mouse_clk_pos[0] <= WIDTH/10+400 and HEIGHT/10+240 <= mouse_clk_pos[1] <= HEIGHT/10+70+240: #handleclick on quit button
            return False
        if WIDTH/10 <= mouse_clk_pos[0] <= WIDTH/10+400 and HEIGHT/10+120 <= mouse_clk_pos[1] <= HEIGHT/10+70+120:  #handleclick on highscore button
            highscore_state = True
        if(highscore_state):
            highscore()
        if WIDTH/10 <= mouse_clk_pos[0] <= WIDTH/10+400 and HEIGHT/10 <= mouse_clk_pos[1] <= HEIGHT/10+70:  #handleclick on play button
            return True
        screen.blit(font_play,(WIDTH/10+50,HEIGHT/10+10))
        screen.blit(font_highscore,(WIDTH/10+50,HEIGHT/10+130))
        screen.blit(font_quit,(WIDTH/10+50,HEIGHT/10+250))
        pygame.display.update()
        
if __name__=='__main__':
    menu([1000,2000])
    
