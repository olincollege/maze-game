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
HANNI_X_SCALE = 0.8
HANNI_Y_SCALE = 0.8
JUMPSCARE_X_SCALE = 1.2
JUMPSCARE_Y_SCALE = 0.7


class MazeView(ABC):
    """
    Shows the status of the maze board.

    Attributes:
        _board: An instance of Maze representing the status of the maze.
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
    def character(self, mouse_position, timer):
        """
        Implementations of this method should display the character's location.
        """

    @abstractmethod
    def button(self, path):
        """
        Implementations of this method should display a button.
        """

    @abstractmethod
    def background_image(self, path):
        """
        Implementations of this method should display the image at
            the given path as the background.
        """

    @abstractmethod
    def draw_level(self, level):
        """
        Implementations of this method should display the maze of
            the given level.
        """


class PygameView(MazeView):
    """
    Extending MazeView to show the status of the maze board using pygame
        interface.

    Attributes:
        _screen: An instance of pygame display allowing us to set the
            mode for the game.
    """

    def __init__(self, board):
        self._screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Maze Game")

    def character(self, mouse_position, timer):
        """
        Show the player's position.

        Args:
            mouse_position: A tuple representing the player's position
            timer: An instance of pygame clock representing the in game time
        """
        timer.tick(FPS)
        pygame.draw.circle(self._screen, "pink", mouse_position, 10)
        pygame.display.flip()

    def button(self, path):
        """
        Display a button.

        Args:
            path: A string representing the path to the image being used
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

        Args:
            path: A string representing the path to the image being used
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

        Args:
            level: An int representing the current level
        """
        for i, rectangle in enumerate(maps[level]):
            pygame.draw.rect(self._screen, GREEN, rectangle)
            i += 1

    def jumpscare_image(self, choice):
        """
        Display the jumpscare image.

        Args:
            choice: A string representing the randomly chosen ending image
        """
        if choice == "hanni":
            path = "img/Hanni.jpeg"
        else:
            path = "img/jumpscare.jpg"

        image = pygame.image.load(path)
        width = image.get_width()
        height = image.get_height()
        if choice == "hanni":
            x_scale = HANNI_X_SCALE
            y_scale = HANNI_Y_SCALE
        else:
            x_scale = JUMPSCARE_X_SCALE
            y_scale = JUMPSCARE_Y_SCALE
        image = pygame.transform.scale(
            image,
            (int(width * x_scale), int(height * y_scale)),
        )
        self._screen.blit(image, (0, 0))
