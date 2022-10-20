import sys
import random
import time

import pygame

from config import GameConfig
from gameobject import GameObject
from player import Player
from enemy import Enemy
from button import Button


class Game(GameObject):
    def __init__(self, screen, difficulty):
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
        self.groups["shop"] = pygame.sprite.Group()
        self.groups["player"].add(Player(middle_pos))

        self.__difficulty = difficulty

        self.__upgrade_button_image_paths = [
            "assets/shop/speed.png",
            "assets/shop/shooting_rate.png",
            "assets/shop/shooting_direction_lvl_1.png",
        ]
        self.__player_killed_enemy = False

        self.__last_enemy_kill_time = 0
        self.__last_enemy_count = 0
        self.__enemy_count_diff = 0
        self.__last_enemy_upgrade = 0
        match self.__difficulty:
            case 0:  # Hard
                self.__minimum_enemy_count = 16
                self.__minimum_enemy_increment = 3
                self.__enemy_upgrade_interval = 3
            case 1:
                self.__minimum_enemy_count = 12
                self.__minimum_enemy_increment = 2
                self.__enemy_upgrade_interval = 4
            case 2:
                self.__minimum_enemy_count = 8
                self.__minimum_enemy_increment = 1
                self.__enemy_upgrade_interval = 6
            case 3:  # Easy
                self.__minimum_enemy_count = 4
                self.__minimum_enemy_increment = 1
                self.__enemy_upgrade_interval = 8

    def __spawn_enemies(self):
        enemy_count = len(self.groups["enemies"])
        self.__enemy_count_diff = enemy_count - self.__last_enemy_count
        if self.__last_enemy_count != enemy_count:
            self.__last_enemy_kill_time = time.time()
        self.__last_enemy_count = enemy_count

        def __spawn_enemy(side):
            size = GameConfig.SIZE.value
            enemy = None
            if side:
                enemy = Enemy(
                    (size[0]+100, random.randint(100, size[1]-100)))  # right
            else:
                enemy = Enemy((-100, random.randint(100, size[1]-100)))  # left
            self.groups["enemies"].add(enemy)

        if time.time() - self.__last_enemy_kill_time >= 3:
            __spawn_enemy(random.randint(0, 1))
        if enemy_count < self.__minimum_enemy_count:
            __spawn_enemy(random.randint(0, 1))

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
                self.__player_killed_enemy = True
                player.score += -self.__enemy_count_diff

    def __create_shop(self, player):
        if player.shoot_upgrade == 2:
            self.__upgrade_button_image_paths[2] = "assets/shop/shooting_direction_lvl_2.png"
        upgrades = [player.speed_upgrade,
                    player.firerate_upgrade, player.weapon_upgrade]
        for i, upgrade in enumerate(upgrades):
            def upgrade_and_clear_all(upgrade_func=upgrade):
                upgrade_func()
                for button in self.groups["shop"].sprites():
                    button.kill()
            size = GameConfig.SIZE.value
            self.groups["shop"].add(Button(
                (size[0] - 220 * (i+1), size[1] - 100), (200, 200),
                self.__upgrade_button_image_paths[i], None, None, upgrade_and_clear_all))

    def __handle_upgrades(self):
        # player upgrades
        for player in self.groups["player"].sprites():
            if self.__player_killed_enemy:
                if player.score % 4 == 0:
                    player.firerate += 1
                    player.firerate = min(player.firerate, 20)
                if player.score == 5:
                    self.__create_shop(player)
                elif player.score == 15:
                    self.__create_shop(player)
            self.__player_killed_enemy = False

        # enemy upgrades
        if time.time() - self.__last_enemy_upgrade > self.__enemy_upgrade_interval:
            self.__minimum_enemy_count += self.__minimum_enemy_increment

            self.__last_enemy_upgrade = time.time()

    def update(self, dt):
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit(0)

        self.__spawn_enemies()
        self.__enemies_follow_player()
        self.__projetile_enemy_collision()
        self.__player_enemy_collision()
        self.__evaluate_player_score()
        self.__handle_upgrades()

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
