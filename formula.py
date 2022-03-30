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

def startpoint(z, speed):
    tmpArr.append("G00Z"+str(round(z,2)))
    tmpArr.append("M03S"+str(round(speed, 2)))

def drawA(x, y, f, z, speed): #UPDATED FORMULA AND TEST RUN
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    x+=(3*constantFontSize)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(3*constantFontSize)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y+=(6.5*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y-=(6.5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1.5*constantFontSize)
    y+=(2*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(3*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x-=(0.5*constantFontSize)
    y+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x-=(2.1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawB(x, y, f, z, speed): #UPDATED FORMULA AND TEST RUN 
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(3.25*constantFontSize)
    linear(x, y, f)
    r=(2.75*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(2.75*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2.25*constantFontSize)
    linear(x, y, f)
    x+=(2.25*constantFontSize)
    linear(x, y, f)
    r=(1.75*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(1.75*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2.25*constantFontSize)
    linear(x, y, f)
    y+=(8*constantFontSize)
    linear(x, y, f)
    x+=(2.25*constantFontSize)
    linear(x, y, f)
    r=(1.75*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(1.75*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2.25*constantFontSize)
    linear(x, y, f)
    x+=(2.25*constantFontSize)
    linear(x, y, f)
    r=(2.75*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(2.75*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(3.25*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawC(x, y, f, z, speed): #UPDATED FORMULA AND TEST RUN
    startpoint(z, speed)
    y+=(2*constantFontSize) 
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(6*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(6*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawD(x, y, f, z, speed): #TEST RUN DONE
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    r=(5*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(5*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    y+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    y+=(8*constantFontSize)
    linear(x, y, f)
    r=(4*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(4*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawE(x, y, f, z, speed): #TEST RUN DONE
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    linear(x, y, f)
    y-=(3.5*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    linear(x, y, f)
    y-=(3.5*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x-=(6*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawF(x, y, f, z, speed): #TEST RUN DONE
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    linear(x, y, f)
    y-=(3.5*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    linear(x, y, f)
    y-=(4.5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawG(x, y, f, z, speed): #TEST RUN DONE
    startpoint(z, speed)
    y+=(2*constantFontSize) 
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(2*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(6*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(6*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawH(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(4.5*constantFontSize)
    linear(x, y, f)
    x+=(4*constantFontSize)
    linear(x, y, f)
    y+=(4.5*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y+=(4.5*constantFontSize)
    linear(x, y, f)
    x-=(4*constantFontSize)
    linear(x, y, f)
    y-=(4.5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)  
    up(z, f)
    leftSpaceArr.append(leftSpace) 
    rightSpaceArr.append(rightSpace)

def drawI(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    x+=(6*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(2.5*constantFontSize)
    linear(x, y, f)
    y+=(8*constantFontSize)
    linear(x, y, f)
    x+=(2.5*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x+=(2.5*constantFontSize)
    linear(x, y, f)
    y-=(8*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawJ(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2*constantFontSize) 
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(8*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y-=(8*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawK(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(4*constantFontSize)
    linear(x, y, f)
    x+=(4*constantFontSize)
    y+=(4*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    y-=(5*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    y-=(5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    x-=(4*constantFontSize)
    y+=(4*constantFontSize) 
    linear(x, y, f)
    y-=(4*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawL(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(9*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x-=(6*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawM(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(3*constantFontSize)
    y-=(4*constantFontSize)
    linear(x, y, f)
    x+=(3*constantFontSize)
    y+=(4*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y+=(7*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y-=(3*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y+=(3*constantFontSize)
    linear(x, y, f)
    y-=(7*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawN(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    y+=(2*constantFontSize)
    linear(x, y, f)
    x-=(4*constantFontSize)
    y+=(8*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawO(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(5*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(5*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=(5*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(5*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(5*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(4*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=(4*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(4*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(4*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f) 
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawP(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(3.5*constantFontSize)
    linear(x, y, f)
    r=(2.5*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(2.5*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2.5*constantFontSize)
    linear(x, y, f)
    y-=(5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    y+=(9*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(2.5*constantFontSize)
    linear(x, y, f)
    r=(1.5*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(1.5*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2.5*constantFontSize)
    linear(x, y, f)
    y+=(3*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawQ(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(5*constantFontSize) 
    setpoint(x, y, f)
    down(z, f)
    r=(5*constantFontSize)
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    r=(5*constantFontSize)
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(4*constantFontSize)
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    r=(4*constantFontSize)
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=(6.5*constantFontSize)
    y-=(2.5*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    x+=(1.5*constantFontSize)
    y-=(2.5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    x-=(1.5*constantFontSize)
    y+=(2.5*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawR(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(3.5*constantFontSize)
    linear(x, y, f)
    r=(2.5*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(2.5*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2.5*constantFontSize)
    linear(x, y, f)
    x+=(4*constantFontSize)
    y-=(5*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    x-=(4*constantFontSize)
    y+=(5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y-=(5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    y+=(9*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(2.5*constantFontSize)
    linear(x, y, f)
    r=(1.5*constantFontSize)
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=(2.5*constantFontSize)
    linear(x, y, f)
    y+=(3*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawS(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(5*constantFontSize)
    y+=(6*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(5*constantFontSize)
    y-=(6*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawT(x, y, f, z, speed):
    startpoint(z, speed)
    x+=(2.5*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y+=(9*constantFontSize)
    linear(x, y, f)
    x+=(2.5*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x+=(2.5*constantFontSize)
    linear(x, y, f)
    y-=(9*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawU(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    y-=(8*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(8*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y-=(8*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(8*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
       
def drawV(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(2*constantFontSize)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    x+=(2*constantFontSize)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y-=(9*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y+=(9*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawW(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(1*constantFontSize)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    y+=(4*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    y-=(4*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y+=(7*constantFontSize)
    x-=(2*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y-=(7*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawX(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    x+=(5*constantFontSize)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(5*constantFontSize)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawY(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(2.5*constantFontSize)
    y-=(4*constantFontSize)
    linear(x, y, f)
    y-=(6*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y+=(6*constantFontSize)
    linear(x, y, f)
    x+=(2.5*constantFontSize)
    y+=(4*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y-=(3*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y+=(3*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawZ(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    x+=(6*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    y+=(8*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    y-=(8*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw1(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(8*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    y+=(0.5*constantFontSize)
    linear(x, y, f)
    x+=(1.5*constantFontSize)
    y+=(1.5*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y+=(8*constantFontSize)
    linear(x, y, f)
    x-=(1.5*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw2(x, y, f, z, speed):
    startpoint(z, speed)
    setpoint(x, y, f)
    down(z, f)
    x+=(6*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    y+=(6*constantFontSize)
    linear(x, y, f)
    r=(3*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(3*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=(2*r)
    clockwiseWthRad(x, y, r, f)
    x-=(5*constantFontSize)
    y-=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 

def draw3(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    y+=(3*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    linear(x, y, f)
    x-=(2*constantFontSize)
    y-=(3*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw4(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2.5*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x+=(4*constantFontSize)
    y+=(6.5*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(6.5*constantFontSize)
    linear(x, y, f)
    x+=(1*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y-=(2.5*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    y+=(2.5*constantFontSize)
    linear(x, y, f)
    x-=(4*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    y+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(3*constantFontSize)
    linear(x, y, f)
    y+=(5*constantFontSize)
    linear(x, y, f)
    x-=(3*constantFontSize)
    y-=(5*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw5(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(3*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(3*constantFontSize)
    linear(x, y, f)
    y+=(2*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(6*constantFontSize)
    linear(x, y, f)
    y-=(4*constantFontSize)
    linear(x, y, f)
    x+=(4*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(3*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw6(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=(1*constantFontSize)
    linear(x, y, f) 
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(6*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(2*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)     
    
def draw7(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    y-=(9*constantFontSize)
    linear(x, y, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    x+=(5*constantFontSize)
    y+=(9*constantFontSize)
    linear(x, y, f)
    x-=(5*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)  
   
def draw8(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=(2*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    y+=(6*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)   
        
def draw9(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(6*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    y+=(6*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(2*constantFontSize)
    linear(x, y, f) 
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)   
    
def draw0(x, y, f, z, speed):
    startpoint(z, speed)
    y+=(2*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(2*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(6*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(2*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(6*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(1*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(6*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(2*constantFontSize)
    linear(x, y, f)
    r=(1*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(6*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawHypen(x, y, f, z, speed):
    space = globals()
    x+=(1*constantFontSize) 
    y+=(4*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(6*constantFontSize)
    linear(x, y, f)
    y+=(1*constantFontSize)
    linear(x, y, f)
    x-=(6*constantFontSize)
    linear(x, y, f)
    y-=(1*constantFontSize)
    linear(x, y, f)
    up(z, f)
    space['rightSpace'] +=1 
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawBox(z, f):
    tmpLeft = 20 - (constantFontSize*3)
    hght = (constantFontSize*2)
    hghtUp = constantFontSize*12
    tmpArr.append("G00X"+str(round(tmpLeft, 2))+"Y-"+str(round(hght, 2)))
    down(z, f)
    tmpArr.append("G01X"+str(round(tmpLeft, 2))+"Y"+str(round(hghtUp, 2)))
    tmpRightSpace = rightSpace+(constantFontSize*3)
    tmpArr.append("G01X"+str(round(tmpRightSpace,2))+"Y"+str(round(hghtUp, 2))+"F"+str(round(f,2)))
    tmpArr.append("G01X"+str(round(tmpRightSpace,2))+"Y-"+str(round(hght, 2))+"F"+str(round(f,2)))
    tmpArr.append("G01X"+str(round(tmpLeft, 2))+"Y-"+str(round(hght, 2)))
    up(z, f)

def drawSpace(x, y, f, z, speed):
    x+=(3*constantFontSize)
    setpoint(x, y, f)
    rightSpaceArr.append(rightSpace)
    
def finalDraw():
    with open("output.txt","w") as txt:
        for i in tmpArr:
            txt.write(i+"\n")
    
def convert(text, x, y, f, z, speed):
    checkSpace = globals()
    match text:
        case 'A':
            drawA(x, y, f, z, speed)
        case 'B':
            drawB(x, y, f, z, speed)
        case 'C':
            drawC(x, y, f, z, speed)
        case 'D':
            drawD(x, y, f, z, speed)
        case 'E':
            drawE(x, y, f, z, speed)
        case 'F':
            drawF(x, y, f, z, speed)
        case 'G':
            drawG(x, y, f, z, speed)
        case 'H':
            drawH(x, y, f, z, speed)
        case 'I':
            drawI(x, y, f, z, speed)
        case 'J':
            drawJ(x, y, f, z, speed)
        case 'K':
            drawK(x, y, f, z, speed)
        case 'L':
            drawL(x, y, f, z, speed)
        case 'M':
            drawM(x, y, f, z, speed)
        case 'N':
            drawN(x, y, f, z, speed)
        case 'O':
            drawO(x, y, f, z, speed)
        case 'P':
            drawP(x, y, f, z, speed)
        case 'Q':
            drawQ(x, y, f, z, speed)
        case 'R':
            drawR(x, y, f, z, speed)
        case 'S':
            drawS(x, y, f, z, speed)
        case 'T':
            drawT(x, y, f, z, speed)
        case 'U':
            drawU(x, y, f, z, speed)
        case 'V':
            drawV(x, y, f, z, speed)
        case 'W':
            drawW(x, y, f, z, speed)
        case 'X':
            drawX(x, y, f, z, speed)
        case 'Y':
            drawY(x, y, f, z, speed)
        case 'Z':
            drawZ(x, y, f, z, speed)
        case '1':
            draw1(x, y, f, z, speed)
        case '2':
            draw2(x, y, f, z, speed)
        case '3':
            draw3(x, y, f, z, speed)
        case '4':
            draw4(x, y, f, z, speed)
        case '5':
            draw5(x, y, f, z, speed)
        case '6':
            draw6(x, y, f, z, speed)
        case '7':
            draw7(x, y, f, z, speed)
        case '8':
            draw8(x, y, f, z, speed)
        case '9':
            draw9(x, y, f, z, speed)
        case '0':
            draw0(x, y, f, z, speed)
        case '-':
            drawHypen(x, y, f, z, speed)
        case ' ':
            drawSpace(x, y, f, z, speed)

def unitConvert(unit):
    match unit:
        case 'mm':
            return 1
        case 'cm':
            return 10
    

def convertFontSize(fontSize, unit):
    global constantFontSize
    match fontSize:
        case '6*10':
            constantFontSize = 1 * unit
        case '12*20':
            constantFontSize = 2 * unit
        case '18*30':
            constantFontSize = 3 * unit
        case '24*40':
            constantFontSize = 4 * unit
        case '30*50':
            constantFontSize = 5 * unit
        case '36*60':
            constantFontSize = 6 * unit
        case '42*70':
            constantFontSize = 7 * unit
        case '48*80':
            constantFontSize = 8 * unit
        case '54*90':
            constantFontSize = 9 * unit
        case '60*100':
            constantFontSize = 10 * unit
        case '66*110':
            constantFontSize = 11 * unit
        case '72*120':
            constantFontSize = 12 * unit
        case '78*130':
            constantFontSize = 13 * unit

def passText(text, x, y, f, z, fontSize, unit, speed):
    #Set fontSize as global
    intUnit = unitConvert(unit)
    convertFontSize(fontSize, intUnit)
    txt = list(text)
    for char in txt:
        if(x < rightSpace):
            x = rightSpace + (2*constantFontSize)
            convert(char, x, y, f, z, speed)
        else:
            convert(char, x, y, f, z, speed)
    #print(constantFontSize)

   


    

