import sys
import pygame

import eventhandler
import statehandler
import player

# could make them variable if we dynamically need to change them
PLAYER_SPEED = 1
PROJECTILE_SPEED = 2
PLAYER_ROTATION = 1


def main():
    pygame.init()

    width, height = (1300, 750)
    screen = pygame.display.set_mode((width, height))
    p1 = player.Player()

    eventhandler.register(quit_game, pygame.QUIT)
    eventhandler.register(
        p1.shoot, pygame.MOUSEBUTTONDOWN, vel=PROJECTILE_SPEED)
    statehandler.register(p1.move,
                          statehandler.KEYPRESSED,
                          keys=[pygame.K_UP, pygame.K_w],
                          vel=-PLAYER_SPEED)
    statehandler.register(p1.move,
                          statehandler.KEYPRESSED,
                          keys=[pygame.K_DOWN, pygame.K_s],
                          vel=PLAYER_SPEED)
    statehandler.register(p1.rotate,
                          statehandler.KEYPRESSED,
                          keys=[pygame.K_LEFT, pygame.K_a],
                          angle=-PLAYER_ROTATION)
    statehandler.register(p1.rotate,
                          statehandler.KEYPRESSED,
                          keys=[pygame.K_RIGHT, pygame.K_d],
                          angle=PLAYER_ROTATION)

    while True:
        screen.fill("#121212")

        for event in pygame.event.get():
            eventhandler.call_registered(event)

        statehandler.update_registered()

        for projetile in p1.projectiles:
            projetile.move()
            projetile.draw(screen)

        p1.draw(screen)
        pygame.display.flip()


def quit_game():
    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
