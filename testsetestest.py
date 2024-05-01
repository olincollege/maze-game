import pygame

from library import level_1, level_2, level_3
from maze import Maze
from view import PygameView
from view import START_X
from view import START_Y
from view import START_SCALE
from controller import PygameController

timer = pygame.time.Clock()

maze = Maze()
view = PygameView(maze)
controller = PygameController(maze)

run = True
while run and not maze.jumpscare():
    view.background_image("img/test.png")
    while run:
        mouse_position = pygame.mouse.get_pos()
        view.background_image("img/test.png")
        view.background_image("img/test.png")
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        border_collided = False

    while run:
        mouse_position = pygame.mouse.get_pos()
        view.background_image("img/test.png")
        view.draw_level(level_1)
        view.character(mouse_position, timer)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        border_collided = maze.collide_borders()
