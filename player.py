import turtle
import os

class Player(turtle.Turtle):

    def __init__(self, initSpeed):
        '''initialize a turtle for the player given a speed to move the player at'''
        turtle.Turtle.__init__(self)
        os.chdir(os.getcwd() + '/img')
        turtle.addshape('player.gif')
        os.chdir('..')
        self.playerspeed = initSpeed
        self.color('white')
        self.shape('player.gif')
        self.penup()
        self.speed(0)
        self.setposition(0, -185) #bottom middle of screen
        self.setheading(90) #rotate 90 degrees CCW

    def moveLeft(self):
        '''moves the player to the left'''

        x = self.xcor()
        if x <= -190:
            return
        x -= self.playerspeed
        self.setx(x)

    def moveRight(self):
        '''moves the player to the right'''

        x = self.xcor()
        if x >= 190:
            return
        x += self.playerspeed
        self.setx(x)
