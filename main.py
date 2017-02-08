import os # system("clean")
import random # randrange

'''
1 2 3   1, 2, 3 - first raw, etc.
4 5 6   1, 4, 7 - first column, etc.
7 8 9   1, 5, 9 - left-to-right diagonal, 3, 5, 7 - right-to-left diagonal
'''

class UsedFieldError(Exception):
    pass

class gameOver(Exception):
    def __init__(self, winner):
        global player_char

        if winner == player_char:
            self.message = "You won!"
        else:
            self.message = "You lost :(" 

matrix = [[str(i + 1 + (j * 3)) for i in range(3)] for j in range(3)]
# gameOver = False

os.system("clear")

print("Hello in Tic Tac Toe Game!")
player_char = input("Enter your charachter you want (X/O): ")
comp_char = list(filter(lambda char: char != player_char, ['X', 'O']))[0]

def Draw():
    os.system("clear")

    for raw in matrix:
        for num in raw:
            print(num, end=' ')
        print()

def Input():
    while True:
        user_input = int(input("Enter the number of the field: "))

        raw = (user_input - 1) // 3
        col = (user_input - 1) % 3

        try:
            if matrix[raw][col] == 'O' or matrix[raw][col] == 'X':
                raise UsedFieldError
        except UsedFieldError:
            print("This field already used! Try another field")
        else:
            matrix[raw][col] = player_char
            break

def Logic():
    while True:
        raw, col = [random.randrange(0, 3) for i in range(2)]

        try:
            if matrix[raw][col] == 'O' or matrix[raw][col] == 'X':
                raise UsedFieldError
        except UsedFieldError:
            continue
        else:
            matrix[raw][col] = comp_char
            break

def Win():
    # global gameOver
    # global matrix_zones

    '''
    matrix_zones = [matrix[0],                                  # first raw
                    matrix[1],                                  # second raw
                    matrix[2],                                  # third raw
                    [i[0] for i in matrix],                     # first column
                    [i[1] for i in matrix],                     # second column
                    [i[2] for i in matrix],                     # third column
                    [matrix[i][i] for i in range(3)],           # left-to-right diagonal
                    [matrix[0][2], matrix[1][1], matrix[2][0]]] # right-to-left diagonal

    print(matrix_zones)

    try:
        winner = list(filter(lambda *args: args[0] == args[1] == args[2], matrix_zones))
        print(winner)

        if winner:
            if winner == player_char:
                print("You won!")
            else:
                print("You lost :(")

            # gameOver = True
    except IndexError:
        print("IndexError")
    '''
    
    if matrix[0][0] == matrix[0][1] == matrix[0][2]:
        raise gameOver(matrix[0][0])
    elif matrix[1][0] == matrix[1][1] == matrix[1][2]:
        raise gameOver(matrix[1][0])
    elif matrix[2][0] == matrix[2][1] == matrix[2][2]:
        raise gameOver(matrix[2][0])
    elif matrix[0][0] == matrix[1][0] == matrix[2][0]:
        raise gameOver(matrix[0][0])
    elif matrix[0][1] == matrix[1][1] == matrix[2][1]:
        raise gameOver(matrix[0][1])
    elif matrix[0][2] == matrix[1][2] == matrix[2][2]:
        raise gameOver(matrix[0][2])
    elif matrix[0][0] == matrix[1][1] == matrix[2][2]:
        raise gameOver(matrix[0][0])
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        raise gameOver(matrix[0][2])

try:
    Draw()

    while True:
        Input()
        Draw()
        Win()
        Logic()
        Draw()
        Win()
except gameOver as g:
    print(g.message)