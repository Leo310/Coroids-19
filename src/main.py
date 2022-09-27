import pygame
from player import Player
from game import Game

# could make them variable if we dynamically need to change them
PLAYER_SPEED = 300
PROJECTILE_SPEED = 900
PLAYER_ROTATION_SPEED = 120


def main():
    pygame.init()

    clock = pygame.time.Clock()

    size = (1300, 750)
    screen = pygame.display.set_mode(size)

    p1 = Player((500, 500), PLAYER_SPEED,
                PLAYER_ROTATION_SPEED, PROJECTILE_SPEED)
    game = Game(size, "background.png", p1)

    while True:
        dt = clock.tick() / 1000
        screen.fill("#121212")

        for gameobject in sorted(game, key=(
                lambda gameobj: gameobj.zindex)):
            gameobject.update(dt)
            gameobject.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
