import pygame
import os

# Set the new working directory
new_directory = "D:\Documents\mé dokumenty\Štola\Programování\Fnaf\Fnaf_resources"
os.chdir(new_directory)
pygame.init()

# Set up the game window + fullscreen mode
screen_width = 1920
screen_height = 1080
#pygame.FULLSCREEN
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My FNAF-like Game")

# Load the Office
office_image = pygame.image.load("Office.png")
# Load the MonitorButton
button_image = pygame.image.load("MonitorButton.png")
button_rect = button_image.get_rect()
button_rect.center = (screen_width - 955,  screen_height - 30)

# Define the camera monitor state
camera_monitor_open = False

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # toggle camera monitor
                camera_monitor_open = not camera_monitor_open

    # Update game logic here

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw game elements here
    
    # blit the image at position (0,0)
    screen.blit(office_image, (0, 0))

    # Draw the monitor button
    screen.blit(button_image, button_rect)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock = pygame.time.Clock()
    clock.tick(60)

# Clean up Pygame
pygame.quit()
