import math
from turtle import position
import pygame
import random
import time

pygame.init()

main_dot_size = (5, 5)
dot_size = (2, 2)
main_dots = list()
dots = list()
positions = list()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 400))
screen.fill((25, 25, 25))
pygame.display.set_caption("Sierpinski Hexagon")

running = True
start = True

class Dot(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = position
        
# Make the hexagon (index --> num)

# positions.extend([(133, 100), (266, 100), (66, 200), (336, 200), (133, 300), (266, 300)])
# main_dots.append([pygame.sprite.GroupSingle(Dot((133, 100), main_dot_size)), (133, 100)]) # 0 --> 1
# main_dots.append([pygame.sprite.GroupSingle(Dot((266, 100), main_dot_size)), (266, 100)]) # 1 --> 2

# main_dots.append([pygame.sprite.GroupSingle(Dot((66, 200), main_dot_size)), (66, 200)])  # 2 --> 3
# main_dots.append([pygame.sprite.GroupSingle(Dot((336, 200), main_dot_size)), (336, 200)]) # 3 --> 4

# main_dots.append([pygame.sprite.GroupSingle(Dot((133, 300), main_dot_size)), (133, 300)]) # 4 --> 5
# main_dots.append([pygame.sprite.GroupSingle(Dot((266, 300), main_dot_size)), (266, 300)]) # 5 --> 6

dot_num = 5000
i = 0

clock = pygame.time.Clock()

for dot in main_dots:
    dot[0].draw(screen)

start_pos = [222, 300]

def draw_line(s_p, e_p, d):
    pygame.draw.line(screen, (255, 0, 0), s_p, e_p, 1)

    pygame.display.update()
    pygame.time.delay(d)




def erase_line(s_p, e_p, d, dt):
    pygame.display.update()
    pygame.time.delay(d)

    pygame.draw.line(screen, (25, 25, 25), s_p, e_p, 1)
    dt.draw(screen)

    pygame.display.update()
    pygame.time.delay(d)

def draw_ngon(n, radius, p):
    pi2 = 2 * 3.14

    for i in range(0, n):

        x = math.cos(i / n * pi2) * radius + p[0]
        y = math.sin(i / n * pi2) * radius + p[1]
        positions.append((x, y))
        dot = pygame.sprite.GroupSingle(Dot((x, y), main_dot_size))
        dot.draw(screen)

draw_ngon(6, 150, (200, 200))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if start:

        # f(x) = 1.1^(69-x)
        animation_delay = round(pow(1.5, 16-i))


        line_start_pos = start_pos

        rand_point = random.choice(positions)
        if animation_delay: draw_line(line_start_pos, rand_point, animation_delay)

        # x = (((1/3) * X1) + ((2/3) * X2))
        # y = (((1/3) * Y1) + ((2/3) * Y2))
        

        x = ((1/3) * start_pos[0]) + ((2/3) * rand_point[0])
        y = ((1/3) * start_pos[1]) + ((2/3) * rand_point[1])

        start_pos = [x, y]

        new_dot = pygame.sprite.GroupSingle(Dot((x, y), dot_size))
        new_dot.draw(screen)
        dots.append(new_dot)

        if i < 500: erase_line(line_start_pos, rand_point, animation_delay, new_dot)

        i += 1

        if i == dot_num:
            start = False
    

    pygame.display.update()
    clock.tick(250)