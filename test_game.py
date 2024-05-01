"""
Unit tests for maze model.
"""

import pytest
import pygame

from library import level_1, level_2, level_3
from view import PygameView
from maze import Maze
from controller import PygameController

# Define sets of test cases.
collide_borders_cases = [(1, (200, 200), False), (1, (300, 500), False)]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize(
    "level,test_position,border_collided", collide_borders_cases
)
def test_collide_borders(level, test_position, border_collided):
    """
    Test that the game goes back to the start screen
    """
    from maze import Maze
    from library import maps

    for _, rectangle in enumerate(maps[level]):
        rect = rectangle
        if rect.collidepoint(test_position):
            result = False
        else:
            result = True

    assert result == border_collided
