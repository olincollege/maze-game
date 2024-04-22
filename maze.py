"""
Maze implementation.
"""

from library import level1_collectibles


class Maze:
    """
    Maze with basic play functionality.

    Attributes:
        _score: An int representing the player's score.
    """

    def __init__(self, level):
        """
        Create a new, empty maze.
        """
        self._score = 0
        self._level = level
        self._jumpscare = False
        self._touching_wall = False
        self._finish_level = False
        self._collectibles = {}

    def collectibles_locations(self):
        """
        Get locations of collectibles based on level.
        """
        if self._level == 1:
            self._collectibles = level1_collectibles

    def check_collectible(self, x_location, y_location):
        """
        When a collectible is picked up, remove it from the board and add
        points to the player's score.
        """
        if (x_location, y_location) in self._collectibles:
            self._collectibles[(x_location, y_location)] = True
            self._score += 1

    def get_maze(self):
        """
        Locate the file based on the player's level.
        """

    def __repr__(self):
        """
        Return a string representing the maze.
        """
