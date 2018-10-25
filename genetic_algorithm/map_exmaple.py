import pygame
import sys
from pygame.locals import *

screen_size = (400, 400)
flag = True
color_for_background = (255, 255, 255)
color_for_lines = (0, 0, 0)
width_lines = 3
lines_left = [(170, 400),
              (170, 330),
              (50, 330),
              (50, 170),
              (290, 170),
              (290, 130),
              (170, 130),
              (170, 0)]
lines_right = [(230, 400),
               (230, 270),
               (110, 270),
               (110, 230),
               (350, 230),
               (350, 70),
               (230, 70),
               (230, 0)]

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("car game")

while flag:
    screen.fill(color_for_background)
    pygame.draw.lines(screen,
                      color_for_lines,
                      False,
                      lines_left,
                      width_lines)
    pygame.draw.lines(screen,
                      color_for_lines,
                      False,
                      lines_right,
                      width_lines)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit()