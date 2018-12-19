import os
import turtle
import player
import invader
import projectile
import math

#Game attributes
gamestate = 'playing' #start = homescreen, playing = game, end = gameover
playerscore = 0
level = 1
playerspeed = 10
invaderspeed = 2
projectilespeed = 20
number_of_invaders = 10
invaderx = -184
invadery = 180
liveInvaders = []
liveProjectiles = []
#Create invaders and player
for x in range(number_of_invaders):
    newInvader = invader.Invader(invaderspeed, invaderx, invadery)
    liveInvaders.append(newInvader)
    if invaderx > 184:
        invaderx = -184
        invadery -= 30
    else:
        invaderx += 30
p1 = player.Player(playerspeed)

#Game Controls
def onClickListener(x, y):
    '''Certain functionality depending on where screen is clicked'''
    if x > 100 and x < 200 and y > -260 and y < -210:
        global gamestate
        gamestate = 'end'
        print("quit clicked")
    return

def movePlayerLeft():
    '''Move player left, called on left arrow press'''
    p1.moveLeft()
    return

def movePlayerRight():
    '''Move player to the right, called on right arrow press'''
    p1.moveRight()
    return

def shootProjectile():
    '''creates a new projectile when the user presses spacebar'''
    newProjectile = projectile.Projectile(projectilespeed, p1.xcor())
    liveProjectiles.append(newProjectile)
#    os.system("afplay /sounds/shoot.wav/")
    return

#Game Functions
def checkGameOver():
    '''Returns whether or not the game is over from certain conditions'''
    if len(liveInvaders) == 0: #if there are no invaders remaining
        return True
    return False

def filter_turtles(projectiles, invaders):
    '''Returns the lists of only live projectiles and invaders'''
    for i in invaders:
        if i.invaderstate is 'hit':
            i.hideturtle()
    return ([p for p in projectiles if p.projectilestate is 'live'], [i for i in invaders if i.invaderstate is 'live'])

#Helper Functions
def collision(t1, t2):
    '''Returns whether or not two turtles overlap'''
    dist = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if dist < 15:
        return True
    return False

def remove_none_from_list(list):
    '''takes in a list and returns a new list with all None types removed'''
    return [elem for elem in list if elem is not None]

def checkProjectile(proj, invaders):
    '''returns a tuple of the modified projectile and the modified list of invaders'''
    if proj.ycor() >= 181: #check if the projectile reaches the top
        proj.hideturtle()
        proj.projectilestate = 'inactive'
    else: #check if the projectile hit an invader
        for invader in invaders:
            if collision(proj, invader):
                proj.hideturtle()
                proj.projectilestate = 'inactive'
                invader.destroy()
                invader.invaderstate = 'hit'
                global playerscore
                playerscore +=10
                score_pen.clear()
                score_pen.write("Score: %s" %playerscore, False, align='left', font=('Arial', 14, 'normal'))
    return (proj, invaders)

#Screen Setup
window = turtle.Screen()
os.chdir(os.getcwd() + '/img')
window.bgpic('spacebackground.gif')
os.chdir('..')
window.bgcolor('black')
window.title('Space Invaders')

#draw border
border_pen = turtle.Turtle() #create instance of a Turtle
border_pen.speed(0)
borderColors = ['red', 'blue', 'green', 'yellow']
border_pen.penup()
border_pen.setposition(-200, -200)
border_pen.pendown()
for x in range(4):
    border_pen.color(borderColors[x])
    border_pen.fd(400)
    border_pen.lt(90)
border_pen.penup()

#draw quit button (using border_pen instead of making a new turtle)
border_pen.setposition(200, -210)
border_pen.color('black', 'red')
border_pen.begin_fill()
border_pen.setheading(180)
for x in range(4):
    if x%2 == 0:
        border_pen.fd(100)
    else:
        border_pen.fd(50)
    border_pen.lt(90)
border_pen.end_fill()
border_pen.setposition(150, -245)
border_pen.write("QUIT", False, align='center', font=('Arial', 20, 'normal'))
border_pen.hideturtle()

#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.color('white')
score_pen.setposition(-200, 205)
score_pen.write("Score: %s" %playerscore, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

#draw level
level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.penup()
level_pen.color('white')
level_pen.setposition(-80, 205)
level_pen.write("Level: %s" %level, False, align='left', font=('Arial', 14, 'normal'))
level_pen.hideturtle()

#Key bindings
window.onkeypress(movePlayerLeft, "Left")
window.onkeypress(movePlayerRight, "Right")
window.onkeypress(shootProjectile, "space")
window.onscreenclick(onClickListener, 1)

#main game loop
gameactive = True
while gameactive:

    while gamestate == 'start':
        window.listen()

    while gamestate == 'playing':

        #Remove projectiles or invaders
        temp = filter_turtles(liveProjectiles, liveInvaders)
        liveProjectiles = temp[0]
        liveInvaders = temp[1]
        #Check if the game is over
        if checkGameOver():
            break

        window.listen()

        #Move invaders
        for i in liveInvaders:
            i.move()
        #Move projectiles
        for p in liveProjectiles:
            p.move()

        #Check if the player projectile hit an invader or went off the Screen
        for x in range(len(liveProjectiles)):
            temp = checkProjectile(liveProjectiles[x], liveInvaders)
            liveProjectiles[x] = temp[0]
            liveInvaders = temp[1]
    break;
    while gamestate == 'end':
        window.listen()
        gameactive = False

    print("game over")
