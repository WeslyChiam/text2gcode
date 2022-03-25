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
    x+=(30*constantFontSize)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(30*constantFontSize)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y+=(65*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y-=(65*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(15*constantFontSize)
    y+=(20*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(30*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x-=(5*constantFontSize)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x-=(21*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawB(x, y, f, z): #UPDATED FORMULA AND TEST RUN 
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(32.5*constantFontSize)
    linear(x, y, f)
    r=(27.5*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(27.5*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(22.5*constantFontSize)
    linear(x, y, f)
    x+=(22.5*constantFontSize)
    linear(x, y, f)
    r=(17.5*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(17.5*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(22.5*constantFontSize)
    linear(x, y, f)
    y+=(80*constantFontSize)
    linear(x, y, f)
    x+=(22.5*constantFontSize)
    linear(x, y, f)
    r=(17.5*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(17.5*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(22.5*constantFontSize)
    linear(x, y, f)
    x+=(22.5*constantFontSize)
    linear(x, y, f)
    r=(27.5*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(27.5*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(32.5*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawC(x, y, f, z): #UPDATED FORMULA AND TEST RUN
    startpoint(z)
    y+=(20*constantFontSize) 
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(60*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(60*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawD(x, y, f, z): #TEST RUN DONE
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    r=(50*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(50*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(10*constantFontSize)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    y+=(80*constantFontSize)
    linear(x, y, f)
    r=(40*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(40*constantFontSize)
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
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    linear(x, y, f)
    y-=(35*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    linear(x, y, f)
    y-=(35*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(60*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawF(x, y, f, z): #TEST RUN DONE
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    linear(x, y, f)
    y-=(35*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    linear(x, y, f)
    y-=(45*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawG(x, y, f, z): #TEST RUN DONE
    startpoint(z)
    y+=(20*constantFontSize) 
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(20*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(60*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(60*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawH(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(45*constantFontSize)
    linear(x, y, f)
    x+=(40*constantFontSize)
    linear(x, y, f)
    y+=(45*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y+=(45*constantFontSize)
    linear(x, y, f)
    x-=(40*constantFontSize)
    linear(x, y, f)
    y-=(45*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)  
    up(z, f)
    leftSpaceArr.append(leftSpace) 
    rightSpaceArr.append(rightSpace)

def drawI(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=(60*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(25*constantFontSize)
    linear(x, y, f)
    y+=(80*constantFontSize)
    linear(x, y, f)
    x+=(25*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(25*constantFontSize)
    linear(x, y, f)
    y-=(80*constantFontSize)
    linear(x, y, f)
    x-=(25*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawJ(x, y, f, z):
    startpoint(z)
    y+=(20*constantFontSize) 
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(80*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y-=(80*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawK(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(40*constantFontSize)
    linear(x, y, f)
    x+=(40*constantFontSize)
    y+=(40*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    y-=(50*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    y-=(50*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    x-=(40*constantFontSize)
    y+=(40*constantFontSize) 
    linear(x, y, f)
    y-=(40*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawL(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(90*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(60*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawM(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(30*constantFontSize)
    y-=(40*constantFontSize)
    linear(x, y, f)
    x+=(30*constantFontSize)
    y+=(40*constantFontSize)
    linear(x, y, f)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y+=(70*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y-=(30*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y+=(30*constantFontSize)
    linear(x, y, f)
    y-=(70*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawN(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y-=(100*constantFontSize)
    linear(x, y, f)
    y+=(20*constantFontSize)
    linear(x, y, f)
    x-=(40*constantFontSize)
    y+=(80*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawO(x, y, f, z):
    startpoint(z)
    y+=(50*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(50*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=(50*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(50*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(50*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(40*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=(40*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(40*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(40*constantFontSize)
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
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(35*constantFontSize)
    linear(x, y, f)
    r=(25*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(25*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(25*constantFontSize)
    linear(x, y, f)
    y-=(50*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(10*constantFontSize)
    y+=(90*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(25*constantFontSize)
    linear(x, y, f)
    r=(15*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(15*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(25*constantFontSize)
    linear(x, y, f)
    y+=(30*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawQ(x, y, f, z):
    startpoint(z)
    y+=(50*constantFontSize) 
    setpoint(x, y, f)
    down(z, f)
    r=(50*constantFontSize)
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    r=(50*constantFontSize)
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(40*constantFontSize)
    x+=(r*2)
    clockwiseWthRad(x, y, r, f)
    r=(40*constantFontSize)
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x+=(65*constantFontSize)
    y-=(25*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    x+=(15*constantFontSize)
    y-=(25*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    x-=(15*constantFontSize)
    y+=(25*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawR(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(35*constantFontSize)
    linear(x, y, f)
    r=(25*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=(25*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(25*constantFontSize)
    linear(x, y, f)
    x+=(40*constantFontSize)
    y-=(50*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    x-=(40*constantFontSize)
    y+=(50*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y-=(50*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(10*constantFontSize)
    y+=(90*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(25*constantFontSize)
    linear(x, y, f)
    r=(15*constantFontSize)
    y-=(r*2)
    clockwiseWthRad(x, y, r, f)
    x-=(25*constantFontSize)
    linear(x, y, f)
    y+=(30*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawS(x, y, f, z):
    startpoint(z)
    y+=(20*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(50*constantFontSize)
    y+=(60*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(50*constantFontSize)
    y-=(60*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawT(x, y, f, z):
    startpoint(z)
    x+=(25*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y+=(90*constantFontSize)
    linear(x, y, f)
    x+=(25*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(25*constantFontSize)
    linear(x, y, f)
    y-=(90*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawU(x, y, f, z):
    startpoint(z)
    y+=(100*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    y-=(80*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(80*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y-=(80*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(80*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
       
def drawV(x, y, f, z):
    startpoint(z)
    y+=(100*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(20*constantFontSize)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    x+=(20*constantFontSize)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y-=(90*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y+=(90*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawW(x, y, f, z):
    startpoint(z)
    y+=(100*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(10*constantFontSize)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    y+=(40*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    y-=(40*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y+=(70*constantFontSize)
    x-=(20*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y-=(70*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawX(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=(50*constantFontSize)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    y+=(100*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(50*constantFontSize)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    y+=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawY(x, y, f, z):
    startpoint(z)
    y+=(100*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(25*constantFontSize)
    y-=(40*constantFontSize)
    linear(x, y, f)
    y-=(60*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y+=(60*constantFontSize)
    linear(x, y, f)
    x+=(25*constantFontSize)
    y+=(40*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y-=(30*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y+=(30*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawZ(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=(60*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    y+=(80*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    y-=(80*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw1(x, y, f, z):
    startpoint(z)
    y+=(80*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    y+=(5*constantFontSize)
    linear(x, y, f)
    x+=(15*constantFontSize)
    y+=(15*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(100*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y+=(80*constantFontSize)
    linear(x, y, f)
    x-=(15*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw2(x, y, f, z):
    startpoint(z)
    setpoint(x, y, f)
    down(z, f)
    x+=(60*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    y+=(60*constantFontSize)
    linear(x, y, f)
    r=(30*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(30*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=(2*r)
    clockwiseWthRad(x, y, r, f)
    x-=(50*constantFontSize)
    y-=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 

def draw3(x, y, f, z):
    startpoint(z)
    y+=(20*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    y+=(30*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    linear(x, y, f)
    x-=(20*constantFontSize)
    y-=(30*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw4(x, y, f, z):
    startpoint(z)
    y+=(25*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x+=(40*constantFontSize)
    y+=(65*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(65*constantFontSize)
    linear(x, y, f)
    x+=(10*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y-=(25*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    y+=(25*constantFontSize)
    linear(x, y, f)
    x-=(40*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(10*constantFontSize)
    y+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(30*constantFontSize)
    linear(x, y, f)
    y+=(50*constantFontSize)
    linear(x, y, f)
    x-=(30*constantFontSize)
    y-=(50*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw5(x, y, f, z):
    startpoint(z)
    y+=(20*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(30*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(30*constantFontSize)
    linear(x, y, f)
    y+=(20*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(60*constantFontSize)
    linear(x, y, f)
    y-=(40*constantFontSize)
    linear(x, y, f)
    x+=(40*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(30*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def draw6(x, y, f, z):
    startpoint(z)
    y+=(20*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=(10*constantFontSize)
    linear(x, y, f) 
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(60*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(20*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)     
    
def draw7(x, y, f, z):
    startpoint(z)
    y+=(100*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    y-=(90*constantFontSize)
    linear(x, y, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    x+=(50*constantFontSize)
    y+=(90*constantFontSize)
    linear(x, y, f)
    x-=(50*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)  
   
def draw8(x, y, f, z):
    startpoint(z)
    y+=(20*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    r=(20*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(1*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    y+=(60*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)   
        
def draw9(x, y, f, z):
    startpoint(z)
    y+=(20*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(60*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(10*constantFontSize)
    y+=(60*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    y-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=(20*constantFontSize)
    linear(x, y, f) 
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)   
    
def draw0(x, y, f, z):
    startpoint(z)
    y+=(20*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(20*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(60*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(20*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(60*constantFontSize)
    linear(x, y, f)
    up(z, f)
    x+=(10*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    r=(10*constantFontSize)
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x+=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    y+=(60*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    x-=(20*constantFontSize)
    linear(x, y, f)
    r=(10*constantFontSize)
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=(60*constantFontSize)
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace) 
    
def drawHypen(x, y, f, z):
    space = globals()
    x+=(20*constantFontSize) 
    y+=(40*constantFontSize)
    setpoint(x, y, f)
    down(z, f)
    x+=(60*constantFontSize)
    linear(x, y, f)
    y+=(10*constantFontSize)
    linear(x, y, f)
    x-=(60*constantFontSize)
    linear(x, y, f)
    y-=(10*constantFontSize)
    linear(x, y, f)
    up(z, f)
    space['rightSpace'] +=2 
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawBox(z, f):
    tmpArr.append("G00X17Y-3")
    down(z, f)
    hght = (constantFontSize*100)+3
    tmpArr.append("G01X17Y"+str(round(hght, 2)))
    tmpRightSpace = rightSpace+3
    tmpArr.append("G01X"+str(round(tmpRightSpace,2))+"Y"+str(round(hght, 2))+"F"+str(round(f,2)))
    tmpArr.append("G01X"+str(round(tmpRightSpace,2))+"Y-2"+"F"+str(round(f,2)))
    tmpArr.append("G01X17Y-3")
    up(z, f)

def drawSpace(x, y, f, z):
    x+=(30*constantFontSize)
    setpoint(x, y, f)
    rightSpaceArr.append(rightSpace)
    
def finalDraw():
    with open("output.txt","w") as txt:
        for i in tmpArr:
            txt.write(i+"\n")
    
def convert(text, x, y, f, z):
    checkSpace = globals()
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
        case ' ':
            drawSpace(x, y, f, z)

def convertFontSize(fontSize):
    global constantFontSize
    match fontSize:
        case '6*10 units':
            constantFontSize = 1
        case '12*20 units':
            constantFontSize = 2
        case '18*30 units':
            constantFontSize = 3
        case '24*40 unita':
            constantFontSize = 4
        case '30*50 units':
            constantFontSize = 5

def passText(text, x, y, f, z, fontSize):
    #Set fontSize as global
    convertFontSize(fontSize)
    txt = list(text)
    for char in txt:
        if(x < rightSpace):
            x = rightSpace + (10*constantFontSize)
            convert(char, x, y, f, z)
        else:
            convert(char, x, y, f, z)
    #print(constantFontSize)

   


    

