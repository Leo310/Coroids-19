import sys
import pygame

import eventhandler
import statehandler
import player

pygame.init()
clock = pygame.time.Clock()

width, height = (1300, 750)
screen = pygame.display.set_mode((width, height))


def quit_game():
    pygame.quit()
    sys.exit(0)


p1 = player.Player()

eventhandler.register(quit_game, pygame.QUIT)
statehandler.register(p1.move, statehandler.KEYPRESSED,
                      key=pygame.K_UP, vel=-1)
statehandler.register(p1.move, statehandler.KEYPRESSED,
                      key=pygame.K_DOWN, vel=1)
statehandler.register(p1.rotate, statehandler.KEYPRESSED,
                      key=pygame.K_LEFT, angle=-1)
statehandler.register(p1.rotate, statehandler.KEYPRESSED,
                      key=pygame.K_RIGHT, angle=1)

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        eventhandler.call_registered(event)

    statehandler.update_registered()

    screen.fill("#121212")
    p1.draw(screen)
    pygame.display.flip()
