import Map
import pygame
import random
import math
from pygame import mixer
from PIL import Image
from Card_Shop import Shop
from Card_Battle import Battle
from Car_Racing_Game import Car_Racing_Game
from space_adventure import space_adventure

pygame.init()
mixer.init()
mixer.music.load("Carnival_music.wav")
mixer.music.set_volume(1)
mixer.music.play()

pygame.display.set_caption("Virtual Carnival")

infoObject = pygame.display.Info()

#Initialization
size_of_map=15
no_of_games=4
Map.Map_Gen(size_of_map)
Mini_Game_Pos=[]
for i in Map.Map:
	l=[]
	for j in i:
		if(j==1):
			l.append(int(random.random()*no_of_games)+1)
		else:
			l.append(0)
	Mini_Game_Pos.append(l)
x=0
y=0
length_of_tile=infoObject.current_w//(size_of_map*2)
length_of_border=length_of_tile//8
playerX=0
playerY=0
displacement=length_of_tile/16*length_of_tile*size_of_map/960
UsedX=size_of_map*2
UsedY=size_of_map
for i in range(len(Map.Map)):
	for j in range(len(Map.Map[0])):
		if(Map.Map[i][j]==2):
			playerY=length_of_tile*i+length_of_tile/2
			playerX=length_of_tile*j+length_of_tile/2
			break
	if((not playerX==0) or (not playerY==0)):
		break
card_deck=[]
coin=3

screen=pygame.display.set_mode((size_of_map*2*length_of_tile,size_of_map*length_of_tile))

((Image.open("map_Grass.png")).resize((length_of_tile,length_of_tile))).save("map_Grass_adjusted.png")
((Image.open("map_asphalt.jpg")).resize((length_of_tile,length_of_tile))).save("map_asphalt_adjusted.jpg")
((Image.open("carousel.png")).resize((length_of_tile,length_of_tile))).save("carousel_adjusted.png")
((Image.open("map_mud.jpg")).resize((length_of_border,length_of_border))).save("map_mud_adjusted.jpg")
((Image.open("player.png")).resize((length_of_tile,length_of_tile))).save("player_adjusted.png")
((Image.open("Card_Images/0.png")).resize((int(224*length_of_tile*size_of_map/960),int(224*length_of_tile*size_of_map/960)))).save("Card_Images/0_adjusted.png")
((Image.open("Card_Images/1.png")).resize((int(224*length_of_tile*size_of_map/960),int(224*length_of_tile*size_of_map/960)))).save("Card_Images/1_adjusted.png")
((Image.open("Card_Images/2.png")).resize((int(224*length_of_tile*size_of_map/960),int(224*length_of_tile*size_of_map/960)))).save("Card_Images/2_adjusted.png")
((Image.open("Card_Images/back.png")).resize((length_of_tile*size_of_map*2,length_of_tile*size_of_map))).save("Card_Images/back_adjusted.png")
((Image.open("Card_Images/info.png")).resize((int(224*length_of_tile*size_of_map/960),int(224*length_of_tile*size_of_map/960)))).save("Card_Images/info_adjusted.png")
Grass=pygame.image.load("map_Grass_adjusted.png")
Asphalt=pygame.image.load("map_asphalt_adjusted.jpg")
POI=pygame.image.load("carousel_adjusted.png")
Border=pygame.image.load("map_mud_adjusted.jpg")
Player_icon=pygame.image.load("player_adjusted.png")

running=True

clock=pygame.time.Clock()

while running:
	clock.tick(60)
		
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
	pressed_keys=pygame.key.get_pressed()
	if pressed_keys[pygame.K_UP] and playerY-displacement*math.sqrt(2)>=0 and (not Map.Map[int((playerY-length_of_tile/16)//length_of_tile)][int(playerX//length_of_tile)]==0):
		if(not (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_RIGHT])):
			playerY-=displacement*math.sqrt(2)
		else:
			playerY-=displacement
	if pressed_keys[pygame.K_DOWN] and playerY+displacement*math.sqrt(2)<size_of_map*length_of_tile and (not Map.Map[int((playerY+length_of_tile/16)//length_of_tile)][int(playerX//length_of_tile)]==0):
		if(not (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_RIGHT])):
			playerY+=displacement*math.sqrt(2)
		else:
			playerY+=displacement
	if pressed_keys[pygame.K_LEFT] and playerX-displacement*math.sqrt(2)>=0 and (not Map.Map[int(playerY//length_of_tile)][int((playerX-length_of_tile/16)//length_of_tile)]==0):
		if(not (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_DOWN])):
			playerX-=displacement*math.sqrt(2)
		else:
			playerX-=displacement
	if pressed_keys[pygame.K_RIGHT] and playerX+displacement*math.sqrt(2)<size_of_map*length_of_tile*2 and (not Map.Map[int(playerY//length_of_tile)][int((playerX+length_of_tile/16)//length_of_tile)]==0):
		if(not (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_DOWN])):
			playerX+=displacement*math.sqrt(2)
		else:
			playerX+=displacement
	
	disp_x=0
	disp_y=0
	screen.blit(Grass,(disp_x,disp_y))
	
	for i in range(len(Map.Map)):
		for j in range(len(Map.Map[0])):
			if(Map.Map[i][j]==0):
				screen.blit(Grass,(disp_x,disp_y))
				
				if(i>0):
					if(j>0 and Map.Map[i-1][j-1]!=0):
						screen.blit(Border,(disp_x,disp_y))
					if(Map.Map[i-1][j]!=0):
						for k in range(length_of_tile//length_of_border):
							screen.blit(Border,(disp_x + k*length_of_border,disp_y))
					if(j<len(Map.Map[0])-1 and Map.Map[i-1][j+1]!=0):
						screen.blit(Border,(disp_x + length_of_tile - length_of_border,disp_y))
					
				if(j>0 and Map.Map[i][j-1]!=0):
					for k in range(length_of_tile//length_of_border):
						screen.blit(Border,(disp_x,disp_y + k*length_of_border))
				if(j<len(Map.Map[0])-1 and Map.Map[i][j+1]!=0):
					for k in range(length_of_tile//length_of_border):
						screen.blit(Border,(disp_x + length_of_tile - length_of_border,disp_y + k*length_of_border))
				
				if(i<len(Map.Map)-1):
					if(j>0 and Map.Map[i+1][j-1]!=0):
						screen.blit(Border,(disp_x,disp_y+ length_of_tile - length_of_border))
					if(Map.Map[i+1][j]!=0):
						for k in range(length_of_tile//length_of_border):
							screen.blit(Border,(disp_x + k*length_of_border,disp_y+ length_of_tile - length_of_border))
					if(j<len(Map.Map[0])-1 and Map.Map[i+1][j+1]!=0):
						screen.blit(Border,(disp_x + length_of_tile - length_of_border,disp_y+ length_of_tile - length_of_border))
				
			else:
				screen.blit(Asphalt,(disp_x,disp_y))
				if(Map.Map[i][j]!=2):
					screen.blit(POI,(disp_x,disp_y))
			disp_x+=length_of_tile
		disp_x=0
		disp_y+=length_of_tile
		
		screen.blit(Player_icon,(playerX-length_of_tile/2,playerY-length_of_tile/2))
	
	switch=Mini_Game_Pos[int(playerY//length_of_tile)][int(playerX//length_of_tile)]
	if(switch==0):
		UsedX=size_of_map*2
		UsedY=size_of_map
	elif(not(UsedX==int(playerX//length_of_tile) and UsedY==int(playerY//length_of_tile))):
		UsedX=int(playerX//length_of_tile)
		UsedY=int(playerY//length_of_tile)
		if(switch==1):
			card_deck.append(Shop.Run_Shop(screen,coin))
			if(coin>0):
				coin-=1
		elif(switch==2):
			l=Battle.Run_Battle(card_deck,screen)
			card_deck=l[0]
			if(l[1]):
				coin+=1
		elif(switch==3):
			car_racing=Car_Racing_Game.CarRacing()
			car_racing.racing_window()
		elif(switch==4):
			space_adventure.game_start()
		screen=pygame.display.set_mode((size_of_map*2*length_of_tile,size_of_map*length_of_tile))
		mixer.music.load("Carnival_music.wav")
		mixer.music.set_volume(1)
		mixer.music.play()
	
	pygame.display.set_caption("Virtual Carnival")
	
	pygame.display.update()
