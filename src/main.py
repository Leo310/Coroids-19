import pygame
from config import GameConfig
from game import Game


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(GameConfig.SIZE.value)

    game = Game()

    while True:
        dt = clock.tick() / 1000

        for gameobject in sorted(game, key=(
                lambda gameobj: gameobj.zindex)):
            gameobject.update(dt)
            gameobject.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
