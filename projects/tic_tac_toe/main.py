#! /usr/bin/python3
# tic-tac-toe implementation
# pygame

import pygame
import sys

frame_size_x = 500
frame_size_y = 500
square_size = 100

player_turns = 0
symbol = 0
b = []
g_array = []
r_array = []
pygame.font.init()
g_flag = False
r_flag = False
win_flag = False

# color - dracula color scheme
black = pygame.Color(40, 42, 54)
white = pygame.Color(248, 248, 242)
red = pygame.Color(255, 85, 85)
green = pygame.Color(80, 250, 123)
pink = pygame.Color(255, 121, 198)

# initialize the game window
pygame.display.set_caption("Tic_Tac_Toe_Testing")
game_window = pygame.display.set_mode([frame_size_x, frame_size_y])
fps_controller = pygame.time.Clock()

# show grids in windows
def grids():
    for i in range(3):
        for j in range(3):
            x = i * square_size + 100
            b.append(x)
            y = j * square_size + 100
            b.append(y)
            pygame.draw.rect(game_window, pink, (x, y, square_size, square_size), 1)


# to draw x symbol
def draw_X(x, y, size, color):
    pygame.draw.line(game_window, color, (x - size / 2, y - size / 2), (x + size / 2, y + size / 2), 5)
    pygame.draw.line(game_window, color, (x - size / 2, y + size / 2), (x + size / 2, y - size / 2), 5)


# to show player turns
def show_display(choice, color, font, size, player_turns):
    score_font = pygame.font.SysFont(font, size)
    if player_turns % 2 == 1:
        score_surface = score_font.render("Player 1", True, green)
    else:
        score_surface = score_font.render("Player 2", True, red)
    game_window.fill(black, (150, 50, 150, 50))  # add this line to clear the previous text
    game_window.blit(score_surface, (150, 50))


# show final winner
def show_win_card(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    if choice == 1:
        win_surface = score_font.render("Green Win", True, color)
    elif choice == 2:
        win_surface = score_font.render("Red Win", True, color)
    else:
        win_surface = score_font.render("Game Draw", True, white)
    game_window.fill(black, (150, 50, 150, 50))
    game_window.blit(win_surface, (150, 50))


# validation for win
def validation(array):
    for i in range(0, len(array)):
        element = array[i]
        x, y = element
        x = int(x)
        y = int(y)

        # check for rows
        row_count = 0
        for pos in array:
            if pos[1] == y:
                row_count += 1

        if row_count == 3:
            return True

        # column check
        col_count = 0
        for pos in array:
            if pos[0] == x:
                col_count += 1
        if col_count == 3:
            return True

        # diagonal check
        dia_count = 0
        for pos in array:
            if pos[0] == pos[1]:
                dia_count += 1
        if dia_count == 3:
            return True

        if x + y == 450:
            diag_count = 0
            for pos in array:
                if pos[0] + pos[1] == 450:
                    diag_count += 1
            if diag_count == 3:
                return True


# game loop
game_window.fill(black)
while True:

    show_display(1, white, 'courier', 20, player_turns)
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

                # to avoid the click outside the grids
                if event.pos[0] > 400 or event.pos[1] > 400:
                    break
                x = x_index * square_size + 100 + square_size / 2
                y = y_index * square_size + 100 + square_size / 2
                if (x, y) in r_array or (x, y) in g_array:
                    continue
                else:
                    if player_turns % 2 == 0:
                        if (x, y) not in r_array and not win_flag:
                            pygame.draw.circle(game_window, red, (x, y), 30, 5)
                            r_array.append((x, y))
                            symbol += 1
                    else:
                        if (x, y) not in g_array and not win_flag:
                            draw_X(x, y, 50, green)
                            g_array.append((x, y))
                            symbol += 1

                player_turns += 1

    g_flag = validation(g_array)
    r_flag = validation(r_array)

    # to check the draw condition
    if symbol == 9:
        show_win_card(3, white, 'courier', 20)
        keys = pygame.key.get_pressed()
        if any(keys):
            pygame.quit()
            sys.quit()
    # to print green as a winner
    if g_flag:
        show_win_card(1, green, 'courier', 20)
        win_flag = True
        keys = pygame.key.get_pressed()
        if any(keys):
            pygame.quit()
            sys.exit()
    # to print red as a winner
    elif r_flag:
        show_win_card(2, red, 'courier', 20)
        win_flag = True
        keys = pygame.key.get_pressed()
        if any(keys):
            pygame.quit()
            sys.exit()
    grids()
    pygame.display.update()
    fps_controller.tick(10)
