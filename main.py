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

screen = pygame.display.set_mode((600, 400))
screen.fill((25, 25, 25))
pygame.display.set_caption("Sierpinski Hexagon")
font = pygame.font.SysFont('Arial', 25)

running = True
start = True

class Dot(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = position
        

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

def calculate_button_render():
    pygame.draw.rect(screen, (25, 25, 25), pygame.Rect(425, 25, 150, 50))
    btn_text = font.render('Calculate', True, (255, 255, 255))
    btn_text_rect = btn_text.get_rect()
    btn_text_rect.center = (500, 50)
    screen.blit(btn_text, btn_text_rect)

def reset_button_render():
    pygame.draw.rect(screen, (25, 25, 25), pygame.Rect(425, 100, 150, 50))
    btn_text = font.render('Reset', True, (255, 255, 255))
    btn_text_rect = btn_text.get_rect()
    btn_text_rect.center = (500, 125)
    screen.blit(btn_text, btn_text_rect)

pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(400, 0, 200, 400))
draw_ngon(6, 150, (200, 200))
calculate_button_render()
reset_button_render()

pressed = False
start = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if (425 < pos[0] < 575) and (25 < pos[1] < 75) and not pressed:
            pressed = True
            start = True

        elif (425 < pos[0] < 575) and (100 < pos[1] < 150) and pressed:
            pressed = False
            start = False
            pygame.draw.rect(screen, (25, 25, 25), pygame.Rect(0, 0, 400, 400))
            draw_ngon(6, 150, (200, 200))

    if start:

        # f(x) = 1.1^(69-x)
        animation_delay = round(pow(1.5, 16-i))


        line_start_pos = start_pos

        rand_point = random.choice(positions)
        if i < 500: draw_line(line_start_pos, rand_point, animation_delay)

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