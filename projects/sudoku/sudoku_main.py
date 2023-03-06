# not yet completed
import sys



sudoku = [  [5,3,0,0,7,0,0,0,0],
		    [6,0,0,1,9,5,0,0,0],
			[0,9,8,0,0,0,0,6,0],
			[8,0,0,0,6,0,0,0,3],
			[4,0,0,8,0,3,0,0,1],
			[7,0,0,0,2,0,0,0,6],
			[0,6,0,0,0,0,2,8,0],
			[0,0,0,4,1,9,0,0,5],
			[0,0,0,0,8,0,0,7,9]]

x = y =0
#print(sudoku[1][1])
def get_sudoku(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            input(sudoku[i][j])

def print_sudoku(sudoku):
    for i in range(0,9):
        if i==3 or i ==6:
            print('- - - - - - - - - -\n')
        for j in range(0,9):
            if j==3 or j==6:
                print('|',end=' ')
            print(sudoku[i][j],end=' ')
        print('\n')
    print('\n')

def solve_sudoku(sudoku,x,y):
    num = 1
    tx = ty = 0
    # already filled space 
    if sudoku[x][y] != 0:
        if x ==8 and y ==8:
            return 1
        if x<8:
            x += 1
        else:
            x =0
            y += 1
        if solve_sudoku(sudoku, x, y)
            return 1
        else
            return 0

print("Choose any option")
option = int(input('1. Add a 9X9 sudoku to get solution\n2. Go for default one\n3. Exit\n'))
if option == 1:
    print("Enter sudoku to solve...\n")
    get_sudoku(sudoku)
elif option == 2:
    print('You selected system sudoku as demo\n')
elif option == 3:
    sys.QUIT

print_sudoku(sudoku)
solve_sudoku(sudoku,x,y)
print('\tsolution\n')
print_sudoku(sudoku)