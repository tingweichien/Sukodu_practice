## This is the sudoku solver

import time
import Index
import pygame

# global var
gCount = 0


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
def FindEmpty(bo : list) -> tuple:
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
def solve ( bo : list,
            GUI_display : bool = False,
            body_canvas :object = None,
            RectList : list = None,
            myfont : object = None,
            clock : object = None,
            screen : object = None,
            bar_canvas : object = None,
            skip_all_print : bool = False
            ) -> bool:


    # for printing the board
    global gCount
    print(f"iteration = {gCount}")
    gCount += 1
    if not GUI_display and not skip_all_print:
        print_board(bo)
        time.sleep(0.25)

    # find the empty space
    find = FindEmpty(bo)
    if not find :
        return True
    else:
        (row, col) = find




    for num in range(1,10):
        #\ display on the GUI

        #\ recursive content
        if valid(bo, num, find):
            bo[row][col] = num

            #\ bar and body canvas
            if GUI_display:
                time.sleep(0.1)
                screen.blit(bar_canvas, (0, 0))
                screen.blit(body_canvas, (0, Index.FrameY * Index.bar_percentage))
                InputTextRect = RectList[col*9+row]
                pygame.draw.rect(body_canvas,
                                Index.White,
                                InputTextRect,
                                0
                                )
                text_surface = myfont.render(str(bo[row][col]), True, Index.Green2)
                body_canvas.blit(text_surface, (InputTextRect.x + Index.blockLenghtX/4, InputTextRect.y))
                pygame.display.flip()
                clock.tick(60)

            # not find
            if solve(bo, GUI_display, body_canvas, RectList, myfont, clock, screen, bar_canvas, skip_all_print):
                return True

            # if no num is valid then solve will return False which makes the recurrsive go back to the previous one to reset and redo
            else:
                bo[find[0]][find[1]] = 0
                if GUI_display:
                    time.sleep(0.1)
                    screen.blit(bar_canvas, (0, 0))
                    screen.blit(body_canvas, (0, Index.FrameY * Index.bar_percentage))
                    InputTextRect = RectList[col*9+row]
                    pygame.draw.rect(body_canvas,
                                    Index.Red,
                                    InputTextRect,
                                    0
                                    )
                    pygame.display.flip()
                    clock.tick(60)

    return False



#\ main
if __name__ == "__main__":
    print_board(Index.BOARD)
    solve(Index.BOARD)
    print("\n################## ANSWER ####################\n")
    print_board(Index.BOARD)