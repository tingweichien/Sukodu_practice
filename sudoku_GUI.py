import pygame
from index import *

#\ initialize the pygame
pygame.init()

#\ screen
screen = pygame.display.set_mode((FrameX, FrameY))
pygame.display.set_caption("Sudoku")

#\ canvas
bar_percentage = 0.1
bar_canvas = pygame.Surface((FrameX, FrameY * bar_percentage))
bar_canvas = bar_canvas.convert()
bar_canvas.fill((255,255,255))

body_percentage = 1 - bar_percentage
body_canvas = pygame.Surface((FrameX, FrameY * body_percentage))
body_canvas = body_canvas.convert()
body_canvas.fill((0,0,0))

#\ block
gap = 5
blockX = FrameX/9 - gap
blockY = FrameX/9 - gap
for row in range(9):
    for col in range(9):
       pygame.draw.rect(body_canvas, (255,255,255), [row * blockX + gap, col * blockY + gap, blockX, blockY], 4)


#\ time
clock = pygame.time.Clock()

#\ close the pygame
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)


    #\ display
    screen.blit(bar_canvas, (0, 0))
    screen.blit(body_canvas, (0, FrameY * bar_percentage))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
