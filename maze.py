"""
Maze implementation.
"""


class Maze:
    """
    Maze with basic play functionality.

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

    def collectibles_locations(self):
        """
        Get locations of collectibles based on level.
        """

    def collectible_picked_up(self):
        """
        When a collectible is picked up, remove it from the board and add
        points to the player's score. If the correct number of points are
        reached, trigger the jumpscare.
        """

    def get_maze(self):
        """
        Locate the file based on the player's level.
        """

    def __repr__(self):
        """
        Return a string representing the maze.
        """
