xpos1=0
xpos2=0.0693
op=0.75
r=xpos2-xpos1
permeability=1.25663753*10**-6 #permeability in air
len1=.005
len2=.005
vol1=len1**3*4/3*pi
vol2=len2**3*4/3*pi
q1=vol1*0.25/(permeability*len1)
q2=q1*len2/r
mass1=0.05
mass2=0.05
v1=0.08
dt=0.01
a=10
A=(len1)**2*4*pi
eject=0;


t=0
scene.append_to_caption("Note: Force arrows not scaled in order to make program viewable\n")

    

ball1=sphere(pos=vec(xpos1,0,0),(radius=len1))
rod = cylinder(pos=vector(xpos2,0,0),         axis=vec(len1,0,0), radius=len1,color=vec(1,0,0))
ball2=sphere(pos=vec(len1*2+xpos2,0,0),(radius=len1))
ball3=sphere(pos=vec(len1*4+xpos2,0,0),(radius=len1))
ball4=sphere(pos=vec(len1*6+xpos2,0,0),(radius=len1))
fakerod=cylinder(pos=vec(xpos2,0,0),axis=vec(len1*50,0,0), radius=len2)
scene.autoscale = False
mybox = box(pos=vector(xpos1,-len1*6/5,0),length=1000, height=len1/2, width=10000)

fakerod.visible=False;


scene.append_to_caption('Size (m)')
def lengts1 (lengts1):
    global lengone
    lengOne=lengts1.value
    global len1
    len1=lengOne


    ball1.radius=len1
    rod.axis.x=len1
    ball2.radius=len1
    ball3.radius=len1
    ball4.radius=len1
    rod.radius=len1
    vol1=len1**3*4/3*pi
    fakerod.axis.x=len1*50
    mybox.pos.y=-len1*6/5
    mybox.height=len1/2
    ball2.pos.x=len1*2+xpos2
    ball3.pos.x=len1*4+xpos2
    ball4.pos.x=len1*6+xpos2
    
slider( bind=lengts1, min=0, max= 0.25, value= 0.001)
scene.append_to_caption('\n\n')
scene.append_to_caption('Position of Approaching Ball (m)')
def pot1(pot1):
    xpos1=pot1.value
    ball1.pos.x=xpos1
    mybox.pos.x=xpos1
    
slider( bind=pot1, min=0, max= 0.05, value= 0.025)

scene.append_to_caption('\n\n')
scene.append_to_caption('Position of magnet (m)')
def pot2(pot2):
    xpos2=pot2.value
    rod.pos.x=xpos2
    ball2.pos.x=xpos2+len1*2
    ball3.pos.x=xpos2+len1*4
    ball4.pos.x=xpos2+len1*6
    
slider( bind=pot2, min=0, max= 0.1, value= 0.025)

scene.append_to_caption('\n\n')
def Force(r):
    global showForce=False
    showForce=!showForce
checkbox(bind=Force, text='Show Forces (not scaled)', checked=False) # text to right of checkbox
def Graph(r):
    global showGraph=False
    showGraph=!showGraph
checkbox(bind=Graph, text='Show Graphs (Increases lag)', checked=False) # text to right of checkbox
r=xpos2-xpos1
permeability=1.25663753*10**-6 #permeability in air
vol1=len1**3*4/3*pi
vol2=len2**3*4/3*pi
q1=vol1*0.25/(permeability*len1)
q2=q1*len2/r
mass1=0.05
mass2=0.05
v1=0.08
dt=0.01
A=(len1)**2*4*pi
eject=0;
scene.pause('Click here to start animation')
#ball2=sphere(pos=vec(xpos2,0,0),(radius=rad))



#while (abs(ball1.pos.x-rod.pos.x)-len1-1>0):

done=0
if (showGraph):
    g1=graph(title='Velocity of Incoming Ball vs. Position of Incoming Ball',xtitle="Position (x)", ytitle="Velocity (m/s)")
    x1=gdots()
    scene.append_to_caption('\n\n')
    g2=graph(title='Position of Ejected Ball vs. Time',xtitle="Time (s)", ytitle="Position (s)")
    x2=gdots()
    scene.append_to_caption('\n\n')
    g4=graph(title='Kinetic Energy of Incoming Ball vs. Position of Incoming Ball',ytitle="Kinetic Energy (J)", xtitle="Position (m/s)")
    x4=gdots()
    scene.append_to_caption('\n\n')
    g3=graph(title='Kinetic Energy of Ejected Ball vs. Position of Ejected Ball',ytitle="Kinetic Energy (J)", xtitle="Position (m/s)")
    x3=gdots()
    scene.append_to_caption('\n\n')
    g6=graph(ytitle='Momentum of Incoming Ball(kg*m/s)', xtitle="Position (m/s)",title="Momentum of Incoming Ball vs. Position of Incoming Ball")
    x6=gdots()
    scene.append_to_caption('\n\n')
    g5=graph(title="Momentum of Ejected Ball vs. Position of Ejected Ball", ytitle="Momentum(kg*m/s)", xtitle="Position (m/s)")
    x5=gdots()

dPE=abs((1/(3*(xpos2-xpos1)**3)-1/(3*(len1+len2)**3))*A*vol1**2/(32*pi**2*len1**2*permeability))
if(showForce):
    friction= arrow(pos=vector(xpos1-len1,0,0),axis=vec(-0.02*9.8*mass1*5/2,0,0) ,shaftwidth=len1/2,opacity =op)
    n= arrow(pos=vector(xpos1+len1,0,0),axis=vec((q1/(4*pi*r**2))**2*A*permeability/2-0.002*mass1*9.8,0,0),shaftwidth=len1/2,opacity =op)
while (ball1.pos.x<rod.pos.x and done==0):
    if (showGraph):
        rate(120)     
    else:
        rate(66)
    force=(q1/(4*pi*r**2))**2*A*permeability/2-0.00001*mass1*9.8
    if(showForce):
        n.axis.x=force/a
    v1+=force/mass1*dt
    
    if (ball1.pos.x+v1*dt>rod.pos.x-len1):
        ball1.pos.x=rod.pos.x-len1
        eject=1
    else:
        ball1.pos.x+=v1*dt
        
        
    
    r=abs(rod.pos.x-ball1.pos.x)
    if prevposx!=ball1.pos.x:
        if showGraph:
            x1.plot(ball1.pos.x-xpos1,v1)
            x4.plot(ball1.pos.x-xpos1,v1**2*0.5*mass1)
            x6.plot(ball1.pos.x-xpos1,v1*mass1)
    else:
        done=1
    prevposx=ball1.pos.x
    if(showForce):
        friction.pos.x=ball1.pos.x-len1
        n.pos.x=ball1.pos.x+len1

while (eject==1 and t<2):
    if (showGraph):
        rate(120)     
    else:
        rate(66)
    
    vball=sqrt(2*dPE/mass1)
    #vball=v1
    forceeject=(q1/(4*pi*(ball4.pos.x-rod.pos.x)**2))**2*A*permeability/2
    ball4.pos.x+=dt*vball
    #vball-=forceeject/mass1*dt
    if (showGraph):
        x2.plot(t,ball4.pos.x-len1*6+xpos2)
        x3.plot(ball4.pos.x-len1*6+xpos2,vball**2*0.5*mass2)
        x5.plot(ball4.pos.x-len1*6+xpos2,vball*mass2)
    t+=dt

