"""
Maze implementation.
"""

import pygame
from library import endings
from library import maps

MAX_LEVEL = 3


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

    def level(self):
        """
        Returns the player's current level.
        """
        return self._level

    def jumpscare(self):
        """
        Returns True if the jumpscare has been triggered, otherwise False.
        """
        return self._jumpscare

    def increase_level(self):
        """
        Increase the level, if possible.
        """
        increased_level = self._level + 1
        if increased_level > MAX_LEVEL:
            self._level = MAX_LEVEL
        else:
            self._level = increased_level

    def reset_level(self):
        """
        Go back to level 1.
        """
        self._level = 1

    def check_ending(self):
        """
        Check if the current level has been completed or not.
        """
        rect = endings[self._level]
        position = pygame.mouse.get_pos()
        if rect.collidepoint(position):
            if self._level == MAX_LEVEL:
                self._jumpscare = True
            self.increase_level()

    def collide_borders(self):
        """
        Check if the player has gone out of the borders.
        """
        position = pygame.mouse.get_pos()
        for _, rectangle in enumerate(maps[self._level]):
            rect = rectangle
            if rect.collidepoint(position):
                return False
        return True

    def __repr__(self):
        """
        Returns a string with the player location, amount of points, and level.
        """
        return (
            f"The player location is:{pygame.mouse.get_pos()}\n"
            "The amount of points collected is:{self._score}\n"
            "The current level is:{self._level}"
        )
