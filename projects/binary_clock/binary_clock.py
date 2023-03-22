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

#initialize the window
pygame.init()
pygame.display.set_caption("Binary Clock")
pygame.font.init()
clock_window = pygame.display.set_mode([frame_size_x,frame_size_y])
font = pygame.font.SysFont('Arial', 30)
fps_controller = pygame.time.Clock()
Running = True

#to display the off circle/ dim circle
def dimCircle():
    # define the coordinates for each column of circles
    coords = [(400, i) for i in range(20, 150, 40)] + \
             [(360, i) for i in range(60, 150, 40)] + \
             [(280, i) for i in range(20, 150, 40)] + \
             [(200, i) for i in range(60, 150, 40)] + \
             [(120, i) for i in range(20, 150, 40)] + \
             [(40, i) for i in range(100, 150, 40)]

    # draw all the circles using a nested loop
    for x, y in coords:
        pygame.draw.circle(clock_window, white, (x, y), 8)
        
# to display the on circle
def binaryCircle(x,y):
    pygame.draw.circle(clock_window, red,(x,y), 8)

#to display time in text format
def displayTime(r,x,y,blix_x,blix_y):
    text = font.render(f'{r}', True, white)
    clock_window.fill(black, (x,y, 30,30))
    clock_window.blit(text, (blix_x,blix_y))

# main function to control the flow of binary clock
def circleVisible(seconds,minutes,hours):
    clock_window.fill(black)
    
    dimCircle()

    r = seconds % 10
    displayTime(r,400,160,395,160)
    for i in range (4): 
        n = (r>>i)&1    
        if i == 3 and n == 1:
            binaryCircle(400,20)
        elif i == 2 and n == 1:
            binaryCircle(400,60)
        elif i == 1 and n == 1:
            binaryCircle(400,100)
        elif i == 0 and n == 1:
            binaryCircle(400,140)

    r = seconds // 10
    displayTime(r,360,160,355,160)
    for i in range (3): 

        n = (r>>i)&1
        if i == 2 and n == 1:
            binaryCircle(360,60)
        if i == 1 and n == 1:
            binaryCircle(360,100)
        if i == 0 and n == 1:
            binaryCircle(360,140)
        
    r = minutes % 10
    displayTime(r,280,160,275,160)
    for i in range (4): 
        n = (r>>i)&1
        if i == 3 and n == 1:
            binaryCircle(280,20)
        if i == 2 and n == 1:
            binaryCircle(280,60)
        if i == 1 and n == 1:
            binaryCircle(280,100)
        if i == 0 and n == 1:
            binaryCircle(280,140)

    r = minutes // 10
    displayTime(r,200,160,195,160)
    for i in range (3): 
        n = (r>>i)&1
        if i == 2 and n == 1:
            binaryCircle(200,60)
        if i == 1 and n == 1:
            binaryCircle(200,100)
        if i == 0 and n == 1:
            binaryCircle(200,140)

    r = hours % 10
    displayTime(r,120,160,115,160)
    for i in range (4): 
        n = (r>>i)&1
        if i == 3 and n == 1:
            binaryCircle(120,20)
        if i == 2 and n == 1:
            binaryCircle(120,60)
        if i == 1 and n == 1:
            binaryCircle(120,100)
        if i == 0 and n == 1:
            binaryCircle(120,140)

    r = hours // 10
    displayTime(r,40,160,35,160)
    for i in range (2): 
        n = (r>>i)&1
        if i == 1 and n == 1:
            binaryCircle(40,100)
        if i == 0 and n == 1:
            binaryCircle(40,140)
    
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Running = False
                pygame.quit()
                sys.exit()
    #fetch current time 
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    #extracting hour minutes and second from the time convert to int
    hours = int(current_time.split(":")[0])
    minutes = int(current_time.split(":")[1])
    seconds = int(current_time.split(":")[2])

    circleVisible(seconds,minutes,hours)
    time.sleep(1)
    pygame.display.update()