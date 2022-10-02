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
        super().__init__(image_size=size, image_path="assets/background.png")
        self._layer = 0
        # setting game to middle pos because image need to be renderd in top right
        middle_pos = (size[0]/2, size[1]/2)
        self.rect.center = middle_pos

        self.groups["enemies"] = pygame.sprite.Group()
        self.groups["player"] = pygame.sprite.Group()

        for _ in range(4):
            self.groups["enemies"].add(
                Enemy((0, random.randint(0, size[1]))))
        for _ in range(4):
            self.groups["enemies"].add(
                Enemy((random.randint(0, size[0]), 0)))
        for _ in range(4):
            self.groups["enemies"].add(
                Enemy((size[0], random.randint(0, size[1]))))
        for _ in range(4):
            self.groups["enemies"].add(
                Enemy((random.randint(0, size[0]), size[1])))

        self.groups["player"].add(Player(middle_pos))

    def update(self, dt):
        # Event handling
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit(0)

        for player in self.groups["player"].sprites():
            for enemy in self.groups["enemies"].sprites():
                enemy._direction = player._pos - enemy._pos
                enemy._direction = enemy._direction.normalize()

        for player in self.groups["player"].sprites():
            pygame.sprite.groupcollide(
                player.groups["projectiles"], self.groups["enemies"], True, True)

        pygame.sprite.groupcollide(
            self.groups["player"], self.groups["enemies"], True, False,
            collided=pygame.sprite.collide_circle)
