import os
import sys

import pygame

from config import GameConfig
from game import Game
from menu import Menu
from death_screen import Deathscreen


def main():
    os.chdir(os.path.dirname(sys.argv[0]))

    pygame.init()
    screen = pygame.display.set_mode(GameConfig.SIZE.value)
    pygame.mixer.music.load("assets/sounds/background.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

    while True:
        menu = Menu(screen)
        difficulty = menu.loop()

        game = Game(screen, difficulty)
        game.loop()

        death_screen = Deathscreen(screen)
        death_screen.loop()


if __name__ == "__main__":
    main()
