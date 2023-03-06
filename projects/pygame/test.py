#bouncing ball 

import pygame
import random
import sys
import math
# Initialize Pygame
pygame.init()

# Set up the display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Endless Bouncing Ball")

# Set up the ball
ball_radius = 10
ball_x = random.randint(ball_radius, width - ball_radius)
ball_y = random.randint(ball_radius, height - ball_radius)
ball_color = (255, 255, 255)
ball_speed = 2
ball_direction = random.uniform(0, 2 * math.pi)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the ball position
    ball_x += ball_speed * math.cos(ball_direction)
    ball_y += ball_speed * math.sin(ball_direction)

    # Check for collision with walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_direction = math.pi - ball_direction
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_direction = -ball_direction

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()