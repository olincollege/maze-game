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
        _level: An int representing the player's level.
        _jumpscare: A bool representing whether or not the jumpscare should be
            triggered.
        _touching_wall: A bool representing whether or not the player is
            touching the wall.
        _finish_level: A bool representing whether or not the player has finished
            the current level.
        _collectibles: A dictionary with a tuple as the key representing the
            location of each collectible mapping to a bool representing whether
            or not the collectible has been picked up.
    """

    def __init__(self):
        """
        Create a new, empty maze.
        """
        self._score = 0
        self._level = 1
        self._jumpscare = False
        self._touching_wall = False
        self._finish_level = False
        self._collectibles = {}

    def collectibles_locations(self):
        """
        Set collectibles based on level.
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
            self._collectibles[(x_location, y_location)] = False
            self._score += 1

            # Somehow stop showing the image after this ish

    def get_maze(self):
        """
        Locate the file based on the player's level.

        Returns:
            A string representing the path to the csv representing the level
                map.
        """
        if self._level == 1:
            return "Levels/level_1.csv"
        if self._level == 2:
            return "Levels/level_2.csv"
        return "Levels/level_3.csv"

    def __repr__(self):
        """
        Returns a string with the player location, amount of points, and level.
        """
        location = ()
        return (f"The player location is:{location}\n
                The amount of points collected is:{self._score}\n
                The current level is:{self._level}")

    # we are going to have to call get mouse position to check if in boundaries
    # hella pygame
