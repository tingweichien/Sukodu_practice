## This is the sudoku solver

import time

# global var
gCount = 0

#\ the quertion board
BOARD = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#\ print the board
def print_board(bo:list):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|  ", end=" ")
            print(f"{bo[i][j]}  ", end=" ")
        if (i+1) % 3 == 0 and i+1 < len(bo):
            print("\n" + "---" * 14)
        else:
            print("\n")
    print("============================================")


#\ Find the position need to insert
def FindEmpty(bo : list)->tuple:
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] is 0 : return (row, col)
    return None


#\ check if the number follow the rule that no duplicate number in row, column and square.
def valid(bo : list, num : int, pos : tuple) -> bool :
    # col and row
    if num in bo[pos[0]] or num in [col[pos[1]] for col in bo]:
        return False

    # square
    box_x = pos[0]//3
    box_y = pos[1]//3
    for row in range(3):
        for col in range(3):
            if num == bo[box_x*3 + row][box_y*3 + col]:
                return False
    # valid
    return True


#\ backtracking to solve
def solve (bo : list):

    # for printing the board
    global gCount
    print(f"iteration = {gCount}")
    gCount += 1
    print_board(bo)
    time.sleep(1)

    # find the empty space
    find = FindEmpty(bo)
    if not find :
        return True

    for num in range(1,10):
        if valid(bo, num, find):
            bo[find[0]][find[1]] = num

            # not find
            if solve(bo):
                return True

            # if no num is valid then solve will return False which makes the recurrsive go back to the previous one to reset and redo
            else:
                bo[find[0]][find[1]] = 0

    return False



#\ main
if __name__ == "__main__":
    print_board(BOARD)
    solve(BOARD)
    print("\n################## ANSWER ####################\n")
    print_board(BOARD)