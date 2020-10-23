#\ timer reference  : https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame
#\ button reference : https://www.youtube.com/watch?v=4_9twnEduFA&ab_channel=TechWithTim
#\ text input       : https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame
#\                  : https://www.youtube.com/watch?v=Rvcyf4HsWiw&ab_channel=ClearCode

import pygame
import Index
from sudoku_solving import *
import math
from Button import button
from tkinter import *
from tkinter import messagebox
import copy
from random import randint


#\ initialize the pygame
pygame.init()
pygame.font.init()


#\ screen
screen = pygame.display.set_mode((Index.FrameX, Index.FrameY))
pygame.display.set_caption(Index.caption)


#\ font
myfont = pygame.font.SysFont('Comic Sans MS', 30)
TextInput = ""


#\ time
clock = pygame.time.Clock()


#\ default Board
defaultBoardIndex = randint(0,len(Index.BOARDList)-1)
BOARD = Index.BOARDList[defaultBoardIndex]
print(defaultBoardIndex)
Original_BOARD = copy.deepcopy(BOARD)


#\ canvas
#\ the upper bar
bar_canvas = pygame.Surface((Index.bar_canvas_X, Index.bar_canvas_Y))
bar_canvas = bar_canvas.convert()
bar_canvas.fill(Index.bar_canvas_color)


#\ the main body
body_canvas = pygame.Surface((Index.body_canvas_X, Index.body_canvas_Y))
body_canvas = body_canvas.convert()
body_canvas.fill(Index.body_canvas_color)


#\ block
# set the boundary
boundaryX = 0
boundaryY = 0


# block draw
RectList = []
textsurface = [[None for i in range(Index.Num_To_Guess)] for j in range(Index.Num_To_Guess)]
for row in range(Index.Num_To_Guess):

    # add the boundary
    boundaryY = 0
    if row != 0 and row%math.sqrt(Index.Num_To_Guess) == 0:
        boundaryX += Index.boundaryLength

    for col in range(Index.Num_To_Guess):

        # add the boundary
        if col != 0 and col%math.sqrt(Index.Num_To_Guess) == 0:
            boundaryY += Index.boundaryLength

        # adding another gap is for the first elemet
        # rect[posX, posY, Length, Width]
        RectX = Index.gap + row * (Index.blockLenghtX + Index.gap) + boundaryX
        RectY = Index.gap + col * (Index.blockLenghtY + Index.gap) + boundaryY
        RectObj = pygame.Rect(RectX, RectY, Index.blockLenghtX, Index.blockLenghtY)
        RectList.append(RectObj)
        pygame.draw.rect(body_canvas,
                        Index.White,
                        RectObj,
                        0
                        )

        # text for the problem
        if Original_BOARD[col][row] != 0:
            textsurface[col][row] = myfont.render(str(Original_BOARD[col][row]), False, Index.Black)
            body_canvas.blit(textsurface[col][row], (RectX + Index.blockLenghtX/4, RectY))
        else:
            textsurface[col][row] = myfont.render("", False, Index.White)


#\ bar
# start button
start_button = button(Index.start_button_Color,
                        Index.start_button_positionX,
                        Index.start_button_positionY,
                        Index.start_buttonW,
                        Index.start_buttonH,
                        "START",
                        Index.start_button_TextColor,
                        Index.button_text_size
                    )

# end button
end_button = button(Index.end_button_Color,
                        Index.end_button_positionX,
                        Index.end_button_positionY,
                        Index.end_buttonW,
                        Index.end_buttonH,
                        "END",
                        Index.end_button_TextColor,
                        Index.button_text_size
                    )


# stop button
stop_button = button(Index.stop_button_Color,
                        Index.stop_button_positionX,
                        Index.stop_button_positionY,
                        Index.stop_buttonW,
                        Index.stop_buttonH,
                        "STOP",
                        Index.stop_button_TextColor,
                        Index.button_text_size
                    )


# AutoSolver button
auto_solver_button = button(Index.auto_solver_button_Color,
                        Index.auto_solver_button_positionX,
                        Index.auto_solver_button_positionY,
                        Index.auto_solver_buttonW,
                        Index.auto_solver_buttonH,
                        "AUTO",
                        Index.auto_solver_button_TextColor,
                        Index.button_text_size
                    )




# timer
#TIMERSTART = pygame.USEREVENT + 0
#pygame.time.set_timer(TIMERSTART, 1000)
MIN = "00"
SEC = "00"
temp_time = 0
start_ticks = 0
timecounter = 0
seconds = 0
timertempColor = Index.timer_InitColor


#\ --pygame mainloop--
crashed = False
previousRect = None
changed = False
TypeState = False
INSERET_POSITION = None
InputTextRect = None
InputTextCnt = None
InputpreviousRect = None
TextList = [["" for i in range(Index.Num_To_Guess)] for j in range(Index.Num_To_Guess)] # !! Important !! The only way to create specific 2D lists
start_button_active = True
timer_continue = False
end_condition = False
auto_solver_active = False
tmpBOARD = []
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            break

        # if event.type == TIMERSTART and start_button_active is False:
        #     timecounter += 1


        if event.type == pygame.MOUSEBUTTONDOWN :
            INSERT_POSITION = event.pos
            # mouse right click
            if event.button == 3:
                print("hint")

            # mouse left click
            if event.button == 1:
                #\ start button
                if start_button.isOver(INSERT_POSITION):
                    if start_button_active:
                        start_ticks = pygame.time.get_ticks() if not timer_continue else pygame.time.get_ticks() - temp_time*1000
                        print(f"temp time: {temp_time}")
                        print("start") if not timer_continue else print("continue")
                        start_button_active = False
                        end_condition = False


                #\ end button
                if end_button.isOver(INSERT_POSITION):
                    if not start_button_active or timer_continue:
                        print("end")
                        start_button_active = True
                        end_condition = True
                        timer_continue = False


                #\ stop button
                if stop_button.isOver(INSERT_POSITION):
                    if not start_button_active:
                        temp_time = seconds
                        print("stop")
                        start_button_active = True
                        timer_continue = True


                #\ auto solving button
                if auto_solver_button.isOver(INSERT_POSITION):
                    if  start_button_active:
                        print("auto solver")
                        start_button_active = False
                        end_condition = False
                        auto_solver_active = True


                #\ mouse click the answer sheet block
                for cnt, rect in enumerate(RectList):
                    if rect.collidepoint((INSERT_POSITION[0], INSERT_POSITION[1] - Index.bar_canvas_Y)) and Original_BOARD[cnt%9][cnt//9] == 0 and not start_button_active:
                        TypeState = True
                        InputTextRect = rect
                        InputTextCnt = cnt
                        pygame.draw.rect(body_canvas,
                                        Index.Green,
                                        rect,
                                        0
                                        )
                        break

                    # when click on the non-block place
                    else:
                        TypeState = False


        #\ input typing text
        elif event.type == pygame.KEYDOWN:
            if TypeState:
                if event.key == pygame.K_BACKSPACE:
                    TextInput = TextInput[:-1]
                else:
                    TextInput += event.unicode
                    # TextInput = TextInput[:TextMaxLength]# limit the length of input
                # add to the BOARD
                BOARD[InputTextCnt%9][InputTextCnt//9] = TextInput if TextInput != "" else 0
                TextList[InputTextCnt%9][InputTextCnt//9] = TextInput
                TextInput = ""


        #\ changing the color when mouse moving on the block that can be inserted
        elif event.type == pygame.MOUSEMOTION:
            POSITION = event.pos

            #\ start button change color when mouse hovering on it
            start_button.getFocus(POSITION, Index.start_button_Color, Index.start_button_HoverColor, start_button_active)

            #\ end button change color when mouse hovering on it
            end_button.getFocus(POSITION, Index.end_button_Color, Index.end_button_HoverColor, (not start_button_active or timer_continue))

            #\ stop button change color when mouse hovering on it
            stop_button.getFocus(POSITION, Index.stop_button_Color, Index.stop_button_HoverColor, (not start_button_active))

            #\ auto solving button change color when mouse hovering on it
            auto_solver_button.getFocus(POSITION, Index.auto_solver_button_Color, Index.auto_solver_button_HoverColor, start_button_active)

            for cnt, rect in enumerate(RectList):
                if rect.collidepoint((POSITION[0], POSITION[1] - Index.bar_canvas_Y)) and BOARD[cnt%9][cnt//9] == 0:
                    pygame.draw.rect(body_canvas,
                                    Index.Cyan,
                                    rect,
                                    0
                                    )

                    if rect != previousRect and previousRect != None:
                        pygame.draw.rect(body_canvas,
                                        Index.White,
                                        previousRect,
                                        0
                                        )
                        print("mouse motion remove")
                    previousRect = rect


            #\ in the bar canvas
            if 0 < POSITION[1] < Index.bar_canvas_Y and previousRect != None:
                pygame.draw.rect(body_canvas,
                                Index.White,
                                previousRect,
                                0
                                )


        #\ outside the windows
        elif event.type == pygame.ACTIVEEVENT and previousRect != None:
            pygame.draw.rect(body_canvas,
                            Index.White,
                            previousRect,
                            0
                            )

        print(event)




    #\ --Display--
    #\ bar and body canvas
    screen.blit(bar_canvas, (0, 0))
    screen.blit(body_canvas, (0, Index.FrameY * Index.bar_percentage))

    #\ timer and button action
    # not start_button_active is True --> the start button is click and the timer start to run
    if not start_button_active and not auto_solver_active:
        bar_canvas.fill(Index.bar_canvas_color) # cover the previous drawing
        seconds = (pygame.time.get_ticks() - start_ticks)//1000
        SEC = str(seconds%60) if seconds%60 >= 10 else ("0" + str(seconds%60))
        MIN = str(seconds//60) if seconds//60 >= 10 else("0" + str(seconds//60))
        timertempColor = Index.timer_Color
        start_button.color = Index.button_deactivecolor
        auto_solver_button.color = Index.button_deactivecolor

    # stop
    if start_button_active and timer_continue:
        timertempColor = Index.timer_stopColor
        if (pygame.time.get_ticks() - seconds)%1000 < 500 :
            timertempColor = Index.timer_Color
        stop_button.color = Index.button_deactivecolor


    # end
    check_condition = False
    if end_condition:
        root = Tk()
        root.wm_withdraw() # removeto hide the main window
        MsgBox = messagebox.askquestion("Finished?", "Finish the solving Sudoku?")
        while True:
            if MsgBox == "yes":
                print("finished~")
                BOARD = [[int(col) for col in row] for row in BOARD]
                tmpBOARD = copy.deepcopy(BOARD)
                solve(BOARD, skip_all_print = True)
                check_condition = True
                TypeState = True
                end_condition = False
                timertempColor = Index.timer_finishedColor
                root.destroy()
                break
            elif MsgBox == "no":
                print("continue~")
                break

    #\ check the result after the timer stop which you click on the end button
    if check_condition:
        for i in range(len(BOARD)):
            for j in range(len(BOARD[i])):
                if Original_BOARD[i][j] == 0:
                    screen.blit(bar_canvas, (0, 0))
                    screen.blit(body_canvas, (0, Index.FrameY * Index.bar_percentage))
                    pygame.draw.rect(body_canvas,
                    Index.White,
                    RectList[j*9+i],
                    0
                    )
                    textcolor = Index.Red if tmpBOARD[i][j] != BOARD[i][j] else Index.Green
                    text_surface = myfont.render(str(BOARD[i][j]), True, textcolor)
                    body_canvas.blit(text_surface, (RectList[j*9+i].x + Index.blockLenghtX/4, RectList[j*9+i].y))
                    pygame.display.flip()
                    time.sleep(0.25)
        previousRect = None
        TypeState = False
        check_condition = False


    #\draw the clock
    bar_canvas.blit(myfont.render(f"{MIN}:{SEC}", True, timertempColor), (Index.timer_positionX, Index.timer_positionY))



    #\ init condition or another new round condition
    if start_button_active and not end_condition and not timer_continue:
        stop_button.color = Index.button_deactivecolor
        end_button.color = Index.button_deactivecolor


    #\ button draw
    start_button.draw(bar_canvas, Index.start_button_outlineColor)
    stop_button.draw(bar_canvas, Index.stop_button_outlineColor)
    end_button.draw(bar_canvas, Index.end_button_outlineColor)
    auto_solver_button.draw(bar_canvas, Index.auto_solver_button_outlineColor)


    #\ type input
    if TypeState :
        pygame.draw.rect(body_canvas,
                    Index.White,
                    InputTextRect,
                    0
                    )
        text_surface = myfont.render(TextList[InputTextCnt%9][InputTextCnt//9], True, Index.Red)
        body_canvas.blit(text_surface, (InputTextRect.x + Index.blockLenghtX/4, InputTextRect.y))


    #\ auto solver
    if auto_solver_active:
        start_button_active = True
        solve(BOARD, True, body_canvas, RectList, myfont, clock, screen, bar_canvas)
        auto_solver_active = False
        previousRect = None
        print("solved")


    pygame.display.flip()
    clock.tick(60) #refresh


pygame.quit()
