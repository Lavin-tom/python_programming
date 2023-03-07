# sudoku solution 
# back tracking algorith - is used as a algorith for solve the puzzle
# same row
def same_row(sudoku,i,j,num):
    for n in range(0,9):
        if sudoku[i][n] == num:
            return False
    return True

# same square or not
def same_square(sudoku,i,j,num):
    if i < 3:
        i = 0
    elif i < 6:
        i = 3
    else:
        i = 6
    if j < 3:
        j = 0
    elif j < 6:
        j = 3
    else:
        j = 6
    for x in range(i, i+3):
        for y in range(j, j+3):
            if sudoku[x][y] == num:
                return False
    return True

# same column
def same_column(sudoku,i,j,num):
    for n in range(0,9):
        if sudoku[n][j] == num:
            return False
    return True

# solve sudoku
def solve_sudoku(sudoku,x,y):
    # already filled space 
    if sudoku[x][y] != 0:
        # to reach at the end
        if x == 8 and y == 8:
            return True
        if x < 8:
            tx = x + 1
            ty = y
        else:
            tx = 0
            ty = y + 1
        if solve_sudoku(sudoku, tx, ty):
            return True
        else:
            return False
        
    # to fill vacant space
    for num in range(1, 10):
        # check for each num , start from 1 to 9
        if same_row(sudoku, x, y, num) and same_column(sudoku, x, y, num) and same_square(sudoku, x, y, num):
            # add values to the vacant slot
            sudoku[x][y] = num

            #backtracking algorithm
            if x == 8 and y == 8:
                return True
            if x < 8:
                tx = x + 1
                ty = y
            else:
                tx = 0
                ty = y + 1
            if solve_sudoku(sudoku, tx, ty):
                return True
            
            # reset the slot if no solution found
            sudoku[x][y] = 0
            
    return False