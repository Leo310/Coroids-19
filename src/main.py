import os
import sys

import pygame

from config import GameConfig
from game import Game
from ui import UI


def main():
    os.chdir(os.path.dirname(sys.argv[0]))

    pygame.init()
    screen = pygame.display.set_mode(GameConfig.SIZE.value)

    ui = UI(screen)
    while True:
        ui.main_menu_loop()
        game = Game(screen)
        game.loop()
        ui.death_screen_loop()


if __name__ == "__main__":
    main()
