"""
Maze game view.
"""

from abc import ABC, abstractmethod

import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60
GREEN = (92, 184, 28)


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
    def button(self, x, y, image, surface):
        """
        Implementations of this method should display a button.
        """

    @abstractmethod
    def background_image(self, path):
        """
        Implementations of this method should display the image at the given path as the background.
        """

    @abstractmethod
    def draw_level(self, level):
        """
        Implementations of this method should display the maze of the given level.
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
        pygame.display.flip()

    def background_image(self, path):
        """ """
        image = pygame.image.load(path)
        width = image.get_width()
        height = image.get_height()
        scale = 3
        image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self._screen.blit(image, (0, 0))
        pygame.display.flip()

    def draw_level(self, level):
        """ """
        for i in range(len(level)):
            pygame.draw.rect(self._screen, GREEN, level(i))
            i += 1
            pygame.display.flip()

    # display board
    # visuals and stuff
    # make a start button at the beginning
    # render all the collectibles
    # render the mouse character
    # jumpscare that breaks out of game loop and display image
