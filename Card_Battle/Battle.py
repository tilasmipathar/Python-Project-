import random
import pygame
from PIL import Image
from pygame import mixer

pygame.init()

infoObject = pygame.display.Info()#finding screen resolution
width=infoObject.current_w
height=infoObject.current_w/2

class Card:
	def __init__(self,card_type,card_def,card_attack,card_image,cardX=0,cardY=height):
		self.card_type=card_type
		self.card_def=card_def
		self.card_attack=card_attack
		self.card_image=card_image
		self.cardX=cardX
		self.cardY=cardY

def Create_opponent():
	deck=[]
	card_type=int(3*random.random())
	deck.append(Card(card_type,int(90*random.random())+1,int(90*random.random())+1,pygame.image.load("Card_Images/"+str(card_type)+"_adjusted.png"),2*width/3-(pygame.image.load("Card_Images/"+str(card_type)+"_adjusted.png")).get_width(),height/3-(pygame.image.load("Card_Images/"+str(card_type)+"_adjusted.png")).get_width()/2))
	card_type=int(3*random.random())
	deck.append(Card(card_type,int(90*random.random())+1,int(90*random.random())+1,pygame.image.load("Card_Images/"+str(card_type)+"_adjusted.png"),2*width/3-(pygame.image.load("Card_Images/"+str(card_type)+"_adjusted.png")).get_width(),2*height/3-(pygame.image.load("Card_Images/"+str(card_type)+"_adjusted.png")).get_width()/2))
	return deck

def Run_Battle(card_deck,screen,kills):
		
	mixer.init()
	mixer.music.load("Card_Battle/Battle.wav")
	mixer.music.set_volume(1)
	mixer.music.play()
	
	pygame.display.set_caption("Card Battle")#Window name
	
	card_width,card_height=(int(224*width/1920),int(224*width/1920))
	
	heading=pygame.font.Font("Card_Images/"+"OldLondon.ttf",int(64*width/1920))
	body=pygame.font.Font("Card_Images/"+"Seagram.ttf",int(24*width/1920))
	heading_render=heading.render("CARD BATTLE",True,(0,0,0))
	
	clock=pygame.time.Clock()
	
	choice1=0
	choice2=0
	player_turn=True
	attack_start=True
	card_return=False
	start_ticks=0
	running=True
	disp_max=0
	win=False
	super_mult=1.25
	under_mult=0.75
	
	background=pygame.image.load("Card_Images/"+"back_adjusted.png")
	
	random.shuffle(card_deck)
	for i in range(min(2,len(card_deck))):
		card_deck[i].cardX=width/3-(card_deck[i].card_image).get_width()
		card_deck[i].cardY=(i+1)*height/3-(card_deck[i].card_image).get_width()/2
	for i in range(2,max(2,len(card_deck))):
		card_deck[i].cardX=0
		card_deck[i].cardY=height
	oppo_deck=Create_opponent()
	
	if(len(card_deck)>=2):
		while running:
			
			clock.tick(60)
		
			body_render=[]
			for i in range(0,2):
				lst=[]
				lst.append(body.render("TYPE: "+("FIRE" if card_deck[i].card_type==0 else ("WATER" if card_deck[i].card_type==1 else "GRASS")),True,(0,0,0)))
				lst.append(body.render("DEFENSE: "+str(card_deck[i].card_def),True,(0,0,0)))
				lst.append(body.render("ATTACK: "+str(card_deck[i].card_attack),True,(0,0,0)))
				body_render.append(lst)
			body_render_oppo=[]
			for i in range(0,2):
				lst=[]
				lst.append(body.render("TYPE: "+("FIRE" if oppo_deck[i].card_type==0 else ("WATER" if oppo_deck[i].card_type==1 else "GRASS")),True,(0,0,0)))
				lst.append(body.render("DEFENSE: "+str(oppo_deck[i].card_def),True,(0,0,0)))
				lst.append(body.render("ATTACK: "+str(oppo_deck[i].card_attack),True,(0,0,0)))
				body_render_oppo.append(lst)
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					running=False
				if player_turn and (choice1==0 or choice2==0) and event.type==pygame.KEYDOWN:
					if event.key==pygame.K_1:
						if(card_deck[0].card_def>0 and choice1==0):
							choice1=1
						elif(oppo_deck[0].card_def>0):
							choice2=1
					if event.key==pygame.K_2:
						if (card_deck[1].card_def>0 and choice1==0):
							choice1=2
						elif(oppo_deck[1].card_def>0):
							choice2=2
			
			damage=0
			if (not player_turn) and (choice1==0 or choice2==0):
				for i in range(len(oppo_deck)):
					for j in range(2):
						if(card_deck[j].card_def>0 and oppo_deck[i].card_def>0 and(oppo_deck[i].card_type==card_deck[j].card_type-2 or oppo_deck[i].card_type==card_deck[j].card_type+1)and(super_mult*oppo_deck[i].card_attack>damage)):
							choice1=i+1
							choice2=j+1
							damage=super_mult*oppo_deck[i].card_attack
						elif(card_deck[j].card_def>0 and oppo_deck[i].card_def>0 and(oppo_deck[i].card_type==card_deck[j].card_type)and(oppo_deck[i].card_attack>damage)):
							choice1=i+1
							choice2=j+1
							damage=oppo_deck[i].card_attack
						elif(card_deck[j].card_def>0 and oppo_deck[i].card_def>0 and under_mult*oppo_deck[i].card_attack>damage):
							choice1=i+1
							choice2=j+1
							damage=under_mult*oppo_deck[i].card_attack
			
			if((not choice1==0)and(not choice2==0)):
				if(player_turn):
					if(attack_start):
						card_deck[choice1-1].cardX+=16*width/1920
						if(card_deck[choice1-1].cardX+card_width*2+16*width/1920>=oppo_deck[choice1-1].cardX):
							attack_start=False
					else:
						if(disp_max==0):
							disp_max=card_deck[choice1-1].cardX-width/3+card_width
							mult=1
							
							#Attack
							if(card_deck[choice1-1].card_type==oppo_deck[choice2-1].card_type-2 or card_deck[choice1-1].card_type==oppo_deck[choice2-1].card_type+1):
								mult=super_mult
							elif(not(card_deck[choice1-1].card_type==oppo_deck[choice2-1].card_type)):
								mult=under_mult
							oppo_deck[choice2-1].card_def-=mult*card_deck[choice1-1].card_attack
							if(oppo_deck[choice2-1].card_def<0):
								oppo_deck[choice2-1].card_def=0
							
						card_deck[choice1-1].cardX-=8*width/1920
						if(card_return):
							oppo_deck[choice2-1].cardX-=4*width/1920
						else:
							oppo_deck[choice2-1].cardX+=4*width/1920
						if(card_deck[choice1-1].cardX-width/3+card_width<=disp_max/2 and oppo_deck[choice2-1].card_def>0):
							card_return=True
						if(card_deck[choice1-1].cardX<=width/3-card_width):
							attack_start=True
							player_turn=False
							card_return=False
							disp_max=0
							choice1=0
							choice2=0
				else:
					if(attack_start):
						oppo_deck[choice1-1].cardX-=16*width/1920
						if(oppo_deck[choice1-1].cardX-16*width/1920<=card_deck[choice1-1].cardX+card_width*2):
							attack_start=False
					else:
						if(disp_max==0):
							disp_max=2*width/3-oppo_deck[choice1-1].cardX-card_width
							mult=1
							
							#Attack
							if(oppo_deck[choice1-1].card_type==card_deck[choice2-1].card_type-2 or oppo_deck[choice1-1].card_type==card_deck[choice2-1].card_type+1):
								mult=super_mult
							elif(not(oppo_deck[choice1-1].card_type==card_deck[choice2-1].card_type)):
								mult=under_mult
							card_deck[choice2-1].card_def-=mult*oppo_deck[choice1-1].card_attack
							if(card_deck[choice2-1].card_def<0):
								card_deck[choice2-1].card_def=0
							
						oppo_deck[choice1-1].cardX+=8
						if(card_return):
							card_deck[choice2-1].cardX+=4*width/1920
						else:
							card_deck[choice2-1].cardX-=4*width/1920
						if(2*width/3-oppo_deck[choice1-1].cardX-card_width<=disp_max/2 and card_deck[choice2-1].card_def>0):
							card_return=True
						if(oppo_deck[choice1-1].cardX>=2*width/3-card_width):
							attack_start=True
							player_turn=True
							card_return=False
							disp_max=0
							choice1=0
							choice2=0
			   
			screen.blit(background,(0,0));
			screen.blit(heading_render,(width/2-heading_render.get_width()/2,10*width/1920))
			for i in range(0,min(2,len(card_deck))):
				screen.blit(card_deck[i].card_image,(card_deck[i].cardX,card_deck[i].cardY))
				screen.blit(pygame.image.load("Card_Images/"+"info_adjusted.png"),(card_deck[i].cardX+card_deck[i].card_image.get_width(),card_deck[i].cardY))
				height_displacement=0
				for j in body_render[i]:
					screen.blit(j,(card_deck[i].cardX+card_deck[i].card_image.get_width()+10*width/1920,card_deck[i].cardY+10*width/1920+height_displacement))
					height_displacement+=48*width/1920
			for i in range(0,2):
				screen.blit(oppo_deck[i].card_image,(oppo_deck[i].cardX,oppo_deck[i].cardY))
				screen.blit(pygame.image.load("Card_Images/"+"info_adjusted.png"),(oppo_deck[i].cardX+oppo_deck[i].card_image.get_width(),oppo_deck[i].cardY))
				height_displacement=0
				for j in body_render_oppo[i]:
					screen.blit(j,(oppo_deck[i].cardX+oppo_deck[i].card_image.get_width()+10*width/1920,oppo_deck[i].cardY+10*width/1920+height_displacement))
					height_displacement+=48*width/1920
			screen.blit(pygame.image.load("Card_Images/info_adjusted.png"),(0,0))
			
			screen.blit(body.render("Kills: "+str(kills),True,(0,0,0)),(10*width/1920,10*width/1920))
			screen.blit(heading.render("Your Deck",True,(0,0,0)),(width/3-card_deck[0].card_image.get_width(),card_deck[0].cardY-60*width/1920))
			screen.blit(heading.render("Enemy Deck",True,(0,0,0)),(2*width/3-card_deck[0].card_image.get_width(),card_deck[0].cardY-60*width/1920))
			for i in range(2):
				number=heading.render(str(i+1),True,(0,0,0))
				screen.blit(pygame.image.load("Card_Images/"+"info_adjusted_small.png"),(card_deck[i].cardX-56*width/1920,card_deck[i].cardY))
				screen.blit(number,(card_deck[i].cardX-number.get_width()-10*width/1920,card_deck[i].cardY-10*width/1920))
			for i in range(2):
				number=heading.render(str(i+1),True,(0,0,0))
				screen.blit(pygame.image.load("Card_Images/"+"info_adjusted_small.png"),(oppo_deck[i].cardX+2*oppo_deck[i].card_image.get_width(),oppo_deck[i].cardY))
				screen.blit(number,(oppo_deck[i].cardX+2*oppo_deck[i].card_image.get_width()+number.get_width(),oppo_deck[i].cardY-10*width/1920))
			
			Break=True
			for i in oppo_deck:
				if(i.card_def>0):
					Break=False
			if(Break and start_ticks==0):
				start_ticks=pygame.time.get_ticks()
			seconds=(pygame.time.get_ticks()-start_ticks)/1000
			if((not start_ticks==0) and seconds>0.8):
				running=False;
			
			Break=True
			for i in card_deck[0:2]:
				if(i.card_def>0):
					Break=False
			if(Break and start_ticks==0):
				start_ticks=pygame.time.get_ticks()
			seconds=(pygame.time.get_ticks()-start_ticks)/1000
			if((not start_ticks==0) and seconds>0.8):
				running=False;
			
			pygame.display.update()
		
		for i in card_deck[0:2]:
			if(i.card_def<=0):
				card_deck.remove(i)
			if(i.card_def>0):
				win=True
	else:
		while running:
			
			clock.tick(60)
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					running=False
			
			text=heading.render("YOU DON'T HAVE ENOUGH CARDS TO FIGHT",True,(0,0,0))
			
			screen.blit(background,(0,0));
			
			screen.blit(heading_render,(width/2-heading_render.get_width()/2,10*width/1920))
			screen.blit(text,(width/2-text.get_width()/2,height/2-text.get_height()/2))
			if(start_ticks==0):
				start_ticks=pygame.time.get_ticks()
			if((pygame.time.get_ticks()-start_ticks)/1000>2):
				break
			pygame.display.update()
	return (card_deck,win)
