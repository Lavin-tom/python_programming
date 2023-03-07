import pygame
import os
import sys

from solutionOfSudoku.sudoku_solution import solve_sudoku

#initialize the pygame
pygame.init()

#define colors
white = pygame.Color(248, 248, 242)
black = pygame.Color(40, 42, 54)
red = pygame.Color(255, 85, 85)
green = pygame.Color(80, 250, 123)

#global variable
x = y = 0
count =0
parity_flag = False
game_over = False

# set up the display
window_size = (500,600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Sudoku")

#set up the font
font = pygame.font.SysFont('Arial',30)
font_text = pygame.font.SysFont('Arial',18)


#define the sudoku board
board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
         [6, 8, 0, 0, 7, 0, 0, 9, 0],
         [1, 9, 0, 0, 0, 4, 5, 0, 0],
         [8, 2, 0, 1, 0, 0, 0, 4, 0],
         [0, 0, 4, 6, 0, 2, 9, 0, 0],
         [0, 5, 0, 0, 0, 3, 0, 2, 8],
         [0, 0, 9, 3, 0, 0, 0, 7, 4],
         [0, 4, 0, 0, 5, 0, 0, 3, 6],
         [7, 0, 3, 0, 1, 8, 0, 0, 0]]

#define the coordinated and size of each cell
cell_size = 50
cell_coords = [(x,y) for x in range(0,9*cell_size,cell_size) for y in range(0,9*cell_size,cell_size)]

#define the selected cell
selected_cell = None

# define a function to draw the Sudoku board
def draw_board():
    screen.fill(black)
    for i in range(9):
        for j in range(9):
            # get the value of the cell
            cell_value = board[i][j]
            # get the coordinates of the cell
            cell_x, cell_y = cell_coords[i*9 + j]
            # draw the cell
            cell_rect = pygame.Rect(cell_x, cell_y, cell_size, cell_size)
            if selected_cell == (i, j):
                pygame.draw.rect(screen, black, cell_rect)
            else:
                pygame.draw.rect(screen, black, cell_rect)
            pygame.draw.rect(screen, white, cell_rect, 2)
            # draw the cell value
            if cell_value != 0:
                text_surface = font.render(str(cell_value), True, white)
                text_rect = text_surface.get_rect(center=(cell_x+cell_size/2, cell_y+cell_size/2))
                screen.blit(text_surface, text_rect)

            # border line for board
            pygame.draw.line(screen,red,(150,0),(150,450),width=5)
            pygame.draw.line(screen,red,(300,0),(300,450),width=5)
            pygame.draw.line(screen,red,(0,150),(450,150),width=5)
            pygame.draw.line(screen,red,(0,300),(450,300),width=5)

            score_surface = font_text.render("-press down arrow to clear all data", True, white)
            screen.blit(score_surface, (10, 455))
            score_surface = font_text.render("-press mouse button to add your sudoku", True, white)
            screen.blit(score_surface, (10, 475))
            score_surface = font_text.render("-press up arrow to solve sudoku", True, white)
            screen.blit(score_surface, (10, 495))

            if not parity_flag and game_over:
                score_surface = font_text.render("sudoku is parity free", True, green)
                screen.blit(score_surface, (10, 515))
            elif game_over and parity_flag:
                score_surface = font_text.render("sudoku has parity error", True, red)
                screen.blit(score_surface, (10, 515))

def parity_check(sudoku):
    count = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                count += 1
    if count == 81:
        parity_flag = True
        print('sudoku is parity free')
    else:
        parity_flag = False
        print('sudoku has parity error')

running = True
while running:
    #os.system('cls')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if (event.key == pygame.K_UP or event.key == ord("w")):
                print('solving puzzle...')
                solve_sudoku(board,x,y)
                game_over = True
                parity_check(board)
                print('solved')
            if (event.key == pygame.K_DOWN):
                print('clearing every field')
                parity_flag = False
                game_over = False
                for i in range(9):
                    for j in range(9):
                        board[i][j]=0
        elif pygame.mouse.get_pressed()[0]:
            x,y = pygame.mouse.get_pos()
            x = int(x / 50)
            y = int(y / 50)
            count = board[x][y]
            if pygame.mouse.get_pressed()[0]:
                count+=1
                if count > 9:
                    count = 1
                board[x][y] = count
            #print(count)
            
    draw_board()
    pygame.display.flip()
    pygame.display.update()
pygame.quit()