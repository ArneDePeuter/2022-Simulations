import pygame
import random
# screen setup
screen_width = 1000
screen_height = 1000
floor = 800

class Ball:
    def __init__(self,x,  y, vy, ay, down, radius):
        self.x = x
        self.y = y
        self.vy = vy
        self.ay = ay
        self.down = down
        self.radius = radius

    def move_ball(self, y, vy, ay, down, radius):
        #moveset
        if y >= floor-radius:
            self.down = False
            self.vy *= 0.8

        elif vy <=0:
            self.down = True

        #buffer/doesnt bouncy infinite
        if self.vy <= 1.5 and y>= floor-radius:
            self.ay = 0
            self.vy = 0

        #move
        if self.down:
            self.vy += self.ay
            self.y += self.vy
        else:
            self.vy -= self.ay
            self.y -= self.vy


def draw_function(win, ball):
    win.fill((0, 0, 0))
    pygame.draw.circle(win, (255,0,0), (ball.x, ball.y), ball.radius)
    pygame.draw.rect(win, (255,255,255), (0,floor, screen_width, 200))
    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()
    ball = Ball(500, 50, 1, 0.3, True, 50)
    run = True

    while run:
        clock.tick(60)

        ball.move_ball(ball.y, ball.vy, ball.ay, ball.down, ball.radius)
        draw_function(win, ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gauss')
main(win)
