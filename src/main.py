import sys
import pygame

import eventhandler
import statehandler
import player

# could make them variable if we dynamically need to change them
PLAYER_SPEED = 300
PROJECTILE_SPEED = 600
PLAYER_ROTATION = 120


def main():
    pygame.init()

    clock = pygame.time.Clock()

    width, height = (1300, 750)
    screen = pygame.display.set_mode((width, height))
    p1 = player.Player((500, 500), PLAYER_SPEED, PLAYER_ROTATION,
                       PROJECTILE_SPEED)

    eventhandler.register(quit_game, pygame.QUIT)
    eventhandler.register(p1.shoot, pygame.MOUSEBUTTONDOWN)
    statehandler.register(p1.move_up,
                          statehandler.KEYPRESSED,
                          keys=[pygame.K_UP, pygame.K_w])
    statehandler.register(p1.move_down,
                          statehandler.KEYPRESSED,
                          keys=[pygame.K_DOWN, pygame.K_s])
    statehandler.register(p1.rotate_left,
                          statehandler.KEYPRESSED,
                          keys=[pygame.K_LEFT, pygame.K_a])
    statehandler.register(p1.rotate_right,
                          statehandler.KEYPRESSED,
                          keys=[pygame.K_RIGHT, pygame.K_d])

    while True:
        dt = clock.tick(60) / 1000
        p1.vel = PLAYER_SPEED * dt
        p1.rotation_speed = PLAYER_ROTATION * dt
        p1.projectile_speed = PROJECTILE_SPEED * dt

        if p1.pos.x < 0:
            p1.pos.x = width
        elif p1.pos.x > width:
            p1.pos.x = 0
        if p1.pos.y < 0:
            p1.pos.y = height
        elif p1.pos.y > height:
            p1.pos.y = 0

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
