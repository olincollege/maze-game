"""
Maze game view.
"""
import pygame
import csv
from abc import ABC, abstractmethod
from maze import get_maze


class MazeView(ABC):
    """
    Shows the status of the maze board.
    """

    def __init__(self, board):
        """
        Define the attributes of the class.
        """
        self._board = board

    @property
    def board(self):
        """
        Returns _board.
        """
        return self._board

    @abstractmethod
    def draw(self):
        """
        Implementations of this method should display a copy of the board.
        """


class PygameView(MazeView):
    """
    Extending MazeView to show the status of the maze board using pygame
        interface.
    """
    def __init__(self, level=1):
        pygame.init()
        self._level = level
        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Maze Game')


    def draw(self):
        """
        Show the current state of the maze.
        """
        world_data = []
        for row in range(19):
            r = [-1] * 19
            world_data.append(r)
        # load in level data
        with open(f'level_{level}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)


