"""
Maze game view.
"""

from abc import ABC, abstractmethod

import pygame

from library import maps

WIDTH = 800
HEIGHT = 600
FPS = 60
GREEN = (92, 184, 28)
START_X = 303
START_Y = 500
START_SCALE = 0.55
JUMPSCARE_X_SCALE = 1
JUMPSCARE_Y_SCALE = 0.6


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
    def button(self, path, scale):
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

    def button(self, path):
        """
        Display a button.
        """
        image = pygame.image.load(path)
        transformed_image = pygame.transform.scale(
            image,
            (
                int(image.get_width() * START_SCALE),
                int(image.get_height() * START_SCALE),
            ),
        )
        self._screen.blit(transformed_image, (START_X, START_Y))
        pygame.display.flip()

    def background_image(self, path):
        """
        Display the background image.
        """
        image = pygame.image.load(path)
        width = image.get_width()
        height = image.get_height()
        scale = 3
        image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self._screen.blit(image, (0, 0))

    def draw_level(self, level):
        """
        Display the corresponding maze for the level.
        """
        for i, rectangle in enumerate(maps[level]):
            pygame.draw.rect(self._screen, GREEN, rectangle)
            i += 1

    def jumpscare_image(self, path):
        """
        Display the jumpscare image.
        """
        image = pygame.image.load(path)
        width = image.get_width()
        height = image.get_height()
        image = pygame.transform.scale(
            image,
            (int(width * JUMPSCARE_X_SCALE), int(height * JUMPSCARE_Y_SCALE)),
        )
        self._screen.blit(image, (0, 0))
