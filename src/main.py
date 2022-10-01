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

    while True:
        dt = clock.tick() / 1000
        screen.fill((0, 0, 0))  # Clear the screen each frame.

        for gameobject in sorted(game.get_all_game_objects(), key=(
                lambda gameobj: gameobj.zindex)):
            gameobject.update(dt)
            gameobject.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
