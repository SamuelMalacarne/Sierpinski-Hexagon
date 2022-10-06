import pygame
import random
import time

pygame.init()

main_dot_size = (5, 5)
dot_size = (2, 2)
main_dots = list()
dots = list()
positions = list()

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

positions.extend([(133, 100), (266, 100), (66, 200), (336, 200), (133, 300), (266, 300)])
main_dots.append([pygame.sprite.GroupSingle(Dot((133, 100), main_dot_size)), (133, 100)]) # 0 --> 1
main_dots.append([pygame.sprite.GroupSingle(Dot((266, 100), main_dot_size)), (266, 100)]) # 1 --> 2

main_dots.append([pygame.sprite.GroupSingle(Dot((66, 200), main_dot_size)), (66, 200)])  # 2 --> 3
main_dots.append([pygame.sprite.GroupSingle(Dot((336, 200), main_dot_size)), (336, 200)]) # 3 --> 4

main_dots.append([pygame.sprite.GroupSingle(Dot((133, 300), main_dot_size)), (133, 300)]) # 4 --> 5
main_dots.append([pygame.sprite.GroupSingle(Dot((266, 300), main_dot_size)), (266, 300)]) # 5 --> 6

dot_num = 10000

clock = pygame.time.Clock()

while running:
    clock.tick(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for dot in main_dots:
        dot[0].draw(screen)

    if start:

        start_pos = [222, 300]

        for i in range(dot_num):
            rand_point = random.choice(positions)

            # x = (((1/3) * X1) + ((2/3) * X2))
            # y = (((1/3) * Y1) + ((2/3) * Y2))

            x = ((1/3) * start_pos[0]) + ((2/3) * rand_point[0])
            y = ((1/3) * start_pos[1]) + ((2/3) * rand_point[1])

            dots.append(pygame.sprite.GroupSingle(Dot((x, y), dot_size)))

            start_pos = [x, y]

        start = False

    for dot in dots:
        dot.draw(screen)
    

    pygame.display.update()