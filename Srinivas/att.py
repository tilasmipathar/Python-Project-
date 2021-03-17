import sys,random,time,pygame

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

apple= pygame.image.load("apple.png")
use = pygame.transform.scale(apple,(25,25))

pygame.display.set_caption('CyberPunk 2077')

dispX = 960
dispY = 720

disp = pygame.display.set_mode((dispX,dispY))

font=pygame.font.SysFont('comicsans',40)

def text_format(message, textFont, textSize, textColor):
 newFont=pygame.font.SysFont(textFont, textSize)
 newText=newFont.render(message, 0, textColor)
 return newText

def menu():
 evnt="start"
 clock = pygame.time.Clock()
 while 1:
  for event in pygame.event.get():
   keys= pygame.key.get_pressed() 
   if event.type==pygame.KEYDOWN:
    if (keys[pygame.K_w] or keys[pygame.K_UP]):
     evnt="start"
    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]):
     evnt="exit"
    if event.key==pygame.K_RETURN:
     if evnt=="start":
      main()
     elif evnt=="exit":
      pygame.quit()
      quit()
          
  disp.fill((0,255,0))
  title=text_format("CyberPunk 2077 By Srinivas",'comicsans',90,(0,0,0))
  if evnt=="start":
   text_start=text_format("START",'comicsans',75,(255,255,255))
  else:
   text_start = text_format("START",'comicsans',75,(0,0,0))
  if evnt=="exit":
   text_quit=text_format("QUIT",'comicsans',75,(255,255,255))
  else:
   text_quit = text_format("QUIT",'comicsans',75,(0,0,0))
 
  title_rect=title.get_rect()
  start_rect=text_start.get_rect()
  quit_rect=text_quit.get_rect()
 
  disp.blit(title, (dispX//2 - (title_rect[2]//2), 80))
  disp.blit(text_start, (dispX//2 - (start_rect[2]//2), 300))
  disp.blit(text_quit, (dispX//2 - (quit_rect[2]//2), 360))
  pygame.display.update()
  clock.tick(60)

def main():
 CLOCK = pygame.time.Clock()
 points=0
 move = 'right'
 apple = True
 apploc = [0,0]
 snake=[[480,360],[470,360]]
 snkhd=[480,360]

 while 1:
  disp.fill((0,255,0))
  
  score_font = font.render("Your Points: "+str(points),True,(0,0,0))
  font_pos = score_font.get_rect(center=(105,30))
  disp.blit(score_font,font_pos)
  
  for el in snake:
   pygame.draw.rect(disp,(0,0,0),(el[0],el[1],10,10))
   
  for event in pygame.event.get(): 
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()
   keys= pygame.key.get_pressed()
   if (keys[pygame.K_UP] or keys[pygame.K_w]) and move != 'down':
    move='up'
   if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and move != 'up':
    move='down'
   if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and move != 'right':
    move='left'
   if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and move != 'left':
    move='right'
  
  if move=='right':
   snkhd[0]+= 10
  elif move=='left':
   snkhd[0]-= 10
  elif move=='up':
   snkhd[1]-= 10
  elif move=='down':
   snkhd[1]+= 10

  snake.append(list(snkhd))

  if apple == True: 
   apploc = [random.randrange(50,dispX-50),random.randrange(50,dispY-50)]
   apple = False

  disp.blit(use,(apploc[0],apploc[1]))

  if pygame.Rect(snkhd[0],snkhd[1],10,10).colliderect(pygame.Rect(apploc[0],apploc[1],20,20)):
   apple=True
   points += 2
  else:
   snake.pop(0)

  for el in snake[:-1]:
   if(snkhd[0]<=0)or(snkhd[0]>=dispX)or(snkhd[1]<=0)or(snkhd[1]>=dispY)or pygame.Rect(el[0],el[1],10,10).colliderect(pygame.Rect(snkhd[0],snkhd[1],10,10)):
    gg(points)

  pygame.display.update()
  CLOCK.tick(45)    # this number can be altered to change the speed of the snake

def gg(points):
  disp.fill((0,255,0))
  ggwp = font.render("Game Over" ,True,(0,0,0))
  scorr = font.render("Your Points are " + str(points),True,(0,0,0))
  message = ggwp.get_rect(center=(dispX//2,dispY//2))
  point = scorr.get_rect(center=(dispX//2,dispY//2+40))
  disp.blit(ggwp,message)
  disp.blit(scorr,point)
  pygame.display.update()
  time.sleep(2)
  menu()

menu()
