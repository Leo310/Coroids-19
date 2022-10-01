import sys
import random

import pygame

from config import GameConfig
from gameobject import GameObject
from player import Player
from enemy import Enemy


class Game(GameObject):
    def __init__(self):
        size = GameConfig.SIZE.value
        super().__init__(image_size=size, image_path="assets/background.png", zindex=0)
        # setting game to middle pos because image need to be renderd in top right
        middle_pos = (size[0]/2, size[1]/2)
        self._pos = middle_pos

        self.game_objects["enemies"] = []
        self.game_objects["player"] = []

        for _ in range(4):
            self.game_objects["enemies"].append(
                Enemy((0, random.randint(0, size[1]))))
        for _ in range(4):
            self.game_objects["enemies"].append(
                Enemy((random.randint(0, size[0]), 0)))
        for _ in range(4):
            self.game_objects["enemies"].append(
                Enemy((size[0], random.randint(0, size[1]))))
        for _ in range(4):
            self.game_objects["enemies"].append(
                Enemy((random.randint(0, size[0]), size[1])))

        self.game_objects["player"].append(Player(middle_pos))

    def update(self, dt):
        # Event handling
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit(0)

        for player in self.game_objects["player"]:
            for enemy in self.game_objects["enemies"]:
                enemy._direction = player._pos - enemy._pos
                enemy._direction = enemy._direction.normalize()

        for player in self.game_objects["player"]:
            for projectile in list(player.game_objects["projectiles"]):
                for enemy in list(self.game_objects["enemies"]):
                    if projectile.is_colliding(enemy):
                        player.game_objects["projectiles"].remove(
                            projectile)
                        self.game_objects["enemies"].remove(enemy)

        for player in list(self.game_objects["player"]):
            for enemy in self.game_objects["enemies"]:
                if enemy.is_colliding(player):
                    self.game_objects["player"].remove(player)
