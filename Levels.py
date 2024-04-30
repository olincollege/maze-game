import pygame
import sys

from maze import Maze
from view import PygameView
from controller import PygameController

timer = pygame.time.Clock()

maze = Maze()
view = PygameView(maze)
controller = PygameController(maze)

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

Level_3 = [
    pygame.Rect(0, 225, 200, 75),
    pygame.Rect(200, 225, 50, 300),
    pygame.Rect(200, 525, 375, 40),
    pygame.Rect(575, 0, 40, 565),
]


# Set the width and height of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle Test")
image = pygame.image.load("img/test.png")
width = image.get_width()
height = image.get_height()
scale = 3

image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

# Define colors
GREEN = (92, 184, 28)
# GREEN = (76, 172, 28)


# Function to draw the rectangle in the middle of the screen
def draw_rectangle(screen):
    pygame.draw.rect(screen, GREEN, pygame.Rect(300, 175, 150, 500))
    pygame.draw.rect(screen, GREEN, pygame.Rect(300, 175, 500, 100))


# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill(GREEN)
    screen.blit(image, (0, 0))

    # Draw the rectangle in the middle of the screen
    draw_rectangle(screen)
    view.button("img/start_btn.png")

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
