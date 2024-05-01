import pytest
import pygame

from library import level_1, level_2, level_3
from view import PygameView
from maze import Maze
from controller import PygameController


collide_borders_level1_tests = [((200, 200), False), ((300, 500), False)]


@pytest.mark.parametrize(
    "test_position", "border_collided", collide_borders_level1_tests
)
def test_collide_borders(test_position, border_collided):
    """
    Test the level borders for level 1
    """
    # maze = Maze()
    # view = PygameView(maze)

    timer = pygame.time.Clock()

    maze = Maze()
    view = PygameView(maze)
    controller = PygameController(maze)

    run = True
    while run and not maze.jumpscare():
        view.background_image("img/test.png")
        while run:
            mouse_position = pygame.mouse.get_pos()
            view.background_image("img/test.png")
            view.background_image("img/test.png")
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            border_collided = False

        while run:
            mouse_position = pygame.mouse.get_pos()
            view.background_image("img/test.png")
            view.draw_level(level_1)
            view.character(mouse_position, timer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            border_collided = maze.collide_borders()
    pygame.quit()

    pygame.mouse.set_pos(test_position)
    result = maze.collide_borders()

    assert result == border_collided
