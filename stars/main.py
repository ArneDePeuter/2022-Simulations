import pygame
import random
import math
# screen setup
screen_width = 1000
screen_height = 1000

class Ship:
    def __init__(self, speed, startposx, startposy):
        self.screenx = pygame.mouse.get_pos()[0]
        self.screeny = pygame.mouse.get_pos()[1]

        self.screenspeed = speed

    def updatepos(self):
        self.screenx = pygame.mouse.get_pos()[0]
        self.screeny = pygame.mouse.get_pos()[1]


def draw_function(win, stars, ship):
    # background
    win.fill((0, 0, 0))
    for star in stars:
        starx, stary, starz = star
        pygame.draw.circle(win, (255,255,255), (starx,stary),starz)
    pygame.draw.circle(win, (255,155,125), (ship.screenx, ship.screeny), ship.screenspeed)

    pygame.display.update()

def move_stars(stars, ship):
    speed = 1/(ship.screenspeed)*10
    for i,star in enumerate(stars):
        starx, stary, starz = star

        ox = ship.screenx
        oy = ship.screeny

        if ox>0 and starx>0 and stary>0 and oy>0:
            if starx < ox:
                starx -= speed*(ox/starx)
            else:
                starx += speed*(starx/ox)

            if stary < oy:
                stary -= speed*(oy/stary)
            else:
                stary += speed*(stary/oy)

            starz += 0.01+speed/20

        if starx >screen_width or starx<=0 or stary>screen_height or stary<=0:
            starx = random.randint(0 , screen_width)
            stary = random.randint(0,screen_height)
            starz = 1
            stars[i] = starx, stary, starz
        else:
            stars[i] = starx, stary, starz
    return stars

def get_stars(aantal):
    stars = []
    for i in range(aantal):
        starx = random.randint(0, screen_width)
        stary = random.randint(0, screen_height)
        starz = 1
        stars.append((starx,stary,starz))
    return stars

def main(win):
    clock = pygame.time.Clock()
    stars = get_stars(1000)
    ship = Ship(10, 0, 0)
    mapcounter = 0

    run = True
    while run:
        clock.tick(60)
        mapcounter += 1

        ship.updatepos()

        draw_function(win, stars, ship)
        stars = move_stars(stars, ship)

        # using physical inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            ship.screenspeed += 2
        elif keys[pygame.K_LEFT]:
            ship.screenspeed -= 2
        if ship.screenspeed <2:
            ship.screenspeed += 2
        elif ship.screenspeed >= 20:
            ship.screenspeed -= 2


win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Stars')
main(win)
