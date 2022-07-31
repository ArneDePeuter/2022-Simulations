import pygame as pg
from waves import TWOPI, Wave
from random import randint

pg.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)

#setup
screenwidht = 1000
screenheight = 600
step = 1
radius = 3
amount = 10


win = pg.display.set_mode((screenwidht,screenheight))

def y_combine(x, waves):
    y = 0
    for wave in waves:
        y+=wave.f(x)
        wave.update()
    return y+screenheight/2

def draw_screen(waves):
    win.fill(black)
    for x in range(0, screenwidht, step):
        pg.draw.circle(win, (randint(0,255),randint(0,255),randint(0,255)), (x,y_combine(x, waves)), radius)
    pg.display.update()

def get_input():
    run = True
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
        if event.type == pg.KEYDOWN:
            pass
    return run

def getWaves(amount):
    waves = []
    for _ in range(amount):
        waves.append(Wave(randint(1, screenwidht), randint(1, screenheight/amount), randint(1, screenwidht), 0.0001))
    return waves

def main():
    clk = pg.time.Clock()
    pg.display.set_caption("Waves")
    run = True

    waves = getWaves(amount)

    while run:
        clk.tick(30)


        draw_screen(waves)
        run = get_input()

    quit()

if __name__ == '__main__':
    main()