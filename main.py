# Python Practice, thanks to Tech with Tim YouTube channel
#ALGORTHIM USED BACKTRACKING
# INPUT THE NUMBERS

#CREATE A BOARD AS A NESTED LIST , EMPTY SQUAARES = 0


import time

def solve(bo):
    global counter
    counter+=1
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


# ------FIND IF THE CURRENT BOARD IS VALID-------

def valid(bo, num, pos): # TAKE 3 PARAMETER BOARD, NUMBER AND POSITION
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

#SHAPING THE BOARD INTO DIFFERENT SECTIONS
def print_board(bo):
#SEPERATING BOARD INTO DIFFERENT SECTIONS
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
#GETTING THE LENGTH OF DIFFERENT ROWS
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
#PRINTING THE NUMBER
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#FIND THE EMPTY SQUARE
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def fill_board():
    global board
    data=[]
    number = 81
    for i in range(number):
        a = int(input())
        data.append(a)
    board = [data[x:x+9] for x in range(0, len(data), 9)]


print ('Welcome to Sudoku solver developed in Python, please enter the row-wise numbers one-by-one and press enter, if any cell is blank, enter zero.')

while True:
    fill_board()
    print_board(board)
    answer = input("Is this your Sudoku puzzle? Please type YES or NO ").upper()
    if answer == "YES":
        counter = 0
        start_time = time.time()
        solve(board)
        print("________________________________")
        print("________________________________")
        print("SEE BELOW FOR THE SOLUTION")
        print("________________________________")
        print_board(board)

        total_time = time.time() - start_time
        if total_time > 3.5:
            print("Oh that was a tough one, time taken--- %s seconds ---" % (time.time() - start_time))
            print ('Total Recursive Tries ' + str(counter))
            input('Press ENTER to exit')

        elif total_time >= 1 and total_time >= 3.5:
            print("Interesting, time taken--- %s seconds ---" % (time.time() - start_time))
            print ('Total  Recursive Tries ' + str(counter))
            input('Press ENTER to exit')

        else :
            print("Piece of cake, time taken--- %s seconds ---" % (time.time() - start_time))
            print ('Total Recursive Tries ' + str(counter))
            input('Press ENTER to exit')

        break

    elif answer == "NO":
       print("Please fill the board again.")
       continue
    else:
       print("Sorry your answer is not recognised. Restart the program and make sure you answer with the word Yes or the word No.")
