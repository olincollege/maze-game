"""
Library of lists to use to make rectangles for the maps.
"""

import pygame

level_1 = [
    pygame.Rect(300, 175, 150, 500),
    pygame.Rect(300, 175, 500, 100),
]

level_1_ending = pygame.Rect(750, 175, 50, 100)

level_2 = [
    pygame.Rect(400, 175, 500, 150),
    pygame.Rect(175, 100, 350, 75),
    pygame.Rect(175, 325, 350, 75),
    pygame.Rect(125, 100, 75, 300),
    pygame.Rect(0, 225, 200, 75),
]

level_2_ending = pygame.Rect(0, 225, 50, 75)

level_3 = [
    pygame.Rect(0, 225, 200, 75),
    pygame.Rect(200, 225, 75, 300),
    pygame.Rect(200, 525, 300, 50),
    pygame.Rect(450, 125, 50, 400),
    pygame.Rect(450, 125, 350, 75),
]

level_3_ending = pygame.Rect(750, 125, 50, 75)

level_4 = [
    pygame.Rect(650, 125, 350, 75),
    pygame.Rect(650, 125, 75, 300),
    pygame.Rect(550, 425, 175, 75),
    pygame.Rect(550, 25, 75, 400),
    pygame.Rect(150, 25, 400, 50),
    pygame.Rect(150, 25, 50, 150),
    pygame.Rect(150, 125, 300, 50),
    pygame.Rect(450, 125, 50, 100),
    pygame.Rect(0, 225, 500, 75),
]

level_4_ending = pygame.Rect(0, 225, 50, 75)

level_5 = [
    pygame.Rect(0, 225, 200, 75),
    pygame.Rect(200, 225, 50, 300),
    pygame.Rect(200, 525, 375, 40),
    pygame.Rect(575, 0, 40, 565),
]

level_5_ending = pygame.Rect(575, 0, 40, 50)

test_level = [
    pygame.Rect(0, 0, 800, 50),
    pygame.Rect(0, 0, 50, 600),
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(750, 0, 50, 600),
    pygame.Rect(0, 300, 300, 50),
    pygame.Rect(300, 300, 50, 150),
    pygame.Rect(300, 400, 250, 50),
    pygame.Rect(500, 100, 50, 350),
    pygame.Rect(200, 100, 350, 50),
    pygame.Rect(200, 0, 50, 150),
]

maps = {1: level_1, 2: level_2, 3: level_3, 4: level_4, 5: level_5}
endings = {
    1: level_1_ending,
    2: level_2_ending,
    3: level_3_ending,
    4: level_4_ending,
    5: level_5_ending,
}
