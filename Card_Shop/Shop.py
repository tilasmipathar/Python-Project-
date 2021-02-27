import random
import pygame
from PIL import Image
def Run_Shop():
	pygame.init()
	
	infoObject = pygame.display.Info()#finding screen resolution
	width=infoObject.current_w*0.95
	hieght=0.95*infoObject.current_w/2
	screen=pygame.display.set_mode((int(width), int(hieght)))#Window resolution

	pygame.display.set_caption("Card Emporium")#Window name
	
	
	card_width,card_hieght=(Image.open("0.png")).size
	card_type=[]
	card_def=[]
	card_attack=[]
	card_image=[]
	cardX=[]
	cardY=[]
	for i in range(0,3):
		card_type.append(int(random.random()*3))
		card_def.append(int(random.random()*101))
		card_attack.append(int(random.random()*101))
		card_image.append(pygame.image.load(str(card_type[i])+".png"))
		cardX.append(width*(i+1)/4-card_width)
		cardY.append(hieght/2-card_hieght/2-(1-i)*128)
	
	heading=pygame.font.Font("OldLondon.ttf",64)
	body=pygame.font.Font("Seagram.ttf",24)
	heading_render=heading.render("CARD EMPORIUM",True,(0,0,0))
	body_render=[]
	for i in range(0,3):
		lst=[]
		lst.append(body.render("TYPE: "+("FIRE" if card_type[i]==0 else ("WATER" if card_type[i]==1 else "GRASS")),True,(0,0,0)))
		lst.append(body.render("DEFENSE: "+str(card_def[i]),True,(0,0,0)))
		lst.append(body.render("ATTACK: "+str(card_attack[i]),True,(0,0,0)))
		body_render.append(lst)
	
	clock=pygame.time.Clock()
	
	choice=0
	start_ticks=0;
	running=True
	
	((Image.open("back.png")).resize((int(width),int(hieght)))).save("back_adjusted.png")
	background=pygame.image.load("back_adjusted.png")
	
	while running:
		
		clock.tick(60)
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			if choice==0 and event.type==pygame.KEYDOWN:
				if event.key==pygame.K_1:
					choice=1
				if event.key==pygame.K_2:
					choice=2
				if event.key==pygame.K_3:
					choice=3
						
		if(choice!=0):
			cardY[choice-1]+=5+((16*(cardY[choice-1]-hieght/2)/(hieght/2)) if cardY[choice-1]>=hieght/2 else 0);
		   
		screen.blit(background,(0,0));
		screen.blit(heading_render,(width/2-heading_render.get_width()/2,10))
		for i in range(0,3):
			screen.blit(card_image[i],(cardX[i],cardY[i]))
			hieght_displacement=0
			screen.blit(pygame.image.load("info.png"),(cardX[i]+card_image[i].get_width(),cardY[i]))
			for j in body_render[i]:
				screen.blit(j,(cardX[i]+card_image[i].get_width()+10,cardY[i]+hieght_displacement+10))
				hieght_displacement+=48
						
		
		if(cardY[choice-1]<hieght+8 and cardY[choice-1]<hieght-8):
			start_ticks=pygame.time.get_ticks()
		seconds=(pygame.time.get_ticks()-start_ticks)/1000
		if((not start_ticks==0) and seconds>0.8):
			running=False;
		
		pygame.display.update()
	return (card_type[choice-1],card_def[choice-1],card_attack[choice-1])
if __name__=="__main__":
	Run_Shop()
