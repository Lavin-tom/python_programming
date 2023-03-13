#binary clock implementation using pygame
#not completed

import pygame
import sys

frame_size_x = 480
frame_size_y = 280


#color
black = pygame.Color(40,42,54)
white = pygame.Color(248,248,242)
red = pygame.Color(255,85,85)
pink = pygame.Color(255, 121, 198)



#initialize the window
pygame.display.set_caption("Binary Clock")
clock_window = pygame.display.set_mode([frame_size_x,frame_size_y])

fps_controller = pygame.time.Clock()

#clock_window.fill(white)

Running = True
while Running:
    clock_window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.draw.rect(clock_window, red, pygame.Rect(0,0, 100, 300))
    pygame.draw.rect(clock_window, black, pygame.Rect(100,0, 100, 300))
    pygame.draw.rect(clock_window, pink, pygame.Rect(200,0, 100, 300))
    pygame.draw.circle(clock_window, pink,(20,200), 8)
    
    pygame.display.update()