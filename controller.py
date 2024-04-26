"""
Maze controller.
"""

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

    # FUNCTIONS TO IMPLEMENT
    # get mouse position
    # get mouse click for start button ya
