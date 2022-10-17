import time
import pygame

from config import PlayerConfig
from gameobject import GameObject
from projectile import Projectile


class Player(GameObject):
    def __init__(self, pos):
        self.__size = PlayerConfig.SIZE.value
        super().__init__(pos, PlayerConfig.SPEED.value,
                         [
                             "assets/player/player_death_2.png",
                             "assets/player/player_death_1.png",
                             "assets/player/player_death_0.png",
                             "assets/player/player.png"
                         ], self.__size)
        self.groups["projectiles"] = pygame.sprite.Group()
        
        self._layer = 10
        self.radius = 80/2

        self.health = 4
        self.set_image(self._images[self.health-1])

        self.__last_hit_time = 0
        self.__rotation_speed = PlayerConfig.ROTATION_SPEED.value

        # Sounds
        self.__piu = pygame.mixer.Sound("assets/sounds/piu.wav")
        self.__death_sound = pygame.mixer.Sound(
            "assets/sounds/player_death.wav")

    def shoot(self, target=None):
        self.__piu.play()
        if target:
            shoot_direction = pygame.Vector2(target) - self.pos
            shoot_direction = shoot_direction.normalize()
        else:
            shoot_direction = self.direction
        self.groups["projectiles"].add(Projectile(
            self.rect.center, shoot_direction))

    def hit(self):
        if time.time() - self.__last_hit_time > 1.5:
            self.health -= 1
            self.radius -= 10
            
            if self.health == 0:
                self.kill()
                self.__death_sound.play()
                return         
            self.set_image(self._images[self.health-1])
            self.__last_hit_time = time.time()

    def __out_of_bounds(self):
        # Player out of bounds logic
        display_info = pygame.display.Info()
        width = display_info.current_w
        height = display_info.current_h
        if self.pos.x < 0:
            self.pos.x = width
        elif self.pos.x > width:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = height
        elif self.pos.y > height:
            self.pos.y = 0

    def __handle_events(self, dt):
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                # p1.shoot(pygame.mouse.get_pos()) # shoots to mouse pos
                # shoots in player direction
                self.shoot()
            if event.key == pygame.K_LSHIFT:
                self.vel *= 2

        for event in pygame.event.get(pygame.KEYUP):
            if event.key == pygame.K_LSHIFT:
                self.vel /= 2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(-self.__rotation_speed * dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(self.__rotation_speed * dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-self.vel * dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(self.vel * dt)

    def update(self, dt):
        self.__handle_events(dt)
        self.__out_of_bounds()
