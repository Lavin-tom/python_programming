#! /usr/bin/python3
# tic-tac-toe implementation
# pygame
# not yet completed 

import pygame
import sys

frame_size_x = 500
frame_size_y = 500
square_size = 100

common_space_x = 300
common_space_y = 50

player_turns = 0
b = []
g_array = []
r_array = []
pygame.font.init()

# color - dracula color scheme
black = pygame.Color(40, 42, 54)
white = pygame.Color(248, 248, 242)
red = pygame.Color(255, 85, 85)
green = pygame.Color(80, 250, 123)

# initialize the game window
pygame.display.set_caption("Tic_Tac_Toe_Testing")
game_window = pygame.display.set_mode([frame_size_x, frame_size_y])
fps_controller = pygame.time.Clock()


# game loop

game_window.fill(black)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("mouse pressed", event.pos)
                x_index = int((event.pos[0] - 100) / square_size)
                y_index = int((event.pos[1] - 100) / square_size)
                if (x_index, y_index) in r_array or (x_index, y_index) in g_array:
                    # skip the drawing step if the position has already been drawn
                    continue
                else:
                    x = x_index * square_size + 100 + square_size / 2
                    y = y_index * square_size + 100 + square_size /2
                    if player_turns % 2 == 0:
                        if (x, y) not in r_array:
                            pygame.draw.circle(game_window, red, (x,y), 30, 5)
                            r_array.append((x,y))
                    else:
                        if (x, y) not in g_array:
                            pygame.draw.circle(game_window, green, (x,y), 30, 5)
                            g_array.append((x, y))

                player_turns += 1

    for i in range(3):
        for j in range(3):
            x = i * square_size + 100
            b.append(x)
            y = j * square_size + 100
            b.append(y)
            pygame.draw.rect(game_window, green, (x, y, square_size, square_size), 1)
 
    pygame.draw.rect(game_window, red, (100, 50, common_space_x, common_space_y), 1)
    # print(b)
    pygame.display.update()
    fps_controller.tick(10)
