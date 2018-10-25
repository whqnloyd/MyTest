import pygame
import sys
from pygame.locals import *


def map_load(size, name):
    screen_size = size
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(name)

    return screen


def maze_load(screen, color_for_lines, width_lines):
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


if __name__ == '__main__':
    color_for_background = (255, 255, 255)
    color_for_lines = (0, 0, 0)
    width_lines = 3
    size = (400, 400)
    name = "test"
    screen = map_load(size, name)

    while True:
        screen.fill(color_for_background)
        maze_load(screen, color_for_lines, width_lines)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
