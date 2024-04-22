"""
Maze game view.
"""

from abc import ABC, abstractmethod


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

    def draw(self):
        """
        Show the current state of the maze.
        """
