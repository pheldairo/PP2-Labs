import pygame
import sys
from pygame.locals import *
import time

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1400, 1050
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Часы")

clock_background = pygame.image.load("mainclock.png")
second_hand = pygame.image.load("rightarm.png")
minute_hand = pygame.image.load("leftarm.png")

clock_center_x = WINDOW_WIDTH // 2
clock_center_y = WINDOW_HEIGHT // 2

minute_hand_angle = 0
second_hand_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_hand_angle = -(minutes * 6)
    second_hand_angle = -(seconds * 6)

    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_hand_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_hand_angle)

    minute_hand_rect = rotated_minute_hand.get_rect(center=(clock_center_x, clock_center_y))
    second_hand_rect = rotated_second_hand.get_rect(center=(clock_center_x, clock_center_y))

    screen.blit(clock_background, (0, 0))
    screen.blit(rotated_minute_hand, minute_hand_rect)
    screen.blit(rotated_second_hand, second_hand_rect)

    pygame.display.flip()
    pygame.time.delay(1000) 
