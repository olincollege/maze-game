"""
Maze implementation.
"""

import random
import pygame
from library import endings
from library import maps

MAX_LEVEL = 5


class Maze:
    """
    Maze with basic play functionality.

    Attributes:
        _level: An int representing the player's level.
        _jumpscare: A bool representing whether or not the jumpscare should be
            triggered.
    """

    def __init__(self):
        """
        Create a new maze.
        """
        self._level = 1
        self._jumpscare = False

    def level(self):
        """
        Returns the player's current level.

        Returns:
            An int representing the player's current level.
        """
        return self._level

    def set_level(self, level):
        """
        Sets the private variable level

        Args:
            An integer that represents the new level
        """
        self._level = level

    def jumpscare(self):
        """
        Returns True if the jumpscare has been triggered, otherwise False.

        Returns:
            A bool representing whether or not the jumpscare has been triggered.
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

    def check_ending(self, position):
        """
        Check if the current level has been completed or not.
        Trigger the jumpscare if the final level is completed.
        """
        rect = endings[self._level]
        if rect.collidepoint(position):
            if self._level == MAX_LEVEL:
                self._jumpscare = True
            self.increase_level()

    def collide_borders(self, position):
        """
        Check if the player has gone out of the borders.

        Returns:
            A bool representing whether or not the player has gone out
                of the borders.
        """
        for _, rectangle in enumerate(maps[self._level]):
            rect = rectangle
            if rect.collidepoint(position):
                return False
        return True

    def get_position(self):
        """
        Returns a tuple of integers that represent the position of the mouse
        """
        return pygame.mouse.get_pos()

    def random_ending(self):
        """
        Pick a random ending.

        Returns:
            A string representing the chosen ending.
        """
        choice = random.randint(1, 2)
        if choice == 1:
            ending = "hanni"
        else:
            ending = "jumpscare"

        return ending

    def check_quit_pygame(self):
        """
        Check if pygame window should be closed.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def __repr__(self):
        """
        Return a string with the player location, amount of points, and level.
        """
        return (
            f"The player location is:{pygame.mouse.get_pos()}\n"
            "The amount of points collected is:{self._score}\n"
            "The current level is:{self._level}"
        )
