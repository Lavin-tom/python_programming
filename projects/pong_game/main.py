#! /usr/bin/python3

# pong game implimentation

import pygame
import sys
import random

frame_size_x = 500
frame_size_y = 500

# color
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)


# initialize the game Window
pygame.display.set_caption("Pong_game_testing")
game_window = pygame.display.set_mode([frame_size_x, frame_size_y])

fps_controller = pygame.time.Clock()


def init_variables():
    global bat_pos, ball_pos, square_size, direction, speed, score, ball
    bat_pos = [[240, 490]]
    square_size = 10
    direction = "CENTER"
    speed = 15
    score = 0
    ball_pos = [random.randrange(1,(frame_size_x // 4)), 1]
    ball = True
    print(ball_pos[0],ball_pos[1])

init_variables()

# game loop

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                direction = "RIGHT"
            else:
                direction = "LEFT"

    if direction == "CENTER":
        bat_pos = [240, 490]
    elif direction == "RIGHT":
        bat_pos[0] += square_size
    else:
        bat_pos[0] -= square_size

    if bat_pos[0] < 0:
        bat_pos[0] = square_size
        direction = "RIGHT"
    elif bat_pos[0] > frame_size_x - square_size:
        bat_pos[0] = frame_size_x
        direction = "LEFT"

    # ball direction
    ball_pos[1] += square_size
    print(bat_pos[0], ball_pos[1])
    
    # for new ball
    if ball_pos[1] > frame_size_x and ball:
        ball_pos = [random.randrange(1, (frame_size_x // square_size) * square_size), 1]

    # game window designing
    game_window.fill(black)
    for pos in bat_pos:
        pygame.draw.rect(game_window, red, pygame.Rect(bat_pos[0], bat_pos[1], square_size * 10, square_size))

    if (bat_pos[0] + 1 == ball_pos[0]):
        score += 1
        ball = False

    print(score)
    
    # pygame.draw.rect(game_window, white, pygame.Rect(ball_pos[0], ball_pos[1], square_size, square_size))
    pygame.draw.circle(game_window, white, (ball_pos[0], ball_pos[1]), 5)

    pygame.display.update()
    fps_controller.tick(speed)
