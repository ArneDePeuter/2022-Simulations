from tkinter import Y
from numpy import ubyte
import pygame
from math import pi, sin
import random
TWOPI = pi*2

class Wave:
    def __init__(self, period, amplitude, offset, wavespeed) -> None:
        self.period = period
        self.amplitude = amplitude
        self.offset = offset

        self.wavespeed = wavespeed
    
    def f(self, x):
        w = TWOPI/self.period
        return sin(w*x + self.offset) * self.amplitude

    def update(self):
        self.offset += self.wavespeed
        self.amplitude += random.choice([1,-1])*self.wavespeed
        self.period += random.choice([1,-1])*self.wavespeed
        