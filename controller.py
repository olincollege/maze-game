"""
Maze controller.
"""

from abc import ABC, abstractmethod
from maze import Maze

import pygame


class MazeController(ABC):
    """
    Allows the player to control the status of the board.
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
    def click_button(self, path, x, y, scale):
        """
        Implementations of this method should check if a button is clicked or not.
        """


class PygameController(MazeController):
    """
    Extending MazeController to control the status of the TicTacToe board using
        pygame interface.
    """

    def click_button(self, path, x, y, scale):
        """
        Check if a button is clicked.
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
        rect.topleft = (x, y)

        position = pygame.mouse.get_pos()

        if rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and clicked is False:
                clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False

        return clicked
