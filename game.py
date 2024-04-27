import pygame
from maze import Maze
from view import PygameView
from controller import PygameController

timer = pygame.time.Clock()

maze = Maze()
controller = PygameController(maze)
view = PygameView(maze)

run = True
while run:
    mouse_position = controller.move()
    view.draw(mouse_position, timer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
