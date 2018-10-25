import pygame
import sys
from pygame.locals import *


def car_load(path):
    car_image = pygame.image.load(path)
    car = pygame.transform.scale(car_image, (20, 20))
    car_rect = car.get_rect()

    return car, car_rect


def car_control(event, speed):
    move = [0, 0]
    if event.type == KEYDOWN:
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

    return move


if __name__ == '__main__':
    screen_size = (400, 400)
    flag = True
    color_for_background = (255, 255, 255)
    car_image_path = "car.png"
    move = [0, 0]
    frame_rate = 120
    speed = 1

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("car game")
    car, car_rect = car_load(car_image_path)

    clock = pygame.time.Clock()

    while True:
        screen.fill(color_for_background)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            else:
                move = car_control(event, speed)
        car_rect = car_rect.move(move).clamp(0, 0, 400, 400)
        screen.blit(car, car_rect)
        pygame.display.update()
        clock.tick(frame_rate)
