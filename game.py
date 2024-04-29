import pygame
import matplotlib.pyplot as plt

from maze import Maze
from view import PygameView
from controller import PygameController
from Levels import Level_1
from Levels import Level_2
from Levels import Level_3

timer = pygame.time.Clock()
button = plt.imread("img/start_btn.png")

maze = Maze()
controller = PygameController(maze)
view = PygameView(maze)

run = True
while run:
    mouse_position = controller.mouse_position()
    view.character(mouse_position, timer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
