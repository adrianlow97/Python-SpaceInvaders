import turtle
import os

class Invader(turtle.Turtle):

    def __init__(self, initSpeed, startx, starty):
        '''initialize a turtle for the invader given a speed to move the invader at'''
        turtle.Turtle.__init__(self)
        os.chdir(os.getcwd() + '/img')
        turtle.addshape('invader.gif')
        turtle.addshape('explosion.gif')
        os.chdir('..')
        self.invaderspeed = initSpeed
        self.invaderstate = 'live'
        self.shape('invader.gif')
        self.penup()
        self.speed(0)
        self.setposition(startx, starty)

    def move(self):
        '''moves the invader'''

        x = self.xcor()
        if x <= -185 or x >= 185:
            self.invaderspeed *= -1
            y = self.ycor()
            y -= 30
            self.sety(y)
        x += self.invaderspeed
        self.setx(x)
        return

    def destroy(self):
        '''changes the invader to an explosion, called when hit by projectile'''
        self.shape('explosion.gif')
        self.invaderspeed = 0
        return
