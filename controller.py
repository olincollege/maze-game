"""
Maze controller.
"""

import pygame
from abc import ABC, abstractmethod


class MazeController(ABC):
    """
    Allows the player to control the status of the board.
    """

    def __init__(self, board):
        """
        Define attributes.
        """
        self._board = board

    @property
    def board(self):
        """
        Returns _board.
        """
        return self._board

    @abstractmethod
    def mouse_position(self):
        """
        Implementations of this method should get and return the mouse's position.
        """

    @abstractmethod
    def click_button(self, x, y, image):
        """
        Implementations of this method should check if a button is clicked or not.
        """

    # @abstractmethod
    # def quit_game(self):
    #     """
    #     Implementations of this method should allow users to quit the game.
    #     """


class PygameController(MazeController):
    """
    Extending MazeController to control the status of the TicTacToe board using
        pygame interface.
    """

    def mouse_position(self):
        """
        Get the mouse position so that the player can move!!!
        """
        mouse_position = pygame.mouse.get_pos()
        return mouse_position

    def click_button(self, x, y, path, scale):
        """
        Check if a button is clicked.
        """
        clicked = False
        image = pygame.image.load(path)
        transformed_image = pygame.transform.scale(
            image,
            (int(image.get_width() * scale), int(image.get_height() * scale)),
        )
        rect = transformed_image.get_rect()

        position = self.mouse_position()

        if rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and clicked is False:
                clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False

        return clicked

    # FUNCTIONS TO IMPLEMENT
    # get mouse click for start button ya
