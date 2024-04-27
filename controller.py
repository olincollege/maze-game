"""
Maze controller.
"""

import pygame
from abc import ABC, abstractmethod


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
    def move(self):
        """
        Implementations of this method should allow players to control the board.
        """


class PygameController(MazeController):
    """
    Extending MazeController to control the status of the TicTacToe board using
        pygame interface.
    """

    def move(self):
        """
        Get the mouse position so that the player can move!!!
        """
        mouse_position = pygame.mouse.get_pos()
        return mouse_position

    # FUNCTIONS TO IMPLEMENT
    # get mouse click for start button ya
