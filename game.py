"""
Implement the maze
"""

import random
import pygame

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
button_display = True
while run and not maze.jumpscare():
    view.background_image("img/test.png")
    while run and button_display:
        mouse_position = pygame.mouse.get_pos()
        view.background_image("img/test.png")
        view.button("img/start_btn.png")
        if controller.click_button(
            "img/start_btn.png", START_X, START_Y, START_SCALE
        ):
            button_display = False
            view.background_image("img/test.png")
            pygame.display.flip()

        maze.check_quit_pygame()
        border_collided = False

    while run and not border_collided and not maze.jumpscare():
        button_display = True
        mouse_position = pygame.mouse.get_pos()
        view.background_image("img/test.png")
        view.draw_level(maze.level())
        view.character(mouse_position, timer)

        maze.check_ending()

        maze.check_quit_pygame()
        border_collided = maze.collide_borders()
    maze.reset_level()

if maze.jumpscare():
    ending_screen = True
    ending = maze.random_ending()

    while ending_screen:
        view.jumpscare_image(ending)
        pygame.display.flip()
        maze.check_quit_pygame()

pygame.quit()
