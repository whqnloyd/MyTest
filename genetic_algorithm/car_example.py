import pygame
import sys
from pygame.locals import *

screen_size = (400, 400)
flag = True
color_for_background = (255, 255, 255)
car_image_path = "car.png"
move = [0, 0]
speed = 1
frame_rate = 120

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("car game")
car_image = pygame.image.load(car_image_path)
car = pygame.transform.scale(car_image, (40, 40))
car_rect = car.get_rect()
clock = pygame.time.Clock()

while flag:
    screen.fill(color_for_background)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                move[0] = -speed
                move[1] = 0
            elif event.key == K_RIGHT:
                move[0] = speed
                move[1] = 0
            elif event.key == K_UP:
                move[1] = -speed
                move[0] = 0
            elif event.key == K_DOWN:
                move[1] = speed
                move[0] = 0
        elif event.type == KEYUP:
            move = [0, 0]

    car_rect = car_rect.move(move).clamp(0, 0, 400, 400)
    screen.blit(car, car_rect)
    pygame.display.update()
    clock.tick(frame_rate)