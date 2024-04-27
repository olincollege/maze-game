"""
Maze game view.
"""

import pygame
from abc import ABC, abstractmethod

WIDTH = 800
HEIGHT = 600
FPS = 60


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
        Returns
            _self._fps = 60 board.
        """
        return self._board

    @abstractmethod
    def character(self, mouse_position, timer):
        """
        Implementations of this method should display the character's location.
        """

    @abstractmethod
    def button(self, x, y, image):
        """
        Implementations of this method should display a button.
        """


class PygameView(MazeView):
    """
    Extending MazeView to show the status of the maze board using pygame
        interface.
    """

    def __init__(self, board):
        pygame.init()
        self._level = 1
        self._screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Maze Game")

    def character(self, mouse_position, timer):
        """
        Show the player's position.
        """
        self._screen.fill("white")
        timer.tick(FPS)
        pygame.draw.circle(self._screen, "pink", mouse_position, 10)
        pygame.display.flip()

    def button(self, x, y, image, surface):
        """
        Display a button.
        """
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)

        surface.blit(self.image, (self.rect.x, self.rect.y))

    # display board
    # visuals and stuff
    # make a start button at the beginning
    # render all the collectibles
    # render the mouse character
    # jumpscare that breaks out of game loop and display image
