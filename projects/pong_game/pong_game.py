#! /usr/bin/python3

# pong game implimentation

import pygame
import sys
import random

frame_size_x = 500
frame_size_y = 500

pygame.font.init()
# color - uses dracula color sheme
black = pygame.Color(40, 42, 54)
white = pygame.Color(248, 248, 242)
red = pygame.Color(255, 85, 85)
green = pygame.Color(80, 250, 123)

# initialize the game Window
pygame.display.set_caption("Pong_game")
game_window = pygame.display.set_mode([frame_size_x, frame_size_y])
fps_controller = pygame.time.Clock()


def init_variables():
    global bat_pos, ball_pos, square_size, direction, speed, score, ball, ball_speed, ball_direction, life, life_pos
    bat_pos = [240, 490]
    ball_speed = [10, 10]
    square_size = 10
    direction = "CENTER"
    speed = 20
    score = 0
    life = 5
    life_pos = [440, 10]
    ball_pos = [random.randrange(1, (frame_size_x // 4)), 1]
    ball = True
    ball_direction = "DOWN"


init_variables()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: "+str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_surface = score_font.render("Game Over!!\n  Score: "+str(score), True, color)
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)


# to make the life count at the top of the window
def show_life(life):
    if life < 0:
        print(f'Game Over!! {score}')
        show_score(2, white, "consolas", 15)
        pygame.time.delay(2000)
        init_variables()
    for i in range(1, life+1):
        pygame.draw.circle(game_window, green, (life_pos[0] + 10 * i, life_pos[1]), 5)

# game loop
while True:
    # check for keypress - Paddle right, left and esc for quit from game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                direction = "RIGHT"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT or event.key == ord("a"):
                direction = "LEFT"

    # setting the paddle at the center at the beginning
    if direction == "CENTER":
        bat_pos[0] = frame_size_x//2 - square_size * 5
    elif direction == "RIGHT":
        bat_pos[0] += square_size
    elif direction == "LEFT":
        bat_pos[0] -= square_size

    if bat_pos[0] < 0:
        bat_pos[0] = 0
    elif bat_pos[0] > frame_size_x - square_size * 10:
        bat_pos[0] = frame_size_x - square_size * 10

    # ball direction
    if ball_direction == "DOWN":
        ball_pos[1] += ball_speed[1]
        ball_pos[0] += ball_speed[0]

    elif ball_direction == "UP":
        ball_pos[1] -= ball_speed[1]
        ball_pos[0] -= ball_speed[0]

    if ball_pos[1] >= 490 and ball_pos[0] >= bat_pos[0] and ball_pos[0] <= bat_pos[0] + square_size * 10:
        ball_speed[1] = -ball_speed[1]
        ball_speed[0] = ball_speed[0] + (ball_pos[0] - (bat_pos[0] + square_size * 2.5)) / 5
        score += 1
        ball = False
    else:
        ball = True

    if ball and ball_pos[1] >= 490:
        life -= 1
        ball = False

    # for reflect back the ball
    if ball_pos[0] - 10 <= 0 or ball_pos[0] + 10 >= frame_size_x:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] >= 490 and ball_pos[0] >= bat_pos[0] and ball_pos[0] <= bat_pos[0] + square_size * 10:
        ball_speed[1] = -ball_speed[1]

    # for new ball
    if not ball:
        ball_pos = [random.randrange(1, (frame_size_x // square_size) * square_size), 1]
        ball = True

    # game window designing
    game_window.fill(black)
    pygame.draw.rect(game_window, red, pygame.Rect(bat_pos[0], bat_pos[1], square_size * 10, square_size))
    if ball:
        pygame.draw.circle(game_window, white, (ball_pos[0], ball_pos[1]), 5)
    show_score(1, white, 'consolas', 20)
    show_life(life)
    pygame.display.update()
    fps_controller.tick(speed)
