import sys
import pygame

from config import GameConfig
from gameobject import GameObject
from player import Player


class Game(GameObject):
    def __init__(self):
        size = GameConfig.SIZE.value
        super().__init__(image_size=size, image_path="background.png", zindex=0)

        # setting game to middle pos because image need to be renderd in top right
        middle_pos = (size[0]/2, size[1]/2)
        self._pos = middle_pos

        self._game_objects.append(Player(middle_pos))

    def update(self, dt):
        # Event handling
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit(0)
