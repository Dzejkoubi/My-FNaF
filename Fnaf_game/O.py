import pygame
import os

# Set the new working directory
new_directory = "../Fnaf_resources"
os.chdir(new_directory)
pygame.init()

# Set up the game window + fullscreen mode
screen_width = 1920
screen_height = 1080
#pygame.FULLSCREEN
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My FNAF-like Game")

# Load the office
office_image = pygame.image.load("Office.png")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw game elements here
    
    # blit the image at position (0,0)
    screen.blit(office_image, (0, 0))

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock = pygame.time.Clock()
    clock.tick(60)

# Clean up Pygame
pygame.quit()
