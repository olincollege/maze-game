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
    pygame.Rect(200, 225, 50, 300),
    pygame.Rect(200, 525, 375, 40),
    pygame.Rect(575, 0, 40, 565),
]

level_3_ending = pygame.Rect(575, 0, 40, 50)

maps = {1: level_1, 2: level_2, 3: level_3}
endings = {1: level_1_ending, 2: level_2_ending, 3: level_3_ending}
