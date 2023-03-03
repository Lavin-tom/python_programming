from random import randint
import tkinter as tk


#global variables
moves_list = []
last_scramble = []
f2l_list = []
step_move_list = []
solution_length = 0

#create a 3d list representing a solved cube
def make_cube():
    global step_move_list,f2l_list,moves_list
    step_move_list = [0,0,0,0]
    f2l_list = []
    moves_list = []
    return [   [['W', 'W', 'W'],
                ['W', 'W', 'W'],
                ['W', 'W', 'W']], #Up/white
               
               [['G', 'G', 'G'],
                ['G', 'G', 'G'],
                ['G', 'G', 'G']], #front/green
               
               [['R', 'R', 'R'],
                ['R', 'R', 'R'],
                ['R', 'R', 'R']], #right/red
               
               [['O', 'O', 'O'],
                ['O', 'O', 'O'],
                ['O', 'O', 'O']], #left/orange
               
               [['Y', 'Y', 'Y'],
                ['Y', 'Y', 'Y'],
                ['Y', 'Y', 'Y']], #down/yellow
               
               [['B', 'B', 'B'],
                ['B', 'B', 'B'],
                ['B', 'B', 'B']]] #back/blue

a = make_cube()

#print a string representation of the cube to the interpretor
def print_cube():
    print('\t\t'+str(a[5][0])+'\n\t\t'+str(a[5][1])+'\n\t\t'+str(a[5][2]))   
    print(str(a[3][0])+' '+str(a[0][0])+' '+str(a[2][0]))
    print(str(a[3][1])+' '+str(a[0][1])+' '+str(a[2][1]))   
    print(str(a[3][2])+' '+str(a[0][2])+' '+str(a[2][2]))
    print('\t\t'+str(a[1][0])+'\n\t\t'+str(a[1][1])+'\n\t\t'+str(a[1][2]))
    print('\t\t'+str(a[4][0])+'\n\t\t'+str(a[4][1])+'\n\t\t'+str(a[4][2]))


#simplifies the list of moves and returns a string representation of the moves
def get_moves():
    simplify_moves()
    s = ""
    for i in moves_list:
        s += str(i) + " "
    s = str.replace(s, "i", "'")[:-1] 
    return s

#returns a string representation of the last scramble
def get_scramble():
    s = ""
    for i in last_scramble:
        s += str(i) + " "
    s = str.replace(s, "i", "'")[:-1]
    return s