import sys
import pygame
from gameobject import GameObject


class Game(GameObject):
    def __init__(self, size, background, player, zindex=0):
        super().__init__(image_size=size, image_path=background, zindex=zindex)
        # because we place image in center of pos
        self._pos = (size[0]/2, size[1]/2)
        self._game_objects.append(player)

    def update(self, dt):
        # Event handling
        if pygame.event.get(pygame.QUIT):
            quit_game()


def quit_game():
    pygame.quit()
    sys.exit(0)
