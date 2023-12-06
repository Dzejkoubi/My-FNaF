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

# Load the camera monitor button images
monitor_button_normal_image = pygame.image.load("MonitorButton.png").convert_alpha()
monitor_button_hover_image = pygame.image.load("MonitorButton.png").convert_alpha()
monitor_button_rect = monitor_button_normal_image.get_rect()
monitor_button_rect.center = (screen_width - 955, screen_height - 30)

# Load the camera buttons images
camera_button_normal_images = [
    pygame.image.load(f"CameraButton{i}.png").convert_alpha() for i in range(1, 12)
]
camera_button_hover_images = [
    pygame.image.load(f"CameraButton{i}.png").convert_alpha() for i in range(1, 12)
]
camera_button_rects = [camera_button_normal_images[i].get_rect() for i in range(11)]
#camera button positions
camera_button_positions = [
    (x, y) for x in range(500, screen_width - 600, 700)
           for y in range(500, screen_height - 600, 700)
]

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
    # Adjust the position of the monitor
monitor_rect.center = (screen_width // 2, screen_height // 2)

# Load the camera map image
camera_map_image = pygame.image.load("Cam_Map.png")
camera_map_rect = camera_map_image.get_rect()
    # Adjust the position of the camera map
camera_map_rect.center = (screen_width // 1.25, screen_height // 1.4) 

# Load the camera map images
# Camera 1A
camera_bimage1 = pygame.image.load(f"CameraButton1.png")
camera_rect1 = camera_bimage1.get_rect()
camera_rect1.center = (screen_width // 1.292, screen_height // 1.79) 
# Camera 1B
camera_bimage2 = pygame.image.load(f"CameraButton2.png")
camera_rect2 = camera_bimage2.get_rect()
camera_rect2.center = (screen_width // 1.311, screen_height // 1.623) 
# Camera 1C
camera_bimage3 = pygame.image.load(f"CameraButton3.png")
camera_rect3 = camera_bimage3.get_rect()
camera_rect3.center = (screen_width // 1.343, screen_height // 1.44) 
# Camera 2A
camera_bimage4 = pygame.image.load(f"CameraButton4.png")
camera_rect4 = camera_bimage4.get_rect()
camera_rect4.center = (screen_width // 1.293, screen_height // 1.234) 
# Camera 2B
camera_bimage5 = pygame.image.load(f"CameraButton5.png")
camera_rect5 = camera_bimage5.get_rect()
camera_rect5.center = (screen_width // 1.293, screen_height // 1.1732) 
# Camera 3
camera_bimage6 = pygame.image.load(f"CameraButton6.png")
camera_rect6 = camera_bimage6.get_rect()
camera_rect6.center = (screen_width // 1.377, screen_height // 1.26) 
# Camer 4A 
camera_bimage7 = pygame.image.load(f"CameraButton7.png")
camera_rect7 = camera_bimage7.get_rect()
camera_rect7.center = (screen_width // 1.1965, screen_height // 1.234) 
# Camera 4B
camera_bimage8 = pygame.image.load(f"CameraButton8.png")
camera_rect8 = camera_bimage8.get_rect()
camera_rect8.center = (screen_width // 1.1965, screen_height // 1.1732) 
# Camera 5
camera_bimage9 = pygame.image.load(f"CameraButton9.png")
camera_rect9 = camera_bimage9.get_rect()
camera_rect9.center = (screen_width // 1.4232, screen_height // 1.558) 
# Camera 6
camera_bimage10= pygame.image.load(f"CameraButton10.png")
camera_rect10 = camera_bimage10.get_rect()
camera_rect10.center = (screen_width // 1.1225, screen_height // 1.285)
# Camera 7
camera_bimage11= pygame.image.load(f"CameraButton11.png")
camera_rect11 = camera_bimage11.get_rect()
camera_rect11.center = (screen_width // 1.116, screen_height // 1.555)

# Initialize the monitor state
monitor_open = False
prev_hovering_monitor_button = False
prev_hovering_camera_buttons = [False] * len(camera_button_rects)
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
            mouse_pos = pygame.mouse.get_pos()

            # Check if the mouse is over the monitor button
            hovering_monitor_button = monitor_button_rect.collidepoint(mouse_pos)

            # Check if the mouse is over any of the camera buttons
            hovering_camera_buttons = [camera_button_rect.collidepoint(mouse_pos) for camera_button_rect in camera_button_rects]

            # Open or close the monitor based on the hover event
            if hovering_monitor_button and not prev_hovering_monitor_button:
                if not monitor_open and closing_animation_complete:
                    monitor_open = True
                    opening_animation_complete = False
                    current_frame = 0
                elif monitor_open and opening_animation_complete:
                    monitor_open = False
                    closing_animation_complete = False
                    current_frame = 0

            # Update the previous hovering states
            prev_hovering_monitor_button = hovering_monitor_button
            prev_hovering_camera_button = hovering_camera_buttons

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
            screen.blit(camera_map_image, camera_map_rect)
            screen.blit(monitor_button_hover_image, monitor_button_rect)
            screen.blit(camera_bimage1,camera_rect1)
            screen.blit(camera_bimage2,camera_rect2)
            screen.blit(camera_bimage3,camera_rect3)
            screen.blit(camera_bimage4,camera_rect4)
            screen.blit(camera_bimage5,camera_rect5)
            screen.blit(camera_bimage6,camera_rect6)
            screen.blit(camera_bimage7,camera_rect7)
            screen.blit(camera_bimage8,camera_rect8)
            screen.blit(camera_bimage9,camera_rect9)
            screen.blit(camera_bimage10,camera_rect10)
            screen.blit(camera_bimage11,camera_rect11)
    else:
        if current_frame < len(closing_frames):
            screen.blit(closing_frames[current_frame], (0, 0))
            current_frame += 1
            if current_frame == len(closing_frames):
                closing_animation_complete = True

    # Blit the monitor button
    if prev_hovering_monitor_button:
        screen.blit(monitor_button_hover_image, monitor_button_rect)
    else:
        screen.blit(monitor_button_normal_image, monitor_button_rect)      

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock = pygame.time.Clock()
    clock.tick(200)

# Clean up Pygame
pygame.quit()
