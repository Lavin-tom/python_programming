import pygame
import sys
import math
import time

#color
black = pygame.Color(40,42,54)
white = pygame.Color(248,248,242)
red = pygame.Color(255, 85, 85)
green = pygame.Color(80, 250, 123)
pink = pygame.Color(255, 121, 198)
cyan = pygame.Color(139, 233, 253)

#every node is different in color 
color=[white,red,green,pink,cyan]
Running = True
i = 0

#initialize the window
pygame.init()
frame_size_x = 800
frame_size_y = 600
pygame.display.set_caption("Fractals Tree")
main_window = pygame.display.set_mode([frame_size_x,frame_size_y])
main_window.fill(black)

def fractal_tree(i,main_window, x, y, length, angle, depth):
    if depth == 0:
        return
    y2 = y + length * math.sin(math.radians(angle))
    x2 = x + length * math.cos(math.radians(angle)) 
    pygame.draw.line(main_window, color[i], (x, y), (x2, y2))
    pygame.display.update()
    time.sleep(0.025)

    i += 1
    if i == 5:
        i = 0

    fractal_tree(i,main_window, x2, y2, length*0.7, angle, depth-1)
    fractal_tree(i,main_window, x2, y2, length*0.7, angle+20, depth-1)
    fractal_tree(i,main_window, x2, y2, length*0.7, angle-20, depth-1)


def main():
    start_x = frame_size_x  // 2
    start_y = frame_size_y - 50
    #fractal tree
    depth = 8
    branch_length = 150
    start_angle = -90
    Running = True
    fractal_tree(i,main_window,start_x,start_y, branch_length,start_angle,depth)
    print("Tree generated...")

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
        
if __name__ == "__main__":
    main()