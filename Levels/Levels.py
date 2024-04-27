import pygame
import sys
from PIL import Image

# Initialize Pygame
pygame.init()

Level_1 = [
    pygame.Rect(300, 175, 150, 500),
    pygame.Rect(300, 175, 500, 100),
]

Level_2 = [
    pygame.Rect(400, 175, 500, 150),
    pygame.Rect(175, 100, 350, 75),
    pygame.Rect(175, 325, 350, 75),
    pygame.Rect(125, 100, 75, 300),
    pygame.Rect(0, 225, 200, 75),
]


# Set the width and height of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle Test")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# Function to draw the rectangle in the middle of the screen
def draw_rectangle(screen):
    rect = pygame.Rect(300, 175, 150, 500)
    # pygame.draw.rect(screen, BLACK, rect)
    pygame.draw.rect(screen, BLACK, pygame.Rect(400, 175, 500, 150))
    pygame.draw.rect(screen, BLACK, pygame.Rect(175, 100, 350, 75))
    pygame.draw.rect(screen, BLACK, pygame.Rect(175, 325, 350, 75))
    pygame.draw.rect(screen, BLACK, pygame.Rect(125, 100, 75, 300))
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 225, 200, 75))


# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the rectangle in the middle of the screen
    draw_rectangle(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
