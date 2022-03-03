tmpArr=[]
global leftSpace
leftSpace = 30
global rightSpace
rightSpace = 0
leftSpaceArr = []
rightSpaceArr = []

def checkSpace(leftSpace, rightSpace, x):
    space = globals()
    if x <leftSpace:
        space['leftSpace'] = x
    elif x > rightSpace:
        space['rightSpace'] = x

def down(z, f):
    tmpArr.append("G01Z-"+str(round(z,2))+"F"+str(round(f,2)))

def up(z, f):
   tmpArr.append("G01Z"+str(round(z,2))+"F"+str(round(f,2)))

def linear(x, y, f):
    checkSpace(leftSpace, rightSpace, x)
    tmpArr.append("G01X"+str(round(x,2))+"Y"+str(round(y,2))+"F"+str(round(f,2)))

def clockwiseWthRad(x, y, r, f):
    checkSpace(leftSpace, rightSpace, x)
    tmpArr.append("G02X"+str(round(x,2))+"Y"+str(round(y,2))+"R"+str(round(r,2))+"F"+str(round(f,2)))

def anticlockwiseWthRad(x, y, r, f):
    checkSpace(leftSpace, rightSpace, x)
    tmpArr.append("G03X"+str(round(x,2))+"Y"+str(round(y,2))+"R"+str(round(r,2))+"F"+str(round(f,2)))

def setpoint(x, y, f):
    x = round(x,2)
    y = round(y,2)
    f = round(f,2)
    checkSpace(leftSpace, rightSpace, x)
    tmpArr.append("G00X"+str(x)+"Y"+str(y)+"F"+str(f))

def startpoint(z):
    tmpArr.append("G00Z"+str(round(z,2)))
    tmpArr.append("M03S300")

def drawA(x, y, f, z): #UPDATED FORMULA AND TEST RUN
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=3
    y+=10
    linear(x, y, f)
    x+=3
    y-=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=2
    y+=6.5
    linear(x, y, f)
    x-=2
    y-=6.5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    x+=1.5
    y+=2
    setpoint(x, y, f)
    down(z, f)
    x+=3
    linear(x, y, f)
    up(z, f)
    x-=0.5
    y+=1
    setpoint(x, y, f)
    down(z, f)
    x-=2.1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawB(x, y, f, z): #UPDATED FORMULA AND TEST RUN 
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=3.25
    linear(x, y, f)
    r=2.75
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=2.75
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.25
    linear(x, y, f)
    x+=2.25
    linear(x, y, f)
    r=1.75
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=1.75
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.25
    linear(x, y, f)
    y+=8
    linear(x, y, f)
    x+=2.25
    linear(x, y, f)
    r=1.75
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=1.75
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.25
    linear(x, y, f)
    x+=2.25
    linear(x, y, f)
    r=2.75
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=2.75
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=3.25
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawC(x, y, f, z): #UPDATED FORMULA AND TEST RUN
    startpoint(z)
    y+=2 
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=6
    linear(x, y, f)
    r=1
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=2
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=6
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawD(x, y, f, z): #TEST RUN DONE
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    r=5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=5
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=1
    setpoint(x, y, f)
    down(z, f)
    y+=8
    linear(x, y, f)
    r=4
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=4
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawE(x, y, f, z): #TEST RUN DONE
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=3.5
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=3.5
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=6
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawF(x, y, f, z): #TEST RUN DONE
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=3.5
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=4.5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawG(x, y, f, z): #TEST RUN DONE
    startpoint(z)
    y+=2 
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=2
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=6
    linear(x, y, f)
    r=1
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=2
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=6
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawH(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=4.5
    linear(x, y, f)
    x+=4
    linear(x, y, f)
    y+=4.5
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y+=4.5
    linear(x, y, f)
    x-=4
    linear(x, y, f)
    y-=4.5
    linear(x, y, f)
    x-=1
    linear(x, y, f)  
    up(z, f)
    leftSpaceArr.append(leftSpace) #J
    rightSpaceArr.append(rightSpace)

def drawI(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=6
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=2.5
    linear(x, y, f)
    y+=8
    linear(x, y, f)
    x+=2.5
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=2.5
    linear(x, y, f)
    y-=8
    linear(x, y, f)
    x-=2.5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawJ(x, y, f, z):
    startpoint(z)
    y+=2 
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=8
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y-=8
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawK(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=4
    linear(x, y, f)
    x+=4
    y+=4
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x-=5
    y-=5
    linear(x, y, f)
    x+=5
    y-=5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=4
    y+=4 
    linear(x, y, f)
    y-=4
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawL(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=9
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=6
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawM(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=3
    y-=4
    linear(x, y, f)
    x+=3
    y+=4
    linear(x, y, f)
    y-=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y+=7
    linear(x, y, f)
    x-=2
    y-=3
    linear(x, y, f)
    x-=2
    y+=3
    linear(x, y, f)
    y-=7
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawN(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=5
    y-=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y+=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y-=10
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    x-=4
    y+=8
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawO(x, y, f, z):
    startpoint(z)
    y+=5
    setpoint(x, y, f)
    down(z, f)
    r=5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=1
    setpoint(x, y, f)
    down(z, f)
    r=4
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=4
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=4
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=4
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f) 
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawP(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=3.5
    linear(x, y, f)
    r=2.5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=2.5
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.5
    linear(x, y, f)
    y-=5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=9
    setpoint(x, y, f)
    down(z, f)
    x+=2.5
    linear(x, y, f)
    r=1.5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=1.5
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.5
    linear(x, y, f)
    y+=3
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawQ(x, y, f, z):
    startpoint(z)
    y+=5 
    setpoint(x, y, f)
    down(z, f)
    r=5
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    r=5
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=1
    setpoint(x, y, f)
    down(z, f)
    r=4
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    r=4
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=6.5
    y-=2.5
    setpoint(x, y, f)
    down(z, f)
    x+=1
    linear(x, y, f)
    x+=1.5
    y-=2.5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=1.5
    y+=2.5
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawR(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=10
    linear(x, y, f)
    x+=3.5
    linear(x, y, f)
    r=2.5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=2.5
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.5
    linear(x, y, f)
    x+=4
    y-=5
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x-=4
    y+=5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y-=5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=9
    setpoint(x, y, f)
    down(z, f)
    x+=2.5
    linear(x, y, f)
    r=1.5
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=2.5
    linear(x, y, f)
    y+=3
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawS(x, y, f, z):
    startpoint(z)
    y+=2
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=5
    y+=6
    linear(x, y, f)
    r=1
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=2
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=5
    y-=6
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawT(x, y, f, z):
    startpoint(z)
    x+=2.5
    setpoint(x, y, f)
    down(z, f)
    x+=1
    linear(x, y, f)
    y+=9
    linear(x, y, f)
    x+=2.5
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=2.5
    linear(x, y, f)
    y-=9
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawU(x, y, f, z):
    startpoint(z)
    y+=10
    setpoint(x, y, f)
    down(z, f)
    y-=8
    linear(x, y, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=8
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y-=8
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=8
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
       
def drawV(x, y, f, z):
    startpoint(z)
    y+=10
    setpoint(x, y, f)
    down(z, f)
    x+=2
    y-=10
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    x+=2
    y+=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=2
    y-=9
    linear(x, y, f)
    x-=2
    y+=9
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    

    
def drawW(x, y, f, z):
    startpoint(z)
    y+=10
    setpoint(x, y, f)
    down(z, f)
    x+=1
    y-=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x+=1
    y+=4
    linear(x, y, f)
    x+=1
    y-=4
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x+=1
    y+=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=1
    y-=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y+=7
    x-=2
    linear(x, y, f)
    x-=2
    y-=7
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x-=1
    y+=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawX(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=5
    y+=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x-=5
    y-=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    y+=10
    setpoint(x, y, f)
    down(z, f)
    x+=5
    y-=10
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x-=5
    y+=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawY(x, y, f, z):
    startpoint(z)
    y+=10
    setpoint(x, y, f)
    down(z, f)
    x+=2.5
    y-=4
    linear(x, y, f)
    y-=6
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y+=6
    linear(x, y, f)
    x+=2.5
    y+=4
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=2
    y-=3
    linear(x, y, f)
    x-=2
    y+=3
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawZ(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=6
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    x+=5
    y+=9
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    x-=5
    y-=9
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw1(x, y, f, z):
    startpoint(z)
    y+=8
    setpoint(x, y, f)
    down(z, f)
    y+=0.5
    linear(x, y, f)
    x+=1.5
    y+=1.5
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y+=8
    linear(x, y, f)
    x-=1.5
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw2(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=6
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    x+=5
    y+=6
    linear(x, y, f)
    r=3
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=3
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)
    r=2
    x+=(2*r)
    clockwiseWthRad(x, y, r, f)
    x-=5
    y-=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 

def draw3(x, y, f, z):
    startpoint(z)
    y+=2
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=2
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    y+=3
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    x-=2
    y-=3
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=2
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw4(x, y, f, z):
    startpoint(z)
    y+=2.5
    setpoint(x, y, f)
    down(z, f)
    y+=1
    linear(x, y, f)
    x+=4
    y+=6.5
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=6.5
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y-=2.5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y+=2.5
    linear(x, y, f)
    x-=4
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=1
    setpoint(x, y, f)
    down(z, f)
    x+=3
    linear(x, y, f)
    y+=5
    linear(x, y, f)
    x-=3
    y-=5
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw5(x, y, f, z):
    startpoint(z)
    y+=2
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=3
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=3
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=6
    linear(x, y, f)
    y-=4
    linear(x, y, f)
    x+=4
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=3
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw6(x, y, f, z):
    startpoint(z)
    y+=2
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=2
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=1
    linear(x, y, f)
    r=1
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f) 
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=2
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=6
    linear(x, y, f)
    up(z, f)
    x+=1
    setpoint(x, y, f)
    down(z, f)
    r=1
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=2
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)     
    
def draw7(x, y, f, z):
    startpoint(z)
    y+=10
    setpoint(x, y, f)
    down(z, f)
    x+=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=5
    y-=9
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x+=5
    y+=9
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)  
   
def draw8(x, y, f, z):
    startpoint(z)
    y+=2
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=1
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=1
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=2
    x-=2
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=1
    linear(x, y, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=2
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    x+=1
    setpoint(x, y, f)
    down(z, f)
    r=1
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=1
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    y+=6
    setpoint(x, y, f)
    down(z, f)
    r=1
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=1
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)   
        
def draw9(x, y, f, z):
    startpoint(z)
    y+=2
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=6
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=2
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=2
    linear(x, y, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=1
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=6
    setpoint(x, y, f)
    down(z, f)
    r=1
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=2
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=2
    linear(x, y, f) 
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)   
    
def draw0(x, y, f, z):
    startpoint(z)
    y+=2
    setpoint(x, y, f)
    down(z, f)
    r=2
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=2
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=6
    linear(x, y, f)
    r=2
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=2
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=6
    linear(x, y, f)
    up(z, f)
    x+=1
    setpoint(x, y, f)
    down(z, f)
    r=1
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=1
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=6
    linear(x, y, f)
    r=1
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=1
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=6
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawHypen(x, y, f, z):
    space = globals()
    x+=2 
    y+=4
    setpoint(x, y, f)
    down(z, f)
    x+=6
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=6
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    space['rightSpace'] +=2 
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawBox(z, f):
    tmpArr.append("G00X17Y-3")
    down(z, f)
    tmpArr.append("G01X17Y13")
    tmpRightSpace = rightSpace+3
    tmpArr.append("G01X"+str(round(tmpRightSpace,2))+"Y13"+"F"+str(round(f,2)))
    tmpArr.append("G01X"+str(round(tmpRightSpace,2))+"Y-2"+"F"+str(round(f,2)))
    tmpArr.append("G01X17Y-3")
    up(z, f)

def drawSpace(x, y, f, z):
    x+=2
    setpoint(x, y, f)
    rightSpaceArr.append(rightSpace)
    
def finalDraw():
    with open("output.txt","w") as txt:
        for i in tmpArr:
            txt.write(i+"\n")
    
def convert(text, x, y, f, z):
    match text:
        case 'A':
            drawA(x, y, f, z)
        case 'B':
            drawB(x, y, f, z)
        case 'C':
            drawC(x, y, f, z)
        case 'D':
            drawD(x, y, f, z)
        case 'E':
            drawE(x, y, f, z)
        case 'F':
            drawF(x, y, f, z)
        case 'G':
            drawG(x, y, f, z)
        case 'H':
            drawH(x, y, f, z)
        case 'I':
            drawI(x, y, f, z)
        case 'J':
            drawJ(x, y, f, z)
        case 'K':
            drawK(x, y, f, z)
        case 'L':
            drawL(x, y, f, z)
        case 'M':
            drawM(x, y, f, z)
        case 'N':
            drawN(x, y, f, z)
        case 'O':
            drawO(x, y, f, z)
        case 'P':
            drawP(x, y, f, z)
        case 'Q':
            drawQ(x, y, f, z)
        case 'R':
            drawR(x, y, f, z)
        case 'S':
            drawS(x, y, f, z)
        case 'T':
            drawT(x, y, f, z)
        case 'U':
            drawU(x, y, f, z)
        case 'V':
            drawV(x, y, f, z)
        case 'W':
            drawW(x, y, f, z)
        case 'X':
            drawX(x, y, f, z)
        case 'Y':
            drawY(x, y, f, z)
        case 'Z':
            drawZ(x, y, f, z)
        case '1':
            draw1(x, y, f, z)
        case '2':
            draw2(x, y, f, z)
        case '3':
            draw3(x, y, f, z)
        case '4':
            draw4(x, y, f, z)
        case '5':
            draw5(x, y, f, z)
        case '6':
            draw6(x, y, f, z)
        case '7':
            draw7(x, y, f, z)
        case '8':
            draw8(x, y, f, z)
        case '9':
            draw9(x, y, f, z)
        case '0':
            draw0(x, y, f, z)
        case '-':
            drawHypen(x, y, f, z)

def passText(text, x, y, f, z, space):
    txt = list(text)
    for char in txt:
        if(x < rightSpace):
            x = rightSpace + int(space)
            convert(char, x, y, f, z)
        else:
            convert(char, x, y, f, z)

   


    

