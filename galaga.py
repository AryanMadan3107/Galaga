import pgzrun

WIDTH=800
HEIGHT=600

galaga=Actor("galaga")
galaga.pos=(400,550)
bugs=[]
for i in range(5):
    bug=Actor("bug")
    bugs.append(bug)
    bugs[-1].x=20+55*i
    bugs[-1].y=0
d=1
md=False
bullets=[]

def draw():
    screen.fill("#ba03fc")
    galaga.draw()
    for bug in bugs:
        bug.draw()
    for bullet in bullets:
        bullet.draw()

def update():
    global d, md
    if keyboard.left:
        galaga.x-=10
        if galaga.x<=50:
            galaga.x=50
    if keyboard.right:
        galaga.x+=10
        if galaga.x>=750:
            galaga.x=750
    if bugs[0].x<20 or bugs[-1].x>780:
        d=d*-1
        md=True
    for bug in bugs:
        bug.x+=d*1
        if md==True:
 #   for bug in bugs:    
            if bug.y<=HEIGHT:
                bug.y+=1        
    for bullet in bullets:
        bullet.y-=5

def on_key_down(key):
    if key == keys.SPACE:
        bullet=Actor("bullet")
        bullets.append(bullet)
        bullet.x=galaga.x
        bullet.y=galaga.y-37 
    


pgzrun.go()