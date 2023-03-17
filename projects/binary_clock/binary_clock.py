#binary clock implementation using pygame

import pygame
import sys
import time
import datetime

frame_size_x = 480
frame_size_y = 280

#color
black = pygame.Color(40,42,54)
white = pygame.Color(248,248,242)
red = pygame.Color(255,85,85)
pink = pygame.Color(255, 121, 198)

font = 'courier' 
size = 20

#initialize the window
pygame.init()
pygame.display.set_caption("Binary Clock")
pygame.font.init()
clock_window = pygame.display.set_mode([frame_size_x,frame_size_y])
font = pygame.font.SysFont('Arial', 30)
fps_controller = pygame.time.Clock()

def dimCircle():
    #second right side
    for i in range(20,150,40):
        pygame.draw.circle(clock_window,white,(400,i),8)

    #second left side
    for i in range(60,150,40):
        pygame.draw.circle(clock_window,white,(360,i),8)

    #minutes right side
    for i in range(20,150,40):
        pygame.draw.circle(clock_window,white,(280,i),8)

    #minutes left side
    for i in range(60,150,40):
        pygame.draw.circle(clock_window,white,(200,i),8)

    #hours right side
    for i in range(20,150,40):
        pygame.draw.circle(clock_window,white,(120,i),8)

    #hours left side
    for i in range(100,150,40):
        pygame.draw.circle(clock_window,white,(40,i),8)

def circleVisible(seconds,minutes,hours):
    clock_window.fill(black)
    dimCircle()
    r = seconds % 10
    text = font.render(f'{r}', True, white)
    clock_window.fill(black, (400,160, 50,50))
    clock_window.blit(text, (395, 160))
    
    for i in range (4): 
        n = (r>>i)&1    
        if i == 3 and n == 1:
            pygame.draw.circle(clock_window, red,(400,20), 8)
        elif i == 2 and n == 1:
            pygame.draw.circle(clock_window, red,(400,60), 8)
        elif i == 1 and n == 1:
            pygame.draw.circle(clock_window, red,(400,100), 8)
        elif i == 0 and n == 1:
            pygame.draw.circle(clock_window, red,(400,140), 8)

    r = seconds // 10
    text = font.render(f'{r}', True,white)
    clock_window.fill(black, (360,160, 30,30))
    clock_window.blit(text, (355, 160))
    for i in range (3): 

        n = (r>>i)&1
        if i == 2 and n == 1:
            pygame.draw.circle(clock_window, red,(360,60), 8)
        if i == 1 and n == 1:
            pygame.draw.circle(clock_window, red,(360,100), 8)
        if i == 0 and n == 1:
            pygame.draw.circle(clock_window, red,(360,140), 8)
        
    r = minutes % 10
    text = font.render(f'{r}', True,white)
    clock_window.fill(black, (280,160, 30,30))
    clock_window.blit(text, (275, 160))
    for i in range (4): 
        n = (r>>i)&1
        if i == 3 and n == 1:
            pygame.draw.circle(clock_window, red,(280,20), 8)
        if i == 2 and n == 1:
            pygame.draw.circle(clock_window, red,(280,60), 8)
        if i == 1 and n == 1:
            pygame.draw.circle(clock_window, red,(280,100), 8)
        if i == 0 and n == 1:
            pygame.draw.circle(clock_window, red,(280,140), 8)

    r = minutes // 10
    text = font.render(f'{r}', True,white)
    clock_window.fill(black, (200,160, 30,30))
    clock_window.blit(text, (195, 160))
    for i in range (3): 
        n = (r>>i)&1
        if i == 2 and n == 1:
            pygame.draw.circle(clock_window, red,(200,60), 8)
        if i == 1 and n == 1:
            pygame.draw.circle(clock_window, red,(200,100), 8)
        if i == 0 and n == 1:
            pygame.draw.circle(clock_window, red,(200,140), 8)

    r = hours % 10
    text = font.render(f'{r}', True, white)
    clock_window.fill(black, (120,160, 30,30))
    clock_window.blit(text, (115, 160))
    for i in range (4): 
        n = (r>>i)&1
        if i == 3 and n == 1:
            pygame.draw.circle(clock_window, red,(120,20), 8)
        if i == 2 and n == 1:
            pygame.draw.circle(clock_window, red,(120,60), 8)
        if i == 1 and n == 1:
            pygame.draw.circle(clock_window, red,(120,100), 8)
        if i == 0 and n == 1:
            pygame.draw.circle(clock_window, red,(120,140), 8)

    r = hours // 10
    text = font.render(f'{r}', True,white)
    clock_window.fill(black, (40,160, 30,30))
    clock_window.blit(text, (35, 160))
    for i in range (2): 
        n = (r>>i)&1
        if i == 1 and n == 1:
            pygame.draw.circle(clock_window, red,(40,100), 8)
        if i == 0 and n == 1:
            pygame.draw.circle(clock_window, red,(40,140), 8)
    
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
 
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    hours = int(current_time.split(":")[0])
    minutes = int(current_time.split(":")[1])
    seconds = int(current_time.split(":")[2])

    circleVisible(seconds,minutes,hours)
    time.sleep(1)
    pygame.display.update()