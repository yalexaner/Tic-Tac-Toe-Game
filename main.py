import os # system("clean")
import random # randrange

class UsedFieldError(Exception):
    pass

matrix = [[i + 1 + (j * 3) for i in range(3)] for j in range(3)]
gameOver = False

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
    global gameOver

    '''
    if matrix[0][0] == matrix[0][1] == matrix[0][2] or matrix[1][0] == matrix[1][1] == matrix[1][2] or\
       matrix[2][0] == matrix[2][1] == matrix[2][2] or matrix[0][0] == matrix[1][0] == matrix[2][0] or\
       matrix[0][1] == matrix[1][1] == matrix[2][1] or matrix[0][2] == matrix[1][2] == matrix[2][2] or\
       matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if matrix[0][0] == player_char:
            print("You won!")
        else:
            print("You lost :(")
    '''

    if matrix[0][0] == matrix[0][1] == matrix[0][2]:
        if matrix[0][0] == player_char:
            print("You won!")
        else:
            print("You lost :(")

        gameOver = True
    elif matrix[1][0] == matrix[1][1] == matrix[1][2]:
        if matrix[1][0] == player_char:
            print("You won!")
        else:
            print("You lost :(")

        gameOver = True
    elif matrix[2][0] == matrix[2][1] == matrix[2][2]:
        if matrix[2][0] == player_char:
            print("You won!")
        else:
            print("You lost :(")

        gameOver = True
    elif matrix[0][0] == matrix[1][0] == matrix[2][0]:
        if matrix[0][0] == player_char:
            print("You won!")
        else:
            print("You lost :(")

        gameOver = True
    elif matrix[0][1] == matrix[1][1] == matrix[2][1]:
        if matrix[0][1] == player_char:
            print("You won!")
        else:
            print("You lost :(")

        gameOver = True
    elif matrix[0][2] == matrix[1][2] == matrix[2][2]:
        if matrix[0][2] == player_char:
            print("You won!")
        else:
            print("You lost :(")

        gameOver = True
    elif matrix[0][0] == matrix[1][1] == matrix[2][2]:
        if matrix[0][0] == player_char:
            print("You won!")
        else:
            print("You lost :(")

        gameOver = True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if matrix[0][2] == player_char:
            print("You won!")
        else:
            print("You lost :(")

        gameOver = True

Draw()

while not gameOver:
    Input()
    Logic()
    Draw()
    Win()