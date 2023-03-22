import pygame
import math

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lissajous Curves")
clock = pygame.time.Clock()

# Define some colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(248, 248, 242)

c1 = pygame.Color(255, 0, 0)
c2 = pygame.Color(255,64,0)
c3 = pygame.Color(255,128,0)
c4 = pygame.Color(255,191,0)
c5 = pygame.Color(255,255,0)
c6 = pygame.Color(191,255,0)
c7 = pygame.Color(128,255,0)
c8 = pygame.Color(64,255,0)
c9 = pygame.Color(0,255,0)
c10 = pygame.Color(0,255,64)
c11 = pygame.Color(0,255,128)
c12 = pygame.Color(0,255,191)
c13 = pygame.Color(0,255,255)
c14 = pygame.Color(0,191,255)
c15 = pygame.Color(0,128,255)
c16 = pygame.Color(0,64,255)
c17 = pygame.Color(0,0,255)
c18 = pygame.Color(64,0,255)
c19 = pygame.Color(128,0,255)
c20 = pygame.Color(191,0,255)
c21 = pygame.Color(255,0,255)
c22 = pygame.Color(255,0,191)
c23 = pygame.Color(255,0,128)
c24 = pygame.Color(255,0,64)
c25 = pygame.Color(255,0,0)

colors = []
for r in range(255, -1, -64):
    for b in range(0, 256, 32):
        for g in range(0, 256, 32):
            colors.append(pygame.Color(r, g, b))
            
#color = [violet,indigo,blue,green,yellow,orange,red]
color = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,
         c19,c20,c21,c22,c23,c24,c25]
# Define some parameters
A = 200 # Scaling factor for x
B = 200 # Scaling factor for y
a = 5 # Frequency for x
b = 4 # Frequency for y
delta = math.pi / 2 # Phase angle

# Define some variables
t = 0 # Time parameter
dt = 0.001 # Time increment

# Clear screen
screen.fill(BLACK)
# for color change
i = 0
delay = 0

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key== pygame.K_DOWN:
                a -= 1
                screen.fill(BLACK)
                print(a)
                
            elif event.key == pygame.K_UP:
                a += 1
                screen.fill(BLACK)
                print(a)
    


    # Calculate x and y coordinates of the point on the curve
    x = A * math.sin(a * t + delta) + 400 # Add 400 to center on screen
    y = B * math.sin(b * t) + 300 # Add 300 to center on screen

    # Draw the point as a white circle with radius 1 pixels 
    pygame.draw.circle(screen, color[i], (int(x), int(y)), 1)

    # Increment time parameter 
    t += dt

    # Update display 
    pygame.display.flip()

    # Limit frame rate 
    clock.tick(500)

    delay+=1
    if delay == 200:
        i+=1
        delay = 0
    if i>24:
        i = 0
        
# Quit pygame 
pygame.quit()