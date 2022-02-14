def drawA(x, y, f, z):
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

def drawB(x, y, f, z):
    space = globals()
    setpoint(x, y, f)
    down(z, f)
    y-=20
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=19
    setpoint(x, y, f)
    down(z, f)
    y-=18
    linear(x, y, f)
    up(z, f)
    x-=1
    y+=19
    setpoint(x, y, f)
    down(z, f)
    x+=7.6
    linear(x, y, f)
    space['rightSpace'] = x + 2.88
    radi=0
    tmpy = y
    y-=10.5
    radj=(y-tmpy)/2
    clockwise(x, y, radi, radj, f)
    up(z, f)
    x-=6.6
    y+=9.5
    setpoint(x, y, f)
    down(z, f)
    x+=6.6
    linear(x, y, f)
    tmpy = y
    y-=8.5
    radj=(y-tmpy)/2
    clockwise(x, y, radi, radj, f)
    x-=6.6
    linear(x, y, f)
    x+=6.6
    linear(x, y, f)
    tmpy = y
    y-=10.5
    radj=(y-tmpy)/2
    clockwise(x, y, radi, radj, f)
    x-=7.6
    linear(x, y, f)
    up(z, f)
    x+=1
    y+=9.5
    setpoint(x, y, f)
    down(z, f)
    x+=6.6
    linear(x, y, f)
    tmpy = y
    y-=8.5
    radj=(y-tmpy)/2
    clockwise(x, y, radi, radj, f)
    x-=6.6
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)
    
def drawC(x, y, f, z):
    setpoint(x, y, f)
    down(z, f)
    radi=0
    tmpy = y
    y-=20
    radj=(y-tmpy)/2
    anticlockwise(x, y, radi, radj, f)
    x+=1.5
    linear(x, y, f)
    y+=1.3
    linear(x, y, f)
    x-=1.5
    linear(x, y, f)
    tmpy = y
    y+=17.4
    radj=(y-tmpy)/2
    clockwise(x, y, radi, radj, f)
    x+=1.5
    linear(x, y, f)
    y+=1.3
    linear(x, y, f)
    x-=1.5
    linear(x, y, f)
    up(z, f)
    leftSpaceArr.append(leftSpace)
    rightSpaceArr.append(rightSpace)

def drawD(x, y, f, z):
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

def drawE(x, y, f, z):
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
    x-=11.4
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
