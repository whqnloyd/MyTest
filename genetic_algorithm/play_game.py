import pygame
import sys
from pygame.locals import *
import car_lib
import map_lib

color_for_background = (255, 255, 255)
color_for_lines = (0, 0, 0)
width_lines = 3
screen_size = (400, 400)
name = "test"
screen = map_lib.map_load(screen_size, name)

car_image_path = "car.png"
move = [0, 0]
frame_rate = 120
speed = 1
car, car_rect = car_lib.car_load(car_image_path)

clock = pygame.time.Clock()

while True:
    screen.fill(color_for_background)
    map_lib.maze_load(screen, color_for_lines, width_lines)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            move = car_lib.car_control(event, speed)
    car_rect = car_rect.move(move).clamp(0, 0, 400, 400)
    screen.blit(car, car_rect)
    pygame.display.update()
    clock.tick(frame_rate)
