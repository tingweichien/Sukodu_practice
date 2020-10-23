#Reference :https://www.youtube.com/watch?v=4_9twnEduFA&ab_channel=TechWithTim

import pygame

class button():
    """
    :x is the left top corner x position
    :y is the left top corner y position

    """
    def __init__(self, color, x, y, width, height, text='', textcolor=(0,0,0), textsize = 30):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textcolor = textcolor
        self.textsize = textsize

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.textsize)
            text = font.render(self.text, 1, self.textcolor)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def getFocus(self, pos, orgColor = None, changedColor = None, otherCondition = True):
        if changedColor is None or orgColor is None:
            print("No color changed")
        else:
            if self.isOver(pos) and otherCondition:
                self.color = changedColor
            else :
                self.color = orgColor