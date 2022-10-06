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
        super().__init__(image_size=size,
                         images_path=["assets/background.png"])
        self._layer = 0
        # setting game to middle pos because image need to be renderd in top right
        middle_pos = (size[0]/2, size[1]/2)
        self.rect.center = middle_pos

        self.groups["enemies"] = pygame.sprite.Group()
        self.groups["player"] = pygame.sprite.Group()

        self.groups["player"].add(Player(middle_pos))

    def __spawn_enemies(self):
        size = GameConfig.SIZE.value
        if len(self.groups["enemies"]) < 8:
            # left
            self.groups["enemies"].add(
                Enemy((-100, random.randint(0, size[1]))))
            # top
            self.groups["enemies"].add(
                Enemy((random.randint(0, size[0]), -100)))
            # right
            self.groups["enemies"].add(
                Enemy((size[0]+100, random.randint(0, size[1]))))
            # bottom
            self.groups["enemies"].add(
                Enemy((random.randint(0, size[0]), size[1] + 100)))

    def __enemies_follow_player(self):
        for player in self.groups["player"].sprites():
            for enemy in self.groups["enemies"].sprites():
                enemy.direction = player.pos - enemy.pos
                enemy.direction = enemy.direction.normalize()

    def __projetile_enemy_collision(self):
        for player in self.groups["player"].sprites():
            collisions = pygame.sprite.groupcollide(
                player.groups["projectiles"], self.groups["enemies"], False, False)
            for sprite1, sprites2 in collisions.items():
                sprite1.hit()
                for sprite2 in sprites2:
                    sprite2.hit()

    def __player_enemy_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.groups["player"], self.groups["enemies"], False, False,
            collided=pygame.sprite.collide_circle)
        for sprite1, _ in collisions.items():
            sprite1.hit()

    def __handle_events(self):
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit(0)

    def update(self, dt):
        self.__handle_events()
        self.__spawn_enemies()
        self.__enemies_follow_player()
        self.__projetile_enemy_collision()
        self.__player_enemy_collision()
