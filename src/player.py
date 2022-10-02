import pygame

from config import PlayerConfig
from gameobject import GameObject
from projectile import Projectile


class Player(GameObject):
    def __init__(self, pos):
        super().__init__(pos, PlayerConfig.SPEED.value,
                         "assets/t_cell.png", (100, 100))

        self.groups["projectiles"] = pygame.sprite.Group()

        self._layer = 10
        self.radius = 80/2

        self.__rotation_speed = PlayerConfig.ROTATION_SPEED.value
        self.__piu = pygame.mixer.Sound("assets/piu.mp3")

    def shoot(self, target=None):
        self.__piu.play()
        if target:
            shoot_direction = pygame.Vector2(target) - self.pos
            shoot_direction = shoot_direction.normalize()
        else:
            shoot_direction = self.direction
        self.groups["projectiles"].add(Projectile(
            self.rect.center, shoot_direction))

    def update(self, dt):
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

            # Projectile out of bounds logic
        for projectile in self.groups["projectiles"].sprites():
            if projectile.out_of_bounds():
                projectile.kill()

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
