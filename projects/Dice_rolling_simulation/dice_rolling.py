# dice rolling simulation

import pygame
import sys
import random

frame_size_x = 300
frame_size_y = 300
global x,y
x = 125
y = 125
#color
dark_black = pygame.Color(0,0,0)
black = pygame.Color(40,42,54)
red = pygame.Color(255,85,85)
white = pygame.Color(248, 248, 242)
pink = pygame.Color(255, 121, 198)

#initializing the window

pygame.display.set_caption("Dice rolling")
game_window = pygame.display.set_mode([frame_size_x,frame_size_y])

fps_controller = pygame.time.Clock()

def displayCircle(random_no):
    for i in range(0, random_no+1):
        pygame.draw.rect(game_window, white, pygame.Rect(100,100, 100, 100),border_radius=20)
        if i>0:
            pygame.draw.circle(game_window, red,(125,135), 8)
            pygame.draw.circle(game_window, dark_black,(125,135), 8, width=1)
        if i>1:
            pygame.draw.circle(game_window, red,(150,135), 8)
            pygame.draw.circle(game_window, dark_black,(150,135), 8, width=1)
        if i>2:
            pygame.draw.circle(game_window, red,(175,135), 8)
            pygame.draw.circle(game_window, dark_black,(175,135), 8, width=1)
        if i>3:
            pygame.draw.circle(game_window, red,(125,160), 8)
            pygame.draw.circle(game_window, dark_black,(125,160), 8, width=1)
        if i>4:
            pygame.draw.circle(game_window, red,(150,160), 8)
            pygame.draw.circle(game_window, dark_black,(150,160), 8, width=1)
        if i>5:
            pygame.draw.circle(game_window, red,(175,160), 8)
            pygame.draw.circle(game_window, dark_black,(175,160), 8, width=1)

        

            
game_window.fill(black)
pygame.draw.rect(game_window, white, pygame.Rect(100,100, 100, 100),border_radius=20)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                random_no=random.randrange(1, 7)
                displayCircle(random_no)
    
    pygame.draw.rect(game_window, dark_black, pygame.Rect(100,100, 100, 100),border_radius=20, width=2)
    pygame.display.update()