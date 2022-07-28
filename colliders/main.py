#init
import pygame
pygame.init()
click = pygame.mixer.Sound('mixkit-hard-typewriter-click-1119.wav')
font = pygame.font.SysFont('Segoe UI', 35)

#global vars
screen_width = 1920
screen_height = 1000
fps = 60
floor = 50

#werken met pi
aantalpi = 2
m1 = 10
m2 = m1 * 10**((aantalpi-1)*2)

#werken met massas
#m1 = 10
#m2 = 100

v1 = 0
v2 = -5

class Blok:
    def __init__(self, x, m, v, y):
        self.x = x
        self.y = y
        self.width = self.y
        self.m = m
        self.v = v

def check_bounce(block1, block2, collisions):
    if block1.x+block1.width >= block2.x:
        v1 = (( (block1.m-block2.m)/(block1.m+block2.m) )*block1.v)   +  (((2*block2.m)/(block1.m+block2.m))        *block2.v)
        v2 = (( (2*block1.m)/(block1.m+block2.m)        )*block1.v)   +  (((block2.m-block1.m)/(block1.m+block2.m)) *block2.v)
        block1.v = v1
        block2.v = v2
        collisions += 1
        pygame.mixer.Sound.play(click)
    return collisions

def hit_wall(block1,collisions):
    if block1.x <= 0:
        block1.v *= -1
        collisions += 1
        pygame.mixer.Sound.play(click)
    return collisions

def update(block1, block2, collisions):
    collisions = check_bounce(block1, block2, collisions)
    collisions = hit_wall(block1, collisions)
    block1.x += block1.v
    block2.x += block2.v
    return collisions

def draw_function(win,blocks,collisions):
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255,125,125), (0, screen_height-floor, screen_width, floor))
    for block in blocks:
        pygame.draw.rect(win, (255,255,255), (block.x, screen_height-block.y-floor, block.width, block.width))
    message = font.render(f'Collisions = {collisions}', True, (0,255,255))
    win.blit(message, (1920 - 15*len('Collisions = ' + str(collisions)), 0))
    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()

    block1 = Blok(200, m1, v1, 100)
    block2 = Blok(800, m2, v2, 200)
    blocks = [block1, block2]
    collisions = 0

    run = True
    while run:
        clock.tick(fps)

        collisions = update(block1, block2, collisions)
        draw_function(win, blocks,collisions)

        # using physical inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('collision')
main(win)
