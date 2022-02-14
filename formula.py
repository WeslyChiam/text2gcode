tmpArr=[]
global leftSpace
leftSpace = 0
global rightSpace
rightSpace = 0
leftSpaceArr = []
rightSpaceArr = []

def checkSpace(leftSpace, rightSpace, x):
    space = globals()
    if x <leftSpace:
        leftSpace = x
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

def drawA(x, y, f, z): #TEST RUN DONE 
    setpoint(x, y, f)
    down(z, f)
    linear(x, y, f)
    x-=7.6
    y-=20
    linear(x, y, f)
    up(z, f)
    x+=7.6
    y+=17.1
    setpoint(x, y, f)
    down(z, f)
    x-=6.6
    y-=17.1
    linear(x, y, f)
    x-=1
    linear(x, y, f)
    up(z, f)
    x+=7.6
    y+=17.1
    setpoint(x, y, f)
    down(z, f)
    x+=6.7
    y-=17.1
    linear(x, y, f)
    x+=0.9
    linear(x, y, f)
    x-=7.6
    y+=20
    linear(x, y, f)
    up(z, f)
    x-=4.7
    y-=14.3
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

def drawB(x, y, f, z): #TEST RUN DONE
    space = globals()
    setpoint(x, y, f)
    down(z, f)
    y-=20
    linear(x, y, f)
    up(z, f)
    x+=1
    y-=1
    setpoint(x, y, f)
    down(z, f)
    y-=18
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=19
    setpoint(x, y, f)
    down(z, f)
    x+=7.6
    linear(x, y, f)
    r=5.25
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=5.25
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x-=6
    y+=9.5
    setpoint(x, y, f)
    down(z, f)
    x+=6.6
    linear(x. y. f)
    r=4.25
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=4.25
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=6.6
    linear(x, y, f)
    x+=6.6
    linear(x, y, f)
    r=5.25
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=5.25
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=7.6
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=9.5
    setpoint(x, y, f)
    down(z, f)
    x+=6.6
    linear(x, y, f)
    r=4.25
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    r=4.25
    x-=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=6.6
    linear(x, y, f)
    

    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawC(x, y, f, z): #UPDATED FORMULA AND TEST RUN 
    setpoint(x, y, f)
    down(z, f)
    r=4
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x-=1
    linear(x, y, f)
    r=3
    x-=r
    y+=r
    anticlockwiseWthRad(x, y, r, f)
    r=3
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=5
    linear(x, y, f)
    r=3
    x+=(r*2)
    anticlockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)
    r=4
    x-=(r*2)
    clockwiseWthRad(x, y, r, f)
    y+=5
    linear(x, y, f)
    r=4
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawD(x, y, f, z): #TEST RUN DONE
    setpoint(x, y, f)
    down(z, f)
    y-=20
    linear(x, y, f)
    up(z, f)
    x+=0.9
    y+=19
    setpoint(x, y, f)
    down(z, f)
    y-=18
    linear(x, y, f)
    up(z, f)
    x-=0.9
    y+=19
    setpoint(x, y, f)
    down(z, f)
    x+=6.7
    linear(x, y, f)
    radi=0
    tmpy = y
    y-=20
    radj=(y-tmpy)/2
    clockwise(x, y, radi, radj, f)
    x-=6.7
    linear(x, y, f)
    up(z, f)
    x+=0.9
    y+=19
    setpoint(x, y, f)
    down(z, f)
    x+=5.8
    linear(x, y, f)
    tmpy = y
    y-=18
    radj=(y-tmpy)/2
    clockwise(x, y, radi, radj, f)
    x-=5.8
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawE(x, y, f, z): #TEST RUN DONE
    setpoint(x, y, f)
    down(z, f)
    y-=20
    linear(x, y, f)
    up(z, f)
    x+=0.9
    y+=19
    setpoint(x, y, f)
    down(z, f)
    y-=18
    linear(x, y, f)
    up(z, f)
    x-=0.9
    y+=19
    setpoint(x, y, f)
    down(z, f)
    x+=11.4
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=10.5
    linear(x, y, f)
    up(z, f)
    y-=8.5
    setpoint(x, y, f)
    down(z, f)
    x+=5.8
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=5.8
    linear(x, y, f)
    up(z, f)
    y-=8.5
    setpoint(x, y, f)
    down(z, f)
    x+=10.5
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=11.4
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawF(x, y, f, z): #TEST RUN DONE
    setpoint(x, y, f)
    down(z, f)
    y-=20
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y+=19
    linear(x, y, f)
    x+=8.5
    linear(x, y, f)
    y+=1
    linear(x, y, f)
    x-=9.5
    linear(x, y, f)
    up(z, f)
    x+=1
    y-=9.5
    setpoint(x, y, f)
    down(z, f)
    x+=5.7
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x-=5.7
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawG(x, y, f, z): #TEST RUN DONE
    setpoint(x, y, f)#
    down(z, f)#
    r = 2.5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    up(z, f)
    x-=2.5
    y+=2.5
    setpoint(x, y, f)
    down(z, f)
    r = 5
    x-=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    y-=5
    linear(x, y, f)
    r=5
    x+=r
    y-=r
    anticlockwiseWthRad(x, y, r, f)
    x+=2
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=1
    linear(x, y, f)
    y+=5
    linear(x, y, f)
    x-=3
    linear(x, y, f)
    y-=1
    linear(x, y, f)
    x+=2
    linear(x, y, f)
    y-=2
    linear(x, y, f)
    x-=2
    linear(x, y, f)
    r=4
    x-=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    y+=5
    linear(x, y, f)
    r=4
    x+=r
    y+=r
    clockwiseWthRad(x, y, r, f)
    r=1.5
    x+=r
    y-=r
    clockwiseWthRad(x, y, r, f)
    x+=1
    linear(x, y, f)    
    up(z, f)
    leftSpaceArr.append(leftSpace)
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

def passText(text, x, y, f, z):
    txt = list(text)
    for char in txt:
        if(x < rightSpace):
            differX = rightSpace - x
            x = rightSpace + differX +3
        if(char == 'C'):
            x+=4
            convert(char, x, y, f, z)
        else:
            convert(char, x, y, f, z)
    tmpArr=[]


    

