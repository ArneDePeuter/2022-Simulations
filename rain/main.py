import matplotlib.pyplot as plt
import pygame as pygame
import random
from matplotlib import pyplot as plot
pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)

#screen
screenwidht = 500
screenheight = 500
floorwidth = round(screenheight/10)
floor = screenheight-floorwidth
win = pygame.display.set_mode((screenwidht,screenheight))

class Person:
    def __init__(self, width, heigth, v):
        self.x = 0
        self.width = width
        self.heigth = heigth
        self.v = v
        self.wetness = 0

    def show(self):
        pygame.draw.rect(win, (255,255,255), (self.x, floor - self.heigth, self.width, self.heigth))

    def update(self):
        self.x += self.v

class Raindrop:
    def __init__(self, x, vx, vy):
        self.x = x
        self.vx = vx
        self.y = 0
        self.vy = vy

    def show(self):
        pygame.draw.line(win, (0,0,255), (self.x, self.y), (self.x-self.vx, self.y-self.vy))

    def update(self):
        self.x += self.vx
        self.y += self.vy

def restart(person, v_list, wetnesses, step):
    wetnesses.append(person.wetness)
    v_list.append(person.v)
    person = Person(10, 50, person.v + step)
    return v_list, wetnesses, person

def spawn_raindrop(rain):
    rain.append(Raindrop(random.randint(0,screenwidht), -1, 5))

def check_remove(raindrop, rain, person):
    if raindrop.x >= person.x and raindrop.x <= person.x + person.width and raindrop.y >= floor - person.heigth:
        rain.remove(raindrop)
        person.wetness += 1
    elif raindrop.y >= floor:
        rain.remove(raindrop)

def update(rain, person):
    person.update()
    for raindrop in rain:
        raindrop.update()
        check_remove(raindrop, rain, person)

def draw_screen(person, rain):
    win.fill(black)
    pygame.draw.rect(win, (255,0,0), (0, floor, screenwidht, floorwidth))
    person.show()
    for raindrop in rain:
        raindrop.show()
    pygame.display.update()

def get_input():
    run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.KEYDOWN:
            pass
    return run

def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption("Rain simulation")
    run = True
    frame = 0

    person = Person(10,50, 1)

    rain = []
    rain_per_second = 200

    wetnesses = []
    v_list = []

    iterations = 100
    amount = 0
    while run:
        clock.tick()
        frame += 1

        update(rain, person)

        if frame >=60/rain_per_second:
            spawn_raindrop(rain)
            frame = 0

        draw_screen(person, rain)
        #run = get_input()
        if person.x >= screenwidht and amount <= iterations:
            v_list, wetnesses, person = restart(person, v_list, wetnesses, 0.1)
            rain = []
            amount += 1
            if amount > iterations:
                pygame.quit()
                return v_list, wetnesses

if __name__ == '__main__':
    v_list, wetnesses = main()
    plt.plot(v_list, wetnesses)
    plt.show()