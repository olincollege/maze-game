"""
Maze implementation.
"""

from library import level1_collectibles
from library import level2_collectibles
from library import level3_collectibles


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
        if self._level == 2:
            self._collectibles = level2_collectibles
        self._collectibles = level3_collectibles

    def check_collectible(self, x_location, y_location):
        """
        When a collectible is picked up, remove it from the board and add
        points to the player's score.

        Args:
            x_location: An integer that represents the x index at which the
            player is located
            y_location: An integer that represents the y index at which the
            player is located
        """
        if (x_location, y_location) in self._collectibles:
            self._collectibles[(x_location, y_location)] = True
            self._score += 1

    def get_maze(self):
        """
        Locate the file based on the player's level.
        """
        if self._level == 1:
            return "Levels/level_1.csv"
        if self._level == 2:
            return "Levels/level_2.csv"
        return "Levels/level_3.csv"

    def __repr__(self):
        """
        Returns a string with the player location, amount of points, and level
        """
        location = ()
        return f"The player location is:{location}\nThe amount of points collected is:{self._score}\nThe current level is:{self._level}"
