import pygame
import pygame.camera

pygame.init()

# create a Pygame window
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# initialize the webcam
pygame.camera.init()
cameras = pygame.camera.list_cameras()
if not cameras:
    raise ValueError('No cameras found')
camera = pygame.camera.Camera(cameras[0], window_size)
camera.start()

# create a Pygame surface to display the camera feed
camera_surface = pygame.surface.Surface(window_size, 0, screen)

# event loop to handle user input and exit the program
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # capture a frame from the camera
    camera_surface = camera.get_image(camera_surface)

    # update the Pygame surface with the captured frame
    screen.blit(camera_surface, (0, 0))

    # update the Pygame display
    pygame.display.flip()

# stop the camera and quit Pygame
camera.stop()
pygame.quit()
