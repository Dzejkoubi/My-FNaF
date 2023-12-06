import pygame
import os

# Set the new working directory
new_directory = "../Fnaf_resources"
os.chdir(new_directory)
pygame.init()

# Define screen dimensions
screen_width = 1300
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FNAF-like Game")

# Load your office image (replace 'office_image.png' with your file path)
office_image = pygame.image.load("oOffice.png")

# Define the camera's initial position
camera_x = 0
camera_y = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle mouse movement to control camera view
    mouse_x, mouse_y = pygame.mouse.get_pos()
    camera_x += (mouse_x - screen_width // 2) / 10  # Adjust the camera speed as needed
    camera_y += (mouse_y - screen_height // 2) / 10

    # Keep the camera within bounds
    camera_x = max(0, min(camera_x, office_image.get_width() - screen_width))
    camera_y = max(0, min(camera_y, office_image.get_height() - screen_height))

    # Update the screen with the portion of the office image visible through the camera
    screen.blit(office_image, (-camera_x, -camera_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
