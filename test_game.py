"""
Unit tests for maze model.
"""

import pytest
from maze import Maze


# Define sets of test cases.
collide_borders_cases = [
    # Test that a mouse position outside of the pathed rectangle returns
    # a collision on level 1
    (1, (-1, -1), True),
    # Test that a mouse position outside of the pathed rectangle returns
    # a collision on level 2
    (2, (-1, -1), True),
    # Test that a mouse position outside of the pathed rectangle returns
    # a collision on level 3
    (3, (-1, -1), True),
    # Test that a mouse position outside of the pathed rectangle returns
    # a collision on level 4
    (4, (-1, -1), True),
    # Test that a mouse position outside of the pathed rectangle returns
    # a collision on level 5
    (5, (-1, -1), True),
    # Test that a mouse position inside of the pathed rectangle will not
    # return a collision for level 1
    (1, (300, 175), False),
    # Test that a mouse position inside of the pathed rectangle will not
    # return a collision for level 2
    (2, (175, 325), False),
    # Test that a mouse position inside of the pathed rectangle will not
    # return a collision for level 3
    (3, (200, 525), False),
    # Test that a mouse position inside of the pathed rectangle will not
    # return a collision for level 4
    (4, (150, 125), False),
    # Test that a mouse position inside of the pathed rectangle will not
    # return a collision for level 5
    (5, (200, 525), False),
]

level_cases = [
    # Test that when on level 1 level 1 is returned
    (1, 1),
    # Test that when on level 2 level 2 is returned
    (2, 2),
    # Test that when on level 3 level 3 is returned
    (3, 3),
    # Test that when on level 4 level 4 is returned
    (4, 4),
    # Test that when on level 5 level 5 is returned
    (5, 5),
]

increase_level_cases = [
    # Test that starting at level 1 will increase to level 2
    (1, 2),
    # Test that starting at level 2 will increase to level 3
    (2, 3),
    # Test that starting at level 3 will increase to level 4
    (3, 4),
    # Test that starting at level 4 will increase to level 5
    (4, 5),
    # Test that starting at level 5 will not increase and stay at level 5
    (5, 5),
]

reset_level_cases = [
    # Test that being at level 1 resets to level 1
    (1, 1),
    # Test that being at level 2 resets to level 1
    (2, 1),
    # Test that being at level 3 resets to level 1
    (3, 1),
    # Test that being at level 4 resets to level 1
    (4, 1),
    # Test that being at level 5 resets to level 1
    (5, 1),
]

check_ending_cases = [
    # Test that a mouse position in the ending rectangle of level 1
    # does not result in a jumpscare
    (1, (750, 175), False),
    # Test that a mouse position in the ending rectangle of level 2
    # does not result in a jumpscare
    (2, (0, 225), False),
    # Test that a mouse position in the ending rectangle of level 3
    # does not result in a jumpscare
    (3, (750, 125), False),
    # Test that a mouse position in the ending rectangle of level 4
    # does not result in a jumpscare
    (4, (0, 225), False),
    # Test that a mouse position in the ending rectangle of level 5
    # does result in a jumpscare
    (5, (575, 0), True),
]


@pytest.mark.parametrize(
    "level,test_position,border_collided", collide_borders_cases
)
def test_collide_borders(level, test_position, border_collided):
    """
    Test that when the players cursor/mouse position is inside or outside
    the path the appropriate measures happen

    Check that given a specified level and a test position the method
    collide_borders() will be able to determine if the mouse position
    is inside or outside the maze pathway

    Args:
        level: An integer that represents what level of the maze is being
            tested
        test_position: A tuple of integers that respresents x and y,
            a position on the screen
        border_collided: A boolean that represents whether or not the
            proposed mouse position is on the maze path or not, true for
            off the path and false for on the path
    """
    maze = Maze()
    maze.set_level(level)

    result = maze.collide_borders(test_position)

    assert result == border_collided


@pytest.mark.parametrize("current_level,correct_level", level_cases)
def test_level(current_level, correct_level):
    """
    Test that the maze class stores the correct level

    Check that given a specified current level the method level() can return
    the correct current level the maze class is holding
    Args:
        current_level: An integer representing a proposed level to set the
            maze class to
        correct_level: An integer that represents the correct level that
            the maze class should hold
    """
    maze = Maze()
    maze.set_level(current_level)

    result = maze.level()

    assert result == correct_level


@pytest.mark.parametrize("current_level,increased_level", increase_level_cases)
def test_increase_level(current_level, increased_level):
    """
    Test that the game can increase levels and progress the game when
    it is neccasary to do so

    Check that given a specified level the increase_level() function can
    correctly iterate to the next level and store it properly in the maze class

    Args:
        current_level: An integer representing a proposed level to set the
            maze class to
        increased_level: An integer that represents the increased level
            after the method is called
    """
    maze = Maze()
    maze.set_level(current_level)
    maze.increase_level()

    assert maze.level() == increased_level


@pytest.mark.parametrize("current_level,level_reseted", reset_level_cases)
def test_reset_level(current_level, level_reseted):
    """
    Test that the game can reset levels and start the game over when
    it is neccasary to do so

    Check that given a specified level the reset_level() function can
    correctly reset to the first level and store it properly in the maze class

    Args:
        current_level: An integer representing a proposed level to set the
            maze class to
        level_reseted: An integer that represents the reset level after
            the method is called
    """
    maze = Maze()
    maze.set_level(current_level)
    maze.reset_level()

    assert maze.level() == level_reseted


@pytest.mark.parametrize("level,test_position,jumpscare", check_ending_cases)
def test_check_ending(level, test_position, jumpscare):
    """
    Test that when the players cursor/mouse position is inside the correct
    finish zone a jumpscare will trigger

    Check that given a specified level and a test position the method
    check_ending() will be able to determine if the mouse position
    should warrant a jumpscare or not and store it properly

    Args:
        level: An integer that represents what level of the maze is being
            tested
        test_position: A tuple of integers that respresents x and y,
            a position on the screen
        jumpscare: A boolean that represents whether or not to trigger
            the jumpscare
    """
    maze = Maze()
    maze.set_level(level)

    maze.check_ending(test_position)

    assert maze.jumpscare() == jumpscare
