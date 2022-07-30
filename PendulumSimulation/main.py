import math
import pygame as pg
from pendulum_class import Pendulum
import time
pg.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)

#screen
screenwidht = 1920
screenheight = 1080
win = pg.display.set_mode((screenwidht,screenheight))


"""

You can choose between just a single oscillating pendulum, or if you put doublePendulum to true
you can see how two pendulums react to eachother in space (no gravity)

SETUP VARIABLES
"""
doublePENDULUM = False
if doublePENDULUM:
    alignPIVOTX = screenwidht/2
    alignPIVOTY = screenheight//20

    alignMIDX = -200
    alignMIDY = +200

    alignBOTX = 100
    alignBOTY = -50

    massMID = 1
    massBOT = 1
else:
    alignPIVOTX = screenwidht/2
    alignPIVOTY = screenheight//20

    endX  = 500
    endY  = 0

    mass = 5

def draw_screen(pendulum1, pendulum2, dots):
    win.fill(black)
    for dot in dots:
        pg.draw.circle(win, (255,255,255), dot, 1)
    pendulum1.show(win)
    pendulum2.show(win)
    pg.display.update()

def get_input(pendulum1, dots):
    run = True
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
        if event.type == pg.MOUSEBUTTONDOWN:
            pendulum1 = Pendulum(alignPIVOTX, alignPIVOTY, pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], 1, doublePENDULUM)
            dots = []
    return pendulum1, dots, run


def formula(one, two):
    """
    https://www.myphysicslab.com/pendulum/double-pendulum-en.html
    """
    g       = -one.g
    m1      = one.mass
    m2      = two.mass
    l1      = one.length
    l2      = two.length
    angle1  = one.angle
    angle2  = two.angle
    angleV1 = one.angleV
    angleV2 = two.angleV

    #angleA1
    term1 = -g*(2*m1+m2)*math.sin(angle1)
    term2 = -m2*g*math.sin(angle1-2*angle2)
    term3 = -2*math.sin(angle1-angle2)*m2*(angleV2*angleV2 * l2 + angleV1*angleV1*l1*math.cos(angle1-angle2))
    den   = l1*(2*m1+m2-m2*math.cos(2*angle1-2*angle2)) 
    angleA1 = (term1+term2+term3)/den 

    #angleA2
    term1 = 2*math.sin(angle1-angle2)
    term2 = (angleV1*angleV1 * l1 *(m1+m2)+g*(m1+m2)*math.cos(angle1)+angleV2*angleV2 * l2*m2*math.cos(angle1-angle2))
    den = l2*(2*m1+m2-m2*math.cos(2*angle1-2*angle2))
    angleA2 = (term1*term2)/den
    
    return angleA1, angleA2

def update(pendulum1, pendulum2):
    angleA1, angleA2 = formula(pendulum1, pendulum2)
    pendulum1.move(angleA1)
    pendulum2.x1 = pendulum1.x2
    pendulum2.y1 = pendulum1.y2
    pendulum2.move(angleA2)

def main():
    clk = pg.time.Clock()
    pg.display.set_caption("Pendulum")
    run = True

    if doublePENDULUM:
        pendulum1 = Pendulum(alignPIVOTX, alignPIVOTY,   alignPIVOTX+alignMIDX,    alignPIVOTY+alignMIDY,    massMID,  doublePENDULUM)
        pendulum2 = Pendulum(pendulum1.x2,  pendulum1.y2,       pendulum1.x2+alignBOTX,   pendulum1.y2+alignBOTY,      massBOT,  doublePENDULUM)
    else:
        pendulum2 = Pendulum(alignPIVOTX,  alignPIVOTY,       endX,   endY,   mass,  doublePENDULUM)
    dots = []

    frame = 0
    if doublePENDULUM:
        dotsamount = 20
    else:
        dotsamount = 2

    while run:
        if doublePENDULUM:
            clk.tick(2000)
            draw_screen(pendulum1, pendulum2, dots)
            update(pendulum1, pendulum2)
            pendulum1, dots, run = get_input(pendulum1, dots)
        else:
            clk.tick(60)
            draw_screen(pendulum2, pendulum2, dots)
            pendulum2.move(0)
            pendulum2, dots, run = get_input(pendulum2, dots)

        frame += 1
        if frame%dotsamount==0:
            dots.append((pendulum2.x2, pendulum2.y2))
        if len(dots)>500:
            dots.remove(dots[0])
    quit()

if __name__ == '__main__':
    main()