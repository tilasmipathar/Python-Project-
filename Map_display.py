import Map
import pygame
from PIL import Image

pygame.init()

infoObject = pygame.display.Info()

size_of_map=15
Map.Map_Gen(size_of_map)
x=0
y=0
length_of_tile=infoObject.current_w//(size_of_map*2)
length_of_border=length_of_tile//8
playerX=0
playerY=0
for i in range(len(Map.Map)):
	for j in range(len(Map.Map[0])):
		if(Map.Map[i][j]==2):
			playerY=length_of_tile*i+length_of_tile/2
			playerX=length_of_tile*j+length_of_tile/2
			break
	if(not playerX==0 or not playerY):
		break
print(playerX,playerY)

screen=pygame.display.set_mode((size_of_map*2*length_of_tile,size_of_map*length_of_tile))

((Image.open("map_Grass.png")).resize((length_of_tile,length_of_tile))).save("map_Grass_adjusted.png")
((Image.open("map_asphalt.jpg")).resize((length_of_tile,length_of_tile))).save("map_asphalt_adjusted.jpg")
((Image.open("carousel.png")).resize((length_of_tile,length_of_tile))).save("carousel_adjusted.png")
((Image.open("map_mud.jpg")).resize((length_of_border,length_of_border))).save("map_mud_adjusted.jpg")
((Image.open("player.png")).resize((length_of_tile,length_of_tile))).save("player_adjusted.png")
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
	if pressed_keys[pygame.K_UP] and (not Map.Map[int((playerY-length_of_tile/16)//length_of_tile)][int(playerX//length_of_tile)]==0):
		playerY-=length_of_tile/16;
	if pressed_keys[pygame.K_DOWN] and (not Map.Map[int((playerY+length_of_tile/16)//length_of_tile)][int(playerX//length_of_tile)]==0):
		playerY+=length_of_tile/16;
	if pressed_keys[pygame.K_LEFT] and (not Map.Map[int(playerY//length_of_tile)][int((playerX-length_of_tile/16)//length_of_tile)]==0):
		playerX-=length_of_tile/16;
	if pressed_keys[pygame.K_RIGHT] and (not Map.Map[int(playerY//length_of_tile)][int((playerX+length_of_tile/16)//length_of_tile)]==0):
		playerX+=length_of_tile/16;
	
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
	
	pygame.display.update()
