#modules
import math
from tkinter.messagebox import NO
import pygame

"""
source : https://en.wikipedia.org/wiki/Pendulum#Simple_gravity_pendulum
"""

class Pendulum:
    """
    You firstly initialise the pivot point, this is x1 and x2.
    With the angle and the length of the rod you calculate the coordinates of the massPoint. This is basic goniometry.
    Furthermore the massPoint obviously has a mass.
    """
    def __init__(self, x1, y1, x2, y2, mass, doublepend):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.doublepend = doublepend

        self.length = math.sqrt(math.pow(self.x2-self.x1,2)+math.pow(self.y2-self.y1,2))
        if self.y2>self.y1:
            self.angle = -math.asin((self.x1-self.x2)/self.length)
        else:
            self.angle = math.asin((self.y1-self.y2)/self.length)
            if self.x2>self.x1:
                self.angle += math.pi/2
            else:
                self.angle -= math.pi

        self.angleA = 0
        self.angleV = 0
        self.damping = 0.99

        #formula of gravity
        self.g = -0.005
        self.mass = mass
        self.gravityForce = self.mass*self.g


    def move(self, doublePendAcc):
        if self.doublepend:
            self.angleA = doublePendAcc
            self.angleV += doublePendAcc
            self.angleV *= self.damping
            self.angle += self.angleV
        else:
            self.angleA = self.gravityForce * math.sin(self.angle)
            self.angleV += self.angleA
            self.angleV *= self.damping
            self.angle += self.angleV

        self.x2 = math.sin(self.angle)*self.length+self.x1
        self.y2 = math.cos(self.angle)*self.length+self.y1

    def show(self, win):
        """
        Firstly draws the rod, then the pivot and finally the massPoint
        """
        pygame.draw.line(win, (255,255,255), (self.x1, self.y1), (self.x2, self.y2))
        pygame.draw.circle(win, (255,0,0), (self.x1, self.y1), 5)
        pygame.draw.circle(win, (255,125,125), (self.x2, self.y2), 10)
