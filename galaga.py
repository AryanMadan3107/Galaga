import pgzrun

WIDTH=800
HEIGHT=600

galaga=Actor("galaga")
galaga.pos=(400,550)
bugs=[]
for l in range(2):
    for i in range(5):
        bug=Actor("bug")
        bugs.append(bug)
        bugs[-1].x=20+55*i
        bugs[-1].y=40*l
d=1
md=False
bullets=[]
score=0
bugr=[]
bulletr=[]
gameover=False

def draw():
    global gameover
    screen.fill("#ba03fc")
    galaga.draw()
    for bug in bugs:
        bug.draw()
    for bullet in bullets:
        bullet.draw()
    screen.draw.text(str(score),(20,20))
    if len(bugs)==0:
        screen.draw.text("You win!",(300,300), fontsize=100)
    if gameover==True:
        screen.fill("orange")
        screen.draw.text("You died, this is what you scored: "+ str(score),center=(400,300),fontsize=50,color="blue")
    

def update():
    global d, md, score, gameover
    md = False
    if keyboard.left:
        galaga.x-=10
        if galaga.x<=50:
            galaga.x=50
    if keyboard.right:
        galaga.x+=10
        if galaga.x>=750:
            galaga.x=750
    if len(bugs)>0 and (bugs[0].x<20 or bugs[-1].x>780):
        d=d*-1
        md=True
    for bug in bugs:
        if bug.colliderect(galaga):
           gameover=True

    
    bulletr.clear()
    bugr.clear()

    for bug in bugs:
        bug.x+=d*10  
        if md:
            bug.y+=10
        for bullet in bullets:
            if bug.colliderect(bullet):
                bugr.append(bug)
                bulletr.append(bullet)
                score+=1
    for bug in bugr:
        if bug in bugs:
            bugs.remove(bug)
    for bullet in bulletr:
        if bullet in bullets:
            bullets.remove(bullet)

    for bullet in bullets:
        bullet.y-=3

def on_key_down(key):
    if key == keys.SPACE:
        bullet=Actor("bullet")
        bullets.append(bullet)
        bullet.x=galaga.x
        bullet.y=galaga.y-37 

pgzrun.go()
