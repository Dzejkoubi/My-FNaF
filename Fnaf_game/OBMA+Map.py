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
Monitor_button_normal_image = pygame.image.load("MonitorButton.png")
Monitor_button_hover_image = pygame.image.load("MonitorButton.png")
Monitor_button_rect = Monitor_button_normal_image.get_rect()
Monitor_button_rect.center = (screen_width - 955, screen_height - 30)

# Load the monitor opening and closing frames
opening_frames = [
    pygame.image.load(f"Frame.O.{i}.png") for i in range(1, 8)
]
closing_frames = [
    pygame.image.load(f"Frame.C.{i}.png") for i in range(1, 7)
]
# Load the monitor image
monitor_image = pygame.image.load("CameraMonitor.png")
monitor_rect = monitor_image.get_rect()
monitor_rect.center = (screen_width // 2, screen_height // 2)  # Adjust the position of the monitor

# Load the camera map image
camera_map_image = pygame.image.load("Cam_Map.png")
camera_map_rect = camera_map_image.get_rect()
camera_map_rect.center = (screen_width // 2, screen_height // 2)

# Initialize the monitor state
monitor_open = False
prev_hovering_button = False
opening_animation_complete = False
closing_animation_complete = True
current_frame = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Check if the mouse is over the button
            hovering_button = Monitor_button_rect.collidepoint(event.pos)

            # Open or close the monitor based on the hover event
            if hovering_button and not prev_hovering_button:
                if not monitor_open and closing_animation_complete:
                    monitor_open = True
                    opening_animation_complete = False
                    current_frame = 0
                elif monitor_open and opening_animation_complete:
                    monitor_open = False
                    closing_animation_complete = False
                    current_frame = 0
                    
            # Update the previous hovering state
            prev_hovering_button = hovering_button 
            
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the office image
    screen.blit(office_image, (0, 0))

    # Draw the monitor if it's open
    if monitor_open:
        if current_frame < len(opening_frames):
            screen.blit(opening_frames[current_frame], (0, 0))
            current_frame += 1
            if current_frame == len(opening_frames):
                opening_animation_complete = True
        else:
            screen.blit(monitor_image, monitor_rect)
            
        if current_frame == len(opening_frames):
            # Move the camera map
            camera_map_rect.center = (screen_width // 1.25, screen_height // 1.4)
            screen.blit(camera_map_image, camera_map_rect)
    else:
        if current_frame < len(closing_frames):
            screen.blit(closing_frames[current_frame], (0, 0))
            current_frame += 1
            if current_frame == len(closing_frames):
                closing_animation_complete = True
        
    # Blit the button image
    if prev_hovering_button:
        screen.blit(Monitor_button_hover_image, Monitor_button_rect)
    else:
        screen.blit(Monitor_button_normal_image, Monitor_button_rect)
    # Update the screen
    pygame.display.flip()
    
    # Limit the frame rate
    clock = pygame.time.Clock()
    clock.tick(200)

# Clean up Pygame
pygame.quit()