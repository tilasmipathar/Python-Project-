import random
Map=[]
def reached(POI,coordinate):
	for i in POI:
		if i[0]==coordinate:
			return i[1]==1
def Closest(POI,y1,x1,allow_old):
	global Map
	c=1
	y2=[]
	x2=[]
	while(True):
		for i in range(c):
			y1-=1;
			if(y1>=0 and y1<len(Map) and x1>=0 and x1<len(Map[0]) and Map[y1][x1]==1 and ((not reached(POI,(y1,x1))) or allow_old)):
				y2.append(y1)
				x2.append(x1)
			if(len(y2)>=2):
				break
		if(len(y2)>=2):
			break
		for i in range(c):
			x1+=1;
			if(y1>=0 and y1<len(Map) and x1>=0 and x1<len(Map[0]) and Map[y1][x1]==1 and ((not reached(POI,(y1,x1))) or allow_old)):
				y2.append(y1)
				x2.append(x1)
			if(len(y2)>=2):
				break
		if(len(y2)>=2):
			break
		c+=1
		for i in range(c):
			y1+=1;
			if(y1>=0 and y1<len(Map) and x1>=0 and x1<len(Map[0]) and Map[y1][x1]==1 and ((not reached(POI,(y1,x1))) or allow_old)):
				y2.append(y1)
				x2.append(x1)
			if(len(y2)>=2):
				break
		if(len(y2)>=2):
			break
		for i in range(c):
			x1-=1;	
			if(y1>=0 and y1<len(Map) and x1>=0 and x1<len(Map[0]) and Map[y1][x1]==1 and ((not reached(POI,(y1,x1))) or allow_old)):
				y2.append(y1)
				x2.append(x1)
			if(len(y2)>=2):
				break
		if(len(y2)>=2):
			break
		c+=1
	return (y2,x2)
def Join(y1,x1,y2,x2):
	global Map
	while(not(y1==y2 or x1==x2)):
		if(random.random()>=0.5):
			if y1>y2:
				y1-=1
			else:
				y1+=1
		else:
			if x1>x2:
				x1-=1
			else:
				x1+=1
		if(Map[y1][x1]==0):
			Map[y1][x1]=2
	while(not y1==y2):
		if y1>y2:
			y1-=1
		else:
			y1+=1
		if(Map[y1][x1]==0):
			Map[y1][x1]=2
	while(not x1==x2):
		if x1>x2:
			x1-=1
		else:
			x1+=1
		if(Map[y1][x1]==0):
			Map[y1][x1]=2
def Map_Gen(l):
	POI=[]
	global Map
	while(len(POI)<5):
		POI=[]
		Map=[]
		for i in range(l):
			lst=[]
			for j in range(l*2):
				lst.append(1 if random.random()>=0.96 else 0)
				if(lst[-1]==1):
					POI.append([(i,j),0]);
			Map.append(lst)
	for i in range(len(POI)):
		POI[i][1]=1;
		y2,x2=Closest(POI,POI[i][0][0],POI[i][0][1],len(POI)-i<=2);
		if(__name__=="__main__"):
			print("[",x2[0],y2[0],"] [",x2[1],y2[1],"]")
			print("0",end="  ")
			for j in range(len(Map[0])+1):
				print(j,end=("  " if j<=9 else " "))
			print("\n")
			c=0
			for j in Map:
				print(c,end=("  " if c<=9 else " "))
				c+=1
				for k in j:
					if(k==0):
						print(" ",end="  ")
					else:
						print(k,end="  ")
				print("\n")
		for j in range(2):
			Join(POI[i][0][0],POI[i][0][1],y2[j],x2[j])
if(__name__=="__main__"):
	Map_Gen(int(input()))
