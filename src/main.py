import sys
import pygame

import eventhandler

pygame.init()
clock = pygame.time.Clock()

(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


@eventhandler.register(pygame.QUIT)
def quit_game():
    pygame.quit()
    sys.exit(0)


RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        eventhandler.call_registered(event.type)
