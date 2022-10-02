import os
import sys
import pygame
from config import GameConfig
from game import Game


def main():
    os.chdir(os.path.dirname(sys.argv[0]))

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(GameConfig.SIZE.value)

    game = Game()
    root_group = pygame.sprite.LayeredUpdates()
    root_group.add(game)

    while True:
        dt = clock.tick() / 1000
        screen.fill((0, 0, 0))  # Clear the screen each frame.

        for group in game.get_groups():
            root_group.add(group.sprites())

        root_group.update(dt)
        root_group.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
