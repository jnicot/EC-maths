
a=3
b=-1
px=6
py=3
pz=0
qx=3
qy=0
qz=0
Fp=7

def surLaCourbe(x,y):
	Y=(y*y)%Fp
	X=(x*x*x+a*x+b)%Fp
	if Y==X:
		return True
	else:
		return False
def calculeInverse(y):
        i=1
        while i<Fp:
                if((y*i)%Fp==1):
                        return int(i)
                i=i+1
#Calcul de 2p
def doublepoint(x,y,z):
	if y==0:
		x=0
		y=0
		z=1
		return x,y,z
	elif z==1:
		return x,y,z
	else:
		yy=2*y
		yyy=calculeInverse(yy)
		delta=(3*x*x+a)*yyy
		X=((delta*delta)-2*x)%Fp
		Y=(delta*(x-X)-y)%Fp
		Z=0
		return X,Y,Z
def somme(px,py,pz,qx,qy,qz):
	if(px==qx):
		x=0
		y=0
		z=1
		print("p+q = point infini")
		return x,y,z
	elif(pz==1):
		return qx,qy,qz		
	elif(qz==1):
		return px,py,pz	
	else:
		tmp=(qx-px)%Fp
		z=0
		inv=calculeInverse(tmp) #inverse de x2-x1
		l=((qy-py)*inv)%Fp #on calcule lambda

		Rx=( l * l - px- qx)%Fp #on calcule la coordonnee X de l'intersection
		Ry=( l * Rx - l * px + py)%Fp #on calcule la coordonnee Y de l'intersection

		x=(l*l-px-qx)%Fp #on calcule le x de P+Q
		y=(l*px-l*Rx-px)%Fp #on calcule le y de P+q
		return x,y,z

#Calcul de -p
def inversepoint(x,y):
	x=x
	y=-y
	z=0
	return x,y,z
#Algo diapo 57
def np(x,y,z,n):
	Px=0
	Py=0
	Pz=1
	if(n==0):
		return Px,Py,Pz
	elif(n<0):
		N=-n
		X=x
		Y=-y
		Z=z
	else:
		N=n
		X=x
		Y=y
		Z=z
	Px,Py,Pz=etape2(Px,Py,Pz,X,Y,Z,N)
	return Px,Py,Pz	

def etape3(Px,Py,Pz,X,Y,Z,N):
	N=N/2
	if(N==0):
		return Px,Py,Pz
	else:
		X,Y,Z=doublepoint(X,Y,Z)
		Px,Py,Pz=etape2(Px,Py,Pz,X,Y,Z,N)	
	
		
def etape2(Px,Py,Pz,X,Y,Z,N):
	if(N%2!=0):
                Px,Py,Pz=somme(Px,Py,Pz,X,Y,Z)
		print(str(Px)+str(Py)+str(Pz))
		return Px,Py,Pz
	print("test")
	return Px,Py,Pz
	Px,Py,Pz=etape3(Px,Py,Pz,X,Y,Z,N)
	
#verif=surLaCourbe(px,py)
#print(verif)
#x,y,z=doublepoint(6,3,0)
#print(str(x)+str(y)+str(z))
#x,y,z=somme(6,3,0,0,0,1)
#print(str(x)+str(y)+str(z))
x,y,z=np(6,3,0,2)
print(str(x)+str(y)+str(z))
