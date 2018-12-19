from turtle import Turtle

class Projectile(Turtle):

    def __init__(self, initSpeed, xcor):
        '''initialize projectile the player shoots'''

        Turtle.__init__(self)
        self.projectilespeed = initSpeed
        self.projectilestate = 'live'
        self.color('yellow')
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setposition(xcor, -180)
        self.shapesize(.5, .5)
        self.setheading(90)

    def move(self):
        y = self.ycor()
        y+= self.projectilespeed
        self.sety(y)
