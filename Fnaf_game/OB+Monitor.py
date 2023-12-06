import pygame
import os

# Set the new working directory
new_directory = "../Fnaf_resources"
os.chdir(new_directory)
pygame.init()

# Set up the game window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My FNAF-like Game")

# Load the office image
office_image = pygame.image.load("Office.png")

# Load the button images
button_normal_image = pygame.image.load("MonitorButton.png")
button_hover_image = pygame.image.load("MonitorButton.png")
button_rect = button_normal_image.get_rect()
button_rect.center = (screen_width - 955, screen_height - 30)

# Load the monitor image and scale it up
monitor_image = pygame.image.load("CameraMonitor.png")
monitor_rect = monitor_image.get_rect()
monitor_rect.center = (screen_width // 2, screen_height // 2)  # Set the position to the center of the screen

# Initialize the monitor state
monitor_open = False
prev_hovering_button = False

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Check if the mouse is over the button
            hovering_button = button_rect.collidepoint(event.pos)

            # Open or close the monitor based on the hover event
            if hovering_button and not prev_hovering_button:
                monitor_open = not monitor_open

            # Update the previous hovering state
            prev_hovering_button = hovering_button

    # Update game logic here

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw game elements here

    # Blit the office image
    screen.blit(office_image, (0, 0))

    # Draw the monitor if it's open
    if monitor_open:
        screen.blit(monitor_image, monitor_rect)

    # Blit the button image
    if prev_hovering_button:
        screen.blit(button_hover_image, button_rect)
    else:
        screen.blit(button_normal_image, button_rect)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock = pygame.time.Clock()
    clock.tick(60)

# Clean up Pygame
pygame.quit()
