# Find/use mouse position in Pygame

import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])

run = True
while run:
    screen.fill("white")
    timer.tick(fps)
    mouse_position = pygame.mouse.get_pos()
    pygame.draw.circle(screen, "pink", mouse_position, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
