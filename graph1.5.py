import pygame, sys, random, os
from numpy import array

# === inputs ================================================================================================================================================================================
M=[
[0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,1,0,1,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0]
]

ObjectsInput=["entrance","stuff","stuff","key","key","key","stuff","locked","stuff"]

alea=True

# === constants =============================================================================================================================================================================

WHITE = (255,255,255)
YELLOW = (255,255,0)
GREY = (200,200,200)
BLUE = (100,100,255)
RED = (255,0,0)
fontcolor=WHITE
size = width,height = 900,600
screen = pygame.display.set_mode(size)

l=90
RIGHT=array([l,0])
DOWN=array([0,l])
LEFT=array([-l,0])
UP=array([0,-l])
LV=[RIGHT,DOWN,LEFT,UP]

NULL=array([0,0])

IPOSX=height//2
IPOSY=width//2
IVECT=RIGHT

# === classes ===============================================================================================================================================================================

class Rectangle:
    """ |----> x
        |  []
      y v       []
    """
    def __init__(self,pos,dx,dy,color,vect):
        self.pos=pos
        self.x=pos[0]
        self.y=pos[1]
        self.dx=dx
        self.dy=dy
        self.color=color
        self.vect=vect
    def getCornerx(self):
        return self.x+-self.dx*0.5
    def getCornery(self):
        return self.y+-self.dy*0.5
    def draw(self):
        rect = pygame.Rect(self.getCornerx(),self.getCornery(),self.dx,self.dy)
        pygame.draw.rect(screen,self.color,rect)
    # def getconnectedObjects(self,i,M,Ao):
        # r=customindex(LV,self.vect)
        # O=[]
        # n=M[i][i:].count(1)
        # if n>=2:
            # O+=[LD[(3+r)%len(LD)],LD[(1+r)%len(LD)]]
        # if n in [1,3]:
            # O+=[LD[r%len(LD)]]
        # return O
    def __str__(self):
        return "|"+str(self.pos)+"|"
    def update(self):
        self.x=self.pos[0]
        self.y=self.pos[1]
        
class Entrance(Rectangle):
    def __init__(self):
        Rectangle.__init__(self,NULL,70,70,YELLOW,NULL)
class Stuff(Rectangle):
    def __init__(self):
        Rectangle.__init__(self,NULL,60,30,GREY,NULL)
class Locked(Rectangle):
    def __init__(self):
        Rectangle.__init__(self,NULL,100,100,BLUE,NULL)
class Key(Rectangle):
    def __init__(self):
        Rectangle.__init__(self,NULL,50,50,RED,NULL)

# === functions =============================================================================================================================================================================

def customindex(arraysList,array):
    for i in range(len(arraysList)):
        if (arraysList[i]==array).all():
            return i
    return None

def getFollowingVectors(M,i,vect):
    # print(i)
    n=M[i][i:].count(1)
    if n==0: return []
    V=[]
    r=customindex(LV,vect)
    if n>=2:
        V+=[LV[(3+r)%len(LV)],LV[(1+r)%len(LV)]]
    if n in [1,3]:
        V+=[LV[r%len(LV)]]
    return V

def setPositions(Objects,M,so):
    V=getFollowingVectors(M,so,Objects[so].vect)
    import copy
    L=copy.deepcopy(M[so][so:])
    for v in V:
        j=L.index(1)
        L.pop(j)
        L=[0]+L
        Objects[so+j].pos=Objects[so].pos+v
        Objects[so+j].vect=v
        setPositions(Objects,M,so+j)

def buildObjects(ObjectsInput):
    Objects=[]
    for o in ObjectsInput:
        ol=o.lower()
        if ol=="entrance":
            Objects+=[Entrance()]
        elif ol=="stuff":
            Objects+=[Stuff()]
        elif ol=="locked":
            Objects+=[Locked()]
        elif ol=="key":
            Objects+=[Key()]
        else:
            raise "invalid object format : use either \"entrance\",\"stuff\",\"key\",\"locked\" to complete the list"
    return Objects
            

# === various code =============================================================================================================================================================================

Objects=buildObjects(ObjectsInput)

if alea:
    # === Random M building ===

    Li=[] # list of indexes of ones (by column) :
    for i in range(len(Objects)-1):
        Li+=[random.randint(0,i)]
    M=[]  # creating a matrix of zeros :
    for i in range(len(Objects)):
        L=[]
        for j in range(len(Objects)):
            L+=[0]
        M+=[L]
          # filling the ones :
    for i in range(len(L)-1):
        M[Li[i]][i+1]=1

    # print(Li)
    # print("")
    # for l in M:
        # print(l)

    # ===

so=0
Objects[so].pos=array([IPOSX,IPOSY])
Objects[so].vect=IVECT

setPositions(Objects,M,so)

for o in Objects:
    o.update()
    # print(o)

# === display loop ==========================================================================================================================================================================

while True:
    pygame.time.Clock().tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(fontcolor)
    
    for o in Objects:
        o.draw()
    
    pygame.display.flip()