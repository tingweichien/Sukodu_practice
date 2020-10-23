import copy


#\ color
Cyan = (0,255,255)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)
Green2 = (0,200,0)
White = (255,255,255)
Black = (0,0,0)
Grey = (100,100,100)
Grey2 = (150,150,150)
Grey3 = (200,200,200)
Grey4 = (240,240,240)
Yellow = (255,255,0)
Magenta = (255,0,255)


#\ the quertion board
#\ default
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

BOARD2 = [
        [2,0,9,7,0,0,5,0,0],
        [0,0,4,0,9,0,1,0,0],
        [0,8,0,0,3,0,4,7,0],
        [0,2,6,0,0,1,3,0,5],
        [0,5,0,0,0,0,0,2,0],
        [4,0,3,0,5,0,0,9,1],
        [0,0,7,0,0,3,0,5,0],
        [3,0,2,0,1,5,0,8,7],
        [5,0,8,4,2,7,9,0,0]
    ]

BOARD3 = [
        [0,8,0,0,0,0,0,7,2],
        [2,5,0,0,0,4,0,0,1],
        [0,1,0,0,0,0,5,4,9],
        [5,0,1,3,0,7,0,0,0],
        [0,7,0,0,0,0,0,1,5],
        [4,2,0,1,0,8,0,0,0],
        [0,0,0,0,0,0,0,9,6],
        [0,0,0,0,6,9,0,0,7],
        [1,0,0,0,0,0,2,8,0]
]

#\ Board group
BOARDList = [BOARD, BOARD2, BOARD3]


#\ caption
caption = "Sudoku"


#\ frame size
FrameX = 400
FrameY = 500


#\ bar and body size percentage
bar_percentage = 0.1
body_percentage = 1 - bar_percentage


#\bar and body size
bar_canvas_X = FrameX
bar_canvas_Y = FrameY * bar_percentage
body_canvas_X = FrameX
body_canvas_Y = FrameY * body_percentage

#\ bar and bosy color
bar_canvas_color = White
body_canvas_color = Black


#\ length between each block
# pls set in even number
gap = 4


#\ the number to guess, must in sqrt (int) 1 4 9 16 25 36 ......
#\ 9 --> 1~9 to imput
Num_To_Guess = 9


#\ set the boundary
boundaryLength = gap
boundaryNum = 2
blockLenghtX = (body_canvas_X - gap - boundaryLength * boundaryNum) / Num_To_Guess - gap
blockLenghtY = (body_canvas_Y - gap - boundaryLength * boundaryNum) / Num_To_Guess - gap



#\ Button text size
button_text_size = 20


#\ Button deactive
button_deactivecolor = Grey4


#\ Start Button
start_buttonW = 50
start_buttonH = 30
start_button_positionX = bar_canvas_X*0.25/9
start_button_positionY = bar_canvas_Y/4
start_button_Color = Black
start_button_TextColor = White
start_button_HoverColor = Blue
start_button_outlineColor = Grey2


#\ Stop Button
stop_buttonW = 50
stop_buttonH = 30
stop_button_positionX = bar_canvas_X*1.5/9
stop_button_positionY = bar_canvas_Y/4
stop_button_Color = Black
stop_button_TextColor = White
stop_button_HoverColor = Blue
stop_button_outlineColor = Grey2


#\ end Button
end_buttonW = 50
end_buttonH = 30
end_button_positionX = bar_canvas_X*2.75/9
end_button_positionY = bar_canvas_Y/4
end_button_Color = Black
end_button_TextColor = White
end_button_HoverColor = Blue
end_button_outlineColor = Grey2


#\ auto solving Button
auto_solver_buttonW = 50
auto_solver_buttonH = 30
auto_solver_button_positionX = bar_canvas_X*4/9
auto_solver_button_positionY = bar_canvas_Y/4
auto_solver_button_Color = Black
auto_solver_button_TextColor = White
auto_solver_button_HoverColor = Blue
auto_solver_button_outlineColor = Grey2




#\ timer
timer_positionX = bar_canvas_X*7/9
timer_positionY = bar_canvas_Y/8
timer_InitColor = Grey3
timer_finishedColor = Green
timer_Color = Black
timer_stopColor = Grey2
