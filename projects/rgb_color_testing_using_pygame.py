import pygame
import sys

frame_size_x = 300
frame_size_y = 300

#initialize the window
speed = 200
square_size= 100
r =0
b =0
g = 0
#color 
black = pygame.Color(40,42,54)
red = pygame.Color(255,85,85)
current_color = pygame.Color(0,100,0)
previous_color = pygame.Color(0,0,0)
pygame.display.set_caption("RGB_Color_Testing")
game_window = pygame.display.set_mode([frame_size_x,frame_size_y])
fps_controller = pygame.time.Clock()

#Super loop
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    current_color = pygame.Color(r,g,b)
    color = pygame.Color.lerp(previous_color,current_color,.5)
    game_window.fill(black)
    pygame.draw.rect(game_window, color, pygame.Rect(100,100, square_size, square_size))
   
    if b<255:
        b += 1
    if b==255 and g <255:
        g += 1
        b = 0
    if g == 255:
        r += 1
        b = 0
        g = 0
    if r == 255:
        r=0
        g=0
        b=0
    previous_color = pygame.Color(r,g,b)
    #print(current_color)
    pygame.display.update()
    fps_controller.tick(speed)