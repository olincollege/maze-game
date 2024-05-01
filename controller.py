"""
Maze controller.
"""

from abc import ABC, abstractmethod

import pygame


class MazeController(ABC):
    """
    Allows the player to control the status of the maze.

    Attributes:
        _board: An instance of Maze representing the status of the maze.
    """

    def __init__(self, board):
        """
        Define attributes.
        """
        self._board = board

    @property
    def board(self):
        """
        Returns _board.
        """
        return self._board

    @abstractmethod
    def click_button(self, path, x_position, y_position, scale):
        """
        Implementations of this method should check if a button is
            clicked or not.
        """


class PygameController(MazeController):
    """
    Extending MazeController to control the status of the maze using
        pygame interface.
    """

    def click_button(self, path, x_position, y_position, scale):
        """
        Check if a button is clicked.

        Args:
            path: A string representing the path to the image of the button.
            x_position: An int representing the x position of the top
                left corner of the button.
            y_position: An int representing the y position of the top
                left corner of the button.
            scale: An int representing how much the image is being scaled by.

        Returns:
            A bool representing whether or not the button has been clicked.
        """
        clicked = False
        image = pygame.image.load(path)
        transformed_image = pygame.transform.scale(
            image,
            (
                int(image.get_width() * scale),
                int(image.get_height() * scale),
            ),
        )
        rect = transformed_image.get_rect()
        rect.topleft = (x_position, y_position)

        position = pygame.mouse.get_pos()

        if rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and clicked is False:
                clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False

        return clicked
