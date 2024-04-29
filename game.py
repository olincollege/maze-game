"""
Implement the maze
"""

import pygame
import matplotlib.pyplot as plt

from maze import Maze
from view import PygameView
from controller import PygameController
from library import Level_1
from library import Level_2
from library import Level_3

timer = pygame.time.Clock()
button = plt.imread("img/start_btn.png")

maze = Maze()
view = PygameView(maze)
controller = PygameController(maze)

run = True
start = False
while run:
    mouse_position = controller.mouse_position()
    view.character(mouse_position, timer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
