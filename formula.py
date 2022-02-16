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

def clockwise(x, y, radi, radj, f):
     checkSpace(leftSpace, rightSpace, x)
     tmpArr.append("G02X"+str(round(x,2))+"Y"+str(round(y,2))+"I"+str(round(radi,2))+"J"+str(round(radj,2))+"F"+str(round(f,2)))

def anticlockwise(x, y, radi, radj, f):
    checkSpace(leftSpace, rightSpace, x)
    tmpArr.append("G03X"+str(round(x,2))+"Y"+str(round(y,2))+"I"+str(round(radi,2))+"J"+str(round(radj,2))+"F"+str(round(f,2)))

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

def drawA(x, y, f, z): #UPDATED FORMULA AND TEST RUN 
    setpoint(x, y, f)
    down(z, f)
    x+=7.6
    y+=20
    linear(x, y, f)
    x+=7.6
    y-=20
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=6.6
    y+=17
    linear(x, y, f)
    x-=6.6
    y-=17
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    x+=2.9
    y+=5.7
    setpoint(x, y, f)
    down(z, f)
    x+=9.5
    linear(x, y, f)
    up(z, f)
    x-=10.4
    y-=0.9
    setpoint(x, y, f)
    down(z, f)
    x+=11.3
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawB(x, y, f, z): #UPDATED FORMULA AND TEST RUN 
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    up(z, f)
    x+=1
    y-=1
    up(z, f)
    setpoint(x, y, f)
    down(z, f)
    y-=18
    linear(x, y, f)
    x+=1.5
    linear(x, y, f)
    r=4.25
    y+=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    x-=1.5
    linear(x, y, f)
    x+=1.5
    linear(x, y, f)
    r=5.25
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=5.25
    x-=r
    y+=5.25
    anticlockwiseWthRad(x, y, r, f)
    x-=2.5
    linear(x, y, f)
    up(z, f)
    x+=1
    y-=1
    setpoint(x, y, f)
    down(z, f)   
    x+=1.5
    linear(x, y, f)
    r=4.25
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=1.5
    linear(x, y, f)
    x+=1.5
    linear(x, y, f)
    r=5.25
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=5.25
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.5
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawC(x, y, f, z): #UPDATED FORMULA AND TEST RUN
    y+=5.25
    setpoint(x, y, f)
    down(z, f)
    r=5.25
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2.35
    linear(x, y, f)
    r=5.25
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    r=4.25
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.35
    linear(x, y, f)
    r=4.25
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=9.6
    linear(x, y, f)
    r=4.25
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    r=4.25
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)
    r=5.25
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    r=5.25
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=9.55
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawD(x, y, f, z): #TEST RUN DONE
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    r=10
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=10
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
    y+=18
    linear(x, y, f)
    r=9
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawE(x, y, f, z): #TEST RUN DONE
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=10
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=9
    linear(x, y, f)
    y-=9
    linear(x, y, f)
    x+=9
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=9
    linear(x, y, f)
    y-=8
    linear(x, y, f)
    x+=9
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=10
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawF(x, y, f, z): #TEST RUN DONE
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=10
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=9
    linear(x, y, f)
    y-=9
    linear(x, y, f)
    x+=9
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=9
    linear(x, y, f)
    y-=9
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawG(x, y, f, z): #TEST RUN DONE
    y+=5.25
    setpoint(x, y, f)#
    down(z, f)#
    r = 5.25
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r = 5.25
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=2
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=3
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y+=4
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    r=4.25
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=4.25
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=9.6
    linear(x, y, f)
    r=4.25
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    r=4.25
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)
    r=5.25
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=5.25
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=9.6
    linear(x, y, f)   
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawH(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=9.5
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    y+=9.5
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=20
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y+=9.5
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=9.5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace) #J
    rightSpaceArr.append(rightSpace)

def drawI(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    x+=5
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=1.5
    linear(x, y, f)
    y+=18
    linear(x, y, f)
    x+=1.5
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=1.5
    linear(x, y, f)
    y-=18
    linear(x, y, f)
    x-=1.5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawJ(x, y, f, z):
    y+=3.25
    setpoint(x, y, f)
    down(z, f)
    r=3.25
    x+=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    y+=15.75
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    y-=15.75
    linear(x, y, f)
    r=2.25
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawK(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=9.5
    linear(x, y, f)
    x+=4.5
    y+=9.5
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x-=4.5
    y-=9.5
    linear(x, y, f)
    x+=4.5
    y-=10.5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=4.5
    y+=9.5
    linear(x, y, f)
    y-=9.5
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawL(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=19
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
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    x+=2.5
    y-=14
    linear(x, y, f)
    x+=2
    y+=14
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    y-=20
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    y+=19
    linear(x, y, f)#
    x-=2
    y-=17
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=3.5
    y+=17
    linear(x, y, f)
    y-=19
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawN(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    x+=7
    y-=18
    linear(x, y, f)
    y+=18
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y-=20
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    x-=6
    y+=16
    linear(x, y, f)
    y-=16
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawO(x, y, f, z):
    y+=10
    setpoint(x, y, f)
    down(z, f)
    r=10
    x+=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    r=10
    x-=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=3
    setpoint(x, y, f)
    down(z, f)
    r=7
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    r=7
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawP(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=2
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
    y-=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    x+=2
    y+=19
    setpoint(x, y, f)
    down(z, f)
    r=4
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    y+=8
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawQ(x, y, f, z):
    y+=10
    setpoint(x, y, f)
    down(z, f)
    r=10
    x+=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    r=10
    x-=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=2
    setpoint(x, y, f)
    down(z, f)
    r=8
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    r=8
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=12
    y-=5
    setpoint(x, y, f)
    down(z, f)
    x+=2
    linear(x, y, f)
    x+=3
    y-=5
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    x-=3
    y+=5
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawR(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    y+=20
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    r=5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=5
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=5
    y-=10
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    x-=5
    y+=10
    linear(x, y, f)
    y-=10
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=19
    setpoint(x, y, f)
    down(z, f)
    r=4
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    y+=8
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    up(z, f)
    x-=1
    y-=19
    setpoint(x, y, f)
    down(z, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawS(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    x+=5
    linear(x, y, f)
    r=5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=4
    y+=(r*2)
    clockwiseWthRad(x, y, r, f)
    x+=5
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    r=5
    y-=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    r=4
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawT(x, y, f, z):
    y+=18
    setpoint(x, y, f)
    down(z, f)
    y+=2
    linear(x, y, f)
    x+=11
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=18
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    y+=18
    linear(x, y, f)
    x-=4
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawU(x, y, f, z):
    y+=20
    setpoint(x, y, f)
    down(z, f)
    y-=10
    linear(x, y, f)
    r=10
    x+=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    y+=10
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    y-=10
    linear(x, y, f)
    r=8
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    y+=10
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
       
def drawV(x, y, f, z):
    y+=20
    setpoint(x, y, f)
    down(z, f)
    x+=2
    linear(x, y, f)
    x+=1
    y-=15
    linear(x, y, f)
    x+=1
    y+=15
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    x-=2
    y-=20
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    x-=2
    y+=20
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    

    
def drawW(x, y, f, z):
    y+=20
    setpoint(x, y, f)
    down(z, f)
    x+=2
    linear(x, y, f)
    x+=1
    y-=15
    linear(x, y, f)
    x+=1
    y+=15
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    x+=1
    y-=15
    linear(x, y, f)
    x+=1
    y+=15
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    x-=2
    y-=20
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    x-=1
    y+=15
    linear(x, y, f)
    x-=1
    y-=15
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    x-=2
    y+=20 
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawX(x, y, f, z):
    y+=20
    setpoint(x, y, f)
    down(z, f)
    x+=2.5
    linear(x, y, f)
    x+=2.5
    y-=9.5
    linear(x, y, f)
    x+=2.5
    y+=9.5
    linear(x, y, f)
    x+=2.5
    linear(x, y, f)
    x-=2.5
    y-=10.5
    linear(x, y, f)
    x+=2.5
    y-=9.5
    linear(x, y, f)
    x-=2.5
    linear(x, y, f)
    x-=2.5
    y+=9.5
    linear(x, y, f)
    x-=2.5
    y-=9.5
    linear(x, y, f)
    x-=2.5
    linear(x, y, f)
    x+=2.5
    y+=9.5
    linear(x, y, f)
    x-=2.5
    y+=10.5
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawY(x, y, f, z):
    y+=20
    setpoint(x, y, f)
    down(z, f)
    x+=2
    linear(x, y, f)
    x+=1
    y-=5
    linear(x, y, f)
    x+=1
    y+=5
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    x-=2
    y-=10
    linear(x, y, f)
    y-=10
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    y+=10
    linear(x, y, f)
    x-=2
    y+=10
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawZ(x, y, f, z):
    y+=20
    setpoint(x, y, f)
    down(z, f)
    x+=10
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    x-=8
    y-=16
    linear(x, y, f)
    x+=8
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    x-=10
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    x+=8
    y+=16
    linear(x, y, f)
    x-=8
    linear(x, y, f)
    y+=2 
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw1(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    x+=7
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    x-=2.5
    linear(x, y, f)
    y+=18
    linear(x, y, f)
    x-=2.5
    linear(x, y, f)
    x-=2.5
    y-=2
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=2.25
    linear(x, y, f)
    y-=15
    linear(x, y, f)
    x-=1.75
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw2(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    x+=10
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    x-=8
    linear(x, y, f)
    x+=8
    y+=11.5
    linear(x, y, f)
    y+=1.5
    linear(x, y, f)
    r=5
    x-=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)
    r=4
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    y-=1
    linear(x, y, f)
    x-=9
    y-=12
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 

def draw3(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    x+=2
    linear(x, y, f)
    r=5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    r=4
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=0.5
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    x+=0.5
    linear(x, y, f)
    r=4
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=2
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw4(x, y, f, z):
    y+=5
    setpoint(x, y, f)
    down(z, f)
    x+=5
    linear(x, y, f)
    y-=5
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    y+=5
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    y+=10
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    x-=5
    y-=10
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    up(z, f)
    x+=2
    y+=2
    setpoint(x, y, f)
    down(z, f)
    x+=3
    linear(x, y, f)
    y+=7
    linear(x, y, f)
    x-=3
    y-=7
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw5(x, y, f, z):
    y+=17
    setpoint(x, y, f)
    down(z, f)
    y-=8
    linear(x, y, f)
    x+=3
    linear(x, y, f)
    r=4
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=3
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=4
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    x+=3
    linear(x, y, f)
    r=5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=1
    linear(x, y, f)
    r=5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    y+=4
    linear(x, y, f)
    x+=6
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    x-=8
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw6(x, y, f, z):
    y+=2.5
    setpoint(x, y, f)
    down(z, f)
    r=2.5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=5
    linear(x, y, f)
    r=2.5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=5
    linear(x, y, f)
    r=2.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=5
    linear(x, y, f)
    up(z, f)
    x-=2.5
    y-=7.5
    setpoint(x, y, f)
    down(z, f)
    y+=15
    linear(x, y, f)
    r=2.5
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=5
    linear(x, y, f)
    r=2.5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=2
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    r=1.5
    x-=(r-1)
    y+=(r-0.5)
    anticlockwiseWthRad(x, y, r, f)
    x-=5
    linear(x, y, f)
    r=1.5
    x-=(r-1)
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=8
    linear(x, y, f)
    r=1.5
    x+=(r-1)
    y+=(r-0.5)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    y-=7.5
    setpoint(x, y, f)
    down(z, f)
    r=1.5
    x+=r
    y-=(r-0.5)
    anticlockwiseWthRad(x, y, r, f)
    x+=3
    linear(x, y, f)
    r=1.5
    x+=r
    y+=(r-0.5)
    anticlockwiseWthRad(x, y, r, f)
    y+=5
    linear(x, y, f)
    r=1.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=3
    linear(x, y, f)
    r=1.5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=5
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)     
    
def draw7(x, y, f, z):
    y+=20
    setpoint(x, y, f)
    down(z, f)
    x+=10
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    x-=5 
    y-=18
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    x+=5
    y+=18
    linear(x, y, f)
    x-=8
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)  
   
def draw8(x, y, f, z):
    y+=2.5
    setpoint(x, y, f)
    down(z, f)
    r=2.5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=5
    linear(x, y, f)
    r=2.5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=5
    linear(x, y, f)
    r=2.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=2.5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=5
    linear(x, y, f)
    r=2.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=5
    linear(x, y, f)
    r=2.5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=5
    linear(x, y, f)
    r=2.5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=2.5 
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=5
    linear(x, y, f)
    up(z, f)
    x+=2
    y+=1
    setpoint(x, y, f)
    down(z, f)
    r=1.5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=3
    linear(x, y, f)
    r=1.5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=3
    linear(x, y, f)
    r=1.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=3
    linear(x, y, f)
    r=1.5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=3
    linear(x, y, f)
    up(z,f)
    y+=10
    setpoint(x, y, f)
    down(z, f)
    r=1.5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=3
    linear(x, y, f)
    r=1.5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=3
    linear(x, y, f)
    r=1.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=3
    linear(x, y, f)
    r=1.5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=3
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)   
        
def draw9(x, y, f, z):
    y+=2.5
    setpoint(x, y, f)
    down(z, f)
    x+=2.5
    y-=2.5
    linear(x, y, f)
    x+=5
    linear(x, y, f)
    r=2.5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=15
    linear(x, y, f)
    r=2.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=5
    linear(x, y, f)
    r=2.5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=5
    linear(x, y, f)
    r=2.5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=5
    linear(x, y, f)
    y-=7.5
    linear(x, y, f)
    x-=7.5
    linear(x, y, f)
    up(z, f)
    x+=7.5
    y+=11
    setpoint(x, y, f)
    down(z, f)
    r=1.5
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=2.5
    linear(x, y, f)
    r=1.5
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=3
    linear(x, y, f)
    r=1.5
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=2.5
    linear(x, y, f)
    r=1.5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=3
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)   
    
def draw0(x, y, f, z):
    y+=2.5
    setpoint(x, y, f)
    down(z, f)
    r=2.5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=5
    linear(x, y, f)
    r=2.5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=15
    linear(x, y, f)
    r=2.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=5
    linear(x, y, f)
    r=2.5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=15
    linear(x, y, f)
    up(z, f)
    x+=2
    y+=1
    setpoint(x, y, f)
    down(z, f)
    r=1.5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=3
    linear(x, y, f)
    r=1.5
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=13
    linear(x, y, f)
    r=1.5
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=3
    linear(x, y, f)
    r=1.5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=13
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawHypen(x, y, f, z):
    space = globals()
    x+=2 
    y+=10
    setpoint(x, y, f)
    down(z, f)
    x+=5
    linear(x, y, f)
    y+=2
    linear(x, y, f)
    x-=5
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    up(z, f)
    space['rightSpace'] +=2 
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawBox(z, f):
    tmpArr.append("G00X17Y-3")
    down(z, f)
    tmpArr.append("G01X17Y23")
    tmpRightSpace = rightSpace+3
    tmpArr.append("G01X"+str(round(tmpRightSpace,2))+"Y23"+"F"+str(round(f,2)))
    tmpArr.append("G01X"+str(round(tmpRightSpace,2))+"Y-3"+"F"+str(round(f,2)))
    tmpArr.append("G01X17Y-3")
    up(z, f)
    
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

   


    

