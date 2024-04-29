"""
Maze implementation.
"""

import pygame


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
        return (
            f"The player location is:{self.get_position()}\n"
            "The amount of points collected is:{self._score}\n"
            "The current level is:{self._level}"
        )

    def get_position(self):
        """
        Returns a tuple of the current position of the player
        """
        x, y = pygame.mouse.get_pos()
        pos = (x, y)
        return pos

    # we are going to have to call get mouse position to check if in boundaries
    # hella pygame
