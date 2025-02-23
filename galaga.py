import pgzrun

WIDTH=800
HEIGHT=600

galaga=Actor("galaga")
galaga.pos=(400,550)
bug=Actor("bug")
bullet=Actor("bullet")

def draw():
    screen.fill("#ba03fc")
    galaga.draw()
    bug.draw()
    bullet.draw()

def update():
    if keyboard.left:
        galaga.x-=10
        if galaga.x<=50:
            galaga.x=50
    if keyboard.right:
        galaga.x+=10
        if galaga.x>=750:
            galaga.x=750

pgzrun.go()