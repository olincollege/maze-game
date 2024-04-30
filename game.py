"""
Implement the maze
"""

import pygame

from maze import Maze
from view import PygameView
from view import BUTTON_X
from view import BUTTON_Y
from controller import PygameController
from library import Level_1
from library import Level_2
from library import Level_3

timer = pygame.time.Clock()

maze = Maze()
view = PygameView(maze)
controller = PygameController(maze)

run = True
button_display = True
level = 1
while run:
    view.background_image("img/test.png")
    while button_display:
        mouse_position = controller.mouse_position()
        view.button("img/start_btn.png")
        view.character(mouse_position, timer)
        if controller.click_button(BUTTON_X, BUTTON_Y, "img/start_btn.png", 1):
            button_display = False
            view.background_image("img/test.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # while level < 4:
    # mouse_position = controller.mouse_position()
    # view.background_image("img/test.png")
    # view.character(mouse_position, timer)

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
