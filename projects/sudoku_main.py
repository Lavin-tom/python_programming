x = y =0
sc = sr = ss = 0
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

# same square or not
def same_square(sudoku,i,j,num):
    count = 0
    if i > 2 and i <= 5:
        i = 3
    elif i > 5:
        i = 6
    else:
        i = 0
    if j > 2 and j <= 5:
        j = 3 
    elif j > 5:
        j = 6
    else:
        j = 0
    for k in range(i, i+3):      #extra
        for l in range(j, j+3):  #extra
            if num != sudoku[k][l]:
                count += 1
    if count == 9:
        return 1
    else:
        return 0
    

# same raw
def same_raw(sudoku,i,j,num):
    count = 0
    for n in range(0,9):
        if sudoku[i][n]!=num:
            count += 1
    if count == 9:
        return 1
    else:
        return 0
    

# same column
def same_column(sudoku,i,j,num):
    count  = 0
    for n in range(0,9):
        if sudoku[n][j]!=num:
            count += 1
    if count == 9:
        return 1
    else:
        return 0
   

# solve sudoku
def solve_sudoku(sudoku,x,y):
    num = 1
    tx = 0
    ty = 0
    # already filled space 
    if sudoku[x][y] != 0:
        # to reach at the end
        if x == 8 and y == 8:
            return 1
        if x < 8:
            x += 1
        else:
            x = 0
            y += 1
        if solve_sudoku(sudoku, x, y):
            return 1
        else:
            return 0
        
    # to fill vaccant space
    if sudoku[x][y] == 0:
        # check for each num , start from 1 to 9
        while num<10:
            # same_square return 1 if no duplicate elements
            ss = same_square(sudoku,x,y,num)
            # same_raw return 1 if no duplicate elements in same raw
            sr = same_raw(sudoku,x,y,num)
            # same_column return 1 if no duplicate elements in same column
            sc = same_column(sudoku,x,y,num)

            # if all func are return 1 means no duplicated elements
            if ss and sr and sc:
                # add values to the vaccant slot
                sudoku[x][y] = num

                #back tracking algorithm
                if x == 8 and y == 8 :
                    return 1
                if x < 8:
                    tx = x + 1
                else:
                    tx = 0
                    ty = y + 1
                if solve_sudoku(sudoku,tx,ty):
                    return 1
            tx = x
            ty = y
            num += 1
        sudoku[x][y] = 0
        return 0        