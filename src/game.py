import sys
import random
import time

import pygame

from config import GameConfig
from gameobject import GameObject
from player import Player
from enemy import Enemy


class Game(GameObject):
    def __init__(self, screen):
        size = GameConfig.SIZE.value
        super().__init__(image_size=size,
                         image_paths=["assets/background.png"])

        self.__screen = screen
        self._layer = 0
        # setting game to middle pos because image need to be renderd in top right
        middle_pos = (size[0]/2, size[1]/2)
        self.rect.center = middle_pos

        self.groups["enemies"] = pygame.sprite.Group()
        self.groups["player"] = pygame.sprite.Group()
        self.groups["player"].add(Player(middle_pos))

        self.__last_enemy_kill_time = 0
        self.__last_enemy_count = 0
        self.__enemy_count_diff = 0

    def __spawn_enemy(self, side):
        size = GameConfig.SIZE.value
        enemy = None
        match side:
            case 0:  # bottom
                enemy = Enemy((random.randint(0, size[0]), size[1] + 100))
            case 1:  # top
                enemy = Enemy((random.randint(0, size[0]), -100))
            case 2:  # right
                enemy = Enemy((size[0]+100, random.randint(100, size[1]-100)))
            case 3:  # left
                enemy = Enemy((-100, random.randint(100, size[1]-100)))
        self.groups["enemies"].add(enemy)

    def __spawn_enemies(self):
        enemy_count = len(self.groups["enemies"])
        self.__enemy_count_diff = enemy_count - self.__last_enemy_count
        if self.__last_enemy_count != enemy_count:
            self.__last_enemy_kill_time = time.time()
        self.__last_enemy_count = enemy_count

        if time.time() - self.__last_enemy_kill_time >= 3:
            self.__spawn_enemy(random.randint(2, 3))

        if enemy_count < 8:
            self.__spawn_enemy(random.randint(2, 3))

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

    def __evaluate_player_score(self):
        for player in self.groups["player"].sprites():
            if self.__enemy_count_diff < 0:
                player.score += -self.__enemy_count_diff

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
        self.__evaluate_player_score()

    def loop(self):

        clock = pygame.time.Clock()
        root_group = pygame.sprite.LayeredUpdates()
        root_group.add(self)

        pygame.display.set_caption("Coroids-19")

        while True:
            dt = clock.tick() / 1000
            self.__screen.fill((0, 0, 0))  # Clear the screen each frame.

            for group in self.get_groups():
                root_group.add(group.sprites())

            root_group.update(dt)
            root_group.draw(self.__screen)

            if not self.groups["player"]:
                # player dead
                return

            pygame.display.flip()
