import numpy as np
import random 
import time
def hello():
    print ('Hello, let\'s play Tic Tac Toe!')

#Initializes array grid
arr = np.array([[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']])


#Prints example grid with positions
def print_grid_example():
    arr1 = [[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]
    arr1[0][1] = 1
    arr1[0][5] = 2
    arr1[0][9] = 3
    arr1[2][1] = 4
    arr1[2][5] = 5
    arr1[2][9] = 6
    arr1[4][1] = 7
    arr1[4][5] = 8
    arr1[4][9] = 9
    for row in arr1:
        print(' '.join([str(elem) for elem in row]))

#Updates grid
def update_grid(j,k,type):
    if(type == 'player'):
        arr[j][k] = 'x'
    else:
        arr[j][k] = '0'
    print_grid()

#Prints grid       
def print_grid():
    for row in arr:
        print(' '.join([str(elem) for elem in row]))

#Checks rows
def check_row():
    for row in arr:
        if (row[1] == 'x')*(row[5] == 'x')*(row[9] == 'x'):
            print ('You won!')
            return True
        elif (row[1] == '0')*(row[5] == '0')*(row[9] == '0'):
            print ('You lost!')
            return True

#Checks columns           
def check_column():
    for col in arr.T:
        if (col[0] == 'x')*(col[2] == 'x')*(col[4] == 'x'):
            print ('You won!')
            return True
        elif (col[0] == '0')*(col[2] == '0')*(col[4] == '0'):
            print ('You lost!')
            return True

#Checks diagonally
def check_diagonally():
    if (arr[0][1] == 'x')*(arr[2][5] == 'x')*(arr[4][9] == 'x')+(arr[0][9] == 'x')*(arr[2][5] == 'x')*(arr[4][1] == 'x'):
        print ('You won!')
        return True
    elif (arr[0][1] == '0')*(arr[2][5] == '0')*(arr[4][9] == '0')+(arr[0][9] == '0')*(arr[2][5] == '0')*(arr[4][1] == '0'):
        print ('You lost!')
        return True

input_list = []
def user_input():
    while True:
        user = input('Please enter your position: ')
        if user not in input_list:
            position(user,'player')
            input_list.append(user)
            break
        else:
            print('This position has already been used.')
    return user



def computer_input():
    while True:
        computer = random.randint(1,9)
        if computer not in input_list:
            print('\nComputer position is: ' + str(computer))
            position(computer,'comp')
            input_list.append(computer)
            break
    return computer

#Takes input from user
def turn():
    print ('\nPlease put your mark by entering position on the grid as shown in example above.')
    while (check_row() != True)*(check_diagonally() != True)*(check_column() != True):
        user_input()
        if (check_row() == True)*(check_diagonally() == True)*(check_column() == True):
            break
        computer_input()


def position(x,type):
    if (x != 'x')*(x != '0'):
        if (x == 1 and arr[0][1] == ' '):
            update_grid(0,1,type)
        elif (x == 2 and arr[0][5] == ' '):
            update_grid(0,5,type)
        elif (x == 3 and arr[0][9] == ' '):
            update_grid(0,9,type)
        elif (x == 4 and arr[2][1] == ' '):
            update_grid(2,1,type)
        elif (x == 5 and arr[2][5] == ' '):
            update_grid(2,5,type)
        elif (x == 6 and arr[2][9] == ' '):
            update_grid(2,9,type)
        elif (x == 7 and arr[4][1] == ' '):
            update_grid(4,1,type)
        elif (x == 8 and arr[4][5] == ' '):
            update_grid(4,5,type)
        elif (x == 9 and arr[4][9] == ' '):
            update_grid(4,9,type)
    else:
        print('Position is taken. Please enter different')



hello()
print_grid_example()
turn()

