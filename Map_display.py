import Map
import pygame
from PIL import Image

pygame.init()

size_of_map=15
Map.Map_Gen(size_of_map)
x=0
y=0
length_of_tile=64
length_of_border=length_of_tile//8

screen=pygame.display.set_mode((size_of_map*2*length_of_tile,size_of_map*length_of_tile))

((Image.open("map_Grass.png")).resize((length_of_tile,length_of_tile))).save("map_Grass_adjusted.png")
((Image.open("map_asphalt.jpg")).resize((length_of_tile,length_of_tile))).save("map_asphalt_adjusted.jpg")
((Image.open("carousel.png")).resize((length_of_tile,length_of_tile))).save("carousel_adjusted.png")
((Image.open("map_mud.jpg")).resize((length_of_border,length_of_border))).save("map_mud_adjusted.jpg")
Grass=pygame.image.load("map_Grass_adjusted.png")
Asphalt=pygame.image.load("map_asphalt_adjusted.jpg")
POI=pygame.image.load("carousel_adjusted.png")
Border=pygame.image.load("map_mud_adjusted.jpg")

running=True

clock=pygame.time.Clock()

while running:
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
	
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
	
	pygame.display.update()
