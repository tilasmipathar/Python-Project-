import random
import pygame
from PIL import Image

pygame.init()
	
infoObject = pygame.display.Info()#finding screen resolution
width=infoObject.current_w
height=infoObject.current_w/2

class Card:
	def __init__(self,card_type,card_def,card_attack,card_image,cardX=0,cardY=0):
		self.card_type=card_type
		self.card_def=card_def
		self.card_attack=card_attack
		self.card_image=card_image
		self.cardX=cardX
		self.cardY=cardY

def Run_Shop(screen,coin):
	pygame.display.set_caption("Card Emporium")#Window name
	
	card_width,card_height=(Image.open("Card_Images/0_adjusted.png")).size
	card_type=[]
	card_def=[]
	card_attack=[]
	card_image=[]
	cardX=[]
	cardY=[]
	for i in range(0,3):
		card_type.append(int(random.random()*3))
		card_def.append(int(random.random()*100)+1)
		card_attack.append(int(random.random()*100)+1)
		card_image.append(pygame.image.load("Card_Images/"+str(card_type[i])+"_adjusted.png"))
		cardX.append(width*(i+1)/4-card_width)
		cardY.append(height/2-card_height/2-(1-i)*128)
	
	heading=pygame.font.Font("Card_Images/OldLondon.ttf",int(64*width/1920))
	body=pygame.font.Font("Card_Images/Seagram.ttf",int(24*width/1920))
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
	
	background=pygame.image.load("Card_Images/back_adjusted.png")
	
	if(coin>0):
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
				cardY[choice-1]+=(5+((16*(cardY[choice-1]-height/2)/(height/2)) if cardY[choice-1]>=height/2 else 0))*width/1920;
			   
			screen.blit(background,(0,0));
			screen.blit(heading_render,(width/2-heading_render.get_width()/2,10*width/1920))
			for i in range(0,3):
				screen.blit(card_image[i],(cardX[i],cardY[i]))
				height_displacement=0
				screen.blit(pygame.image.load("Card_Images/info_adjusted.png"),(cardX[i]+card_image[i].get_width(),cardY[i]))
				for j in body_render[i]:
					screen.blit(j,(cardX[i]+card_image[i].get_width()+10*width/1920,cardY[i]+height_displacement+10*width/1920))
					height_displacement+=48*width/1920
			screen.blit(pygame.image.load("Card_Images/info_adjusted.png"),(0,0))
			screen.blit(body.render("Coins: "+str(coin),True,(0,0,0)),(10*width/1920,10*width/1920))	
			
			if(cardY[choice-1]<height+8 and cardY[choice-1]<height-8):
				start_ticks=pygame.time.get_ticks()
			seconds=(pygame.time.get_ticks()-start_ticks)/1000
			if((not start_ticks==0) and seconds>0.8):
				running=False;
			
			pygame.display.update()
	else:
		while running:
			
			clock.tick(60)
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					running=False
			
			screen.blit(background,(0,0));
			
			text=heading.render("YOU CAN'T AFFORD A NEW CARD",True,(0,0,0))
			screen.blit(pygame.image.load("Card_Images/info_adjusted.png"),(0,0))
			screen.blit(body.render("Coins: "+str(coin),True,(0,0,0)),(10*width/1920,10*width/1920))
			
			screen.blit(heading_render,(width/2-heading_render.get_width()/2,10*width/1920))
			screen.blit(text,(width/2-text.get_width()/2,height/2-text.get_height()/2))
			if(start_ticks==0):
				start_ticks=pygame.time.get_ticks()
			if((pygame.time.get_ticks()-start_ticks)/1000>2):
				break
			pygame.display.update()
	
	return Card(card_type[choice-1],card_def[choice-1],card_attack[choice-1],pygame.image.load("Card_Images/"+str(card_type[choice-1])+"_adjusted.png"))
if __name__=="__main__":
	Run_Shop()
