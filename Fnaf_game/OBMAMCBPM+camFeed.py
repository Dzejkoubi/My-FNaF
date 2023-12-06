import pygame
import os

# Set the new working directory
new_directory = "D:\Documents\mé dokumenty\Štola\Programování\Fnaf\Fnaf_resources"
os.chdir(new_directory)
pygame.init()

# Define screen dimensions
screen_width = 1920
screen_height = 1080
#screen_width = 1300
#screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FNAF-like Game")

# Load your office image
office_image = pygame.image.load("oOffice.png")

# Load the camera monitor button images
monitor_button_normal_image = pygame.image.load("MonitorButton.png").convert_alpha()
monitor_button_hover_image = pygame.image.load("MonitorButton.png").convert_alpha()
monitor_button_rect = monitor_button_normal_image.get_rect()
monitor_button_rect.center = (screen_width - 955, screen_height - 30)

# Load the camera buttons images and define their positions
camera_monitor_surface = pygame.Surface((1920, 1080))
# Create camera buttons           Original picture                                                   Pressed picture                                                                               With-X                                   Height-Y   Size of picture                                                                
camera_buttons_data = [
    {"normal": pygame.image.load("CameraButton1.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP1.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.292, camera_monitor_surface.get_height() // 1.79, 63, 41)},
    {"normal": pygame.image.load("CameraButton2.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP2.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.311, camera_monitor_surface.get_height() // 1.623, 63, 40)},
    {"normal": pygame.image.load("CameraButton3.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP3.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.343, camera_monitor_surface.get_height() // 1.44, 60, 40)},
    {"normal": pygame.image.load("CameraButton4.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP4.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.293, camera_monitor_surface.get_height() // 1.234, 63, 41)},
    {"normal": pygame.image.load("CameraButton5.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP5.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.293, camera_monitor_surface.get_height() // 1.1732, 62, 40)},
    {"normal": pygame.image.load("CameraButton6.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP6.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.377, camera_monitor_surface.get_height() // 1.26, 62, 40)},
    {"normal": pygame.image.load("CameraButton7.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP7.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.1965, camera_monitor_surface.get_height() // 1.234, 63, 41)},
    {"normal": pygame.image.load("CameraButton8.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP8.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.1965, camera_monitor_surface.get_height() // 1.1732, 62, 40)},
    {"normal": pygame.image.load("CameraButton9.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP9.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.4232, camera_monitor_surface.get_height() // 1.558, 62, 40)},
    {"normal": pygame.image.load("CameraButton10.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP10.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.1225, camera_monitor_surface.get_height() // 1.285, 64, 40)},
    {"normal": pygame.image.load("CameraButton11.png").convert_alpha(), "pressed": pygame.image.load("CameraButtonP11.png").convert_alpha(), "rect": pygame.Rect(camera_monitor_surface.get_width() // 1.116, camera_monitor_surface.get_height() // 1.555, 62, 40)}
]

# Load the camera map image and define its position
camera_map_image = pygame.image.load("Cam_Map.png")
camera_map_rect = camera_map_image.get_rect()
camera_map_rect.center = (screen_width // 1.225, screen_height // 1.355)
# Set initial button states (all buttons are not pressed)
camera_button_states = [False] * len(camera_buttons_data)

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

# Initialize the monitor state
monitor_open = False
prev_hovering_monitor_button = False
prev_hovering_camera_buttons = [False] * len(camera_buttons_data)
opening_animation_complete = False
closing_animation_complete = True
current_frame = 0

# Create a list to store camera feed images
camera_feed_images = [
    pygame.image.load("Camera1Feed.png"),
    pygame.image.load("Camera2Feed.png"),
    pygame.image.load("Camera3Feed.png"),
    pygame.image.load("Camera4Feed.png"),
    pygame.image.load("Camera5Feed.png"),
    pygame.image.load("Camera6Feed.png"),
    pygame.image.load("Camera7Feed.png"),
    pygame.image.load("Camera8Feed.png"),
    pygame.image.load("Camera9Feed.png"),
    pygame.image.load("Camera10Feed.png"),
    pygame.image.load("Camera11Feed.png"),
]

# Initialize the active camera (None for no active camera)
active_camera = None

# Initialize the camera button Y offsets
camera_button_offsets = [0] * len(camera_buttons_data)

# Define the camera's initial position
camera_x = 0
camera_y = 0

clock = pygame.time.Clock()

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
            hovering_camera_buttons = [camera_button_data["rect"].collidepoint(mouse_pos) for camera_button_data in camera_buttons_data]
          
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
                        
            # Update the camera buttons' positions based on the hover event (button 3d effect)
            for i, hovering in enumerate(hovering_camera_buttons):
                if hovering and not prev_hovering_camera_buttons[i]:
                    camera_buttons_data[i]["rect"].center = (
                        camera_buttons_data[i]["rect"].centerx,
                        camera_buttons_data[i]["rect"].centery + 3,
                    )
                elif not hovering and prev_hovering_camera_buttons[i]:
                    camera_buttons_data[i]["rect"].center = (
                        camera_buttons_data[i]["rect"].centerx,
                        camera_buttons_data[i]["rect"].centery - 3,
                    )
                                
            # Update the previous hovering states
            prev_hovering_monitor_button = hovering_monitor_button
            prev_hovering_camera_buttons = hovering_camera_buttons
        
        # Changing the buttons colour
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if any of the camera buttons are clicked
            for i, camera_button_data in enumerate(camera_buttons_data):
                if camera_button_data["rect"].collidepoint(event.pos):
                    # Update the button state to pressed
                    camera_button_states[i] = True
                    # Change the button image to the pressed version
                    camera_buttons_data[i]["rect"] = camera_button_data["pressed"].get_rect(
                        center=camera_buttons_data[i]["rect"].center)
                    # If the button is now pressed, set the active camera
                    if camera_button_states[i]:
                        active_camera = i
                    else:
                        active_camera = None
                        
                    # Reset the states of other buttons to not pressed
                    for j in range(len(camera_buttons_data)):
                        if j != i:
                            camera_button_states[j] = False
                            camera_buttons_data[j]["rect"] = camera_buttons_data[j]["normal"].get_rect(
                                center=camera_buttons_data[j]["rect"].center)
                            
    
        

    # Keep the camera within bounds
    camera_x = max(0, min(camera_x, office_image.get_width() - screen_width))
    camera_y = max(0, min(camera_y, office_image.get_height() - screen_height))
                                         
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the office image with the camera view
    screen.blit(office_image, (-camera_x, -camera_y))

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
                
            # Blit the camera buttons
            for i, camera_button_data in enumerate(camera_buttons_data):
                if camera_button_states[i]:
                    screen.blit(camera_button_data["pressed"], camera_button_data["rect"])
                else:
                    screen.blit(camera_button_data["normal"], camera_button_data["rect"])
            
            # Display the active camera feed
            if active_camera is not None and 0 <= active_camera < len(camera_feed_images):
                screen.blit(camera_feed_images[active_camera], (monitor_rect.x, monitor_rect.y))   
    else:
        if current_frame < len(closing_frames):
            screen.blit(closing_frames[current_frame], (0, 0))
            current_frame += 1
            if current_frame == len(closing_frames):
                closing_animation_complete = True
        # Handle mouse movement to control camera view
        mouse_x, mouse_y = pygame.mouse.get_pos()
        camera_x += (mouse_x - screen_width // 2) / 10  # Adjust the camera speed as needed
        camera_y += (mouse_y - screen_height // 2) / 10      
          
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
