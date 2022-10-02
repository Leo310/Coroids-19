import pygame

from config import PlayerConfig
from gameobject import GameObject
from projectile import Projectile


class Player(GameObject):
    def __init__(self, pos):
        super().__init__(pos, PlayerConfig.SPEED.value,
                         PlayerConfig.ROTATION_SPEED.value,
                         "assets/t_cell.png", (100, 100))
        self.groups["projectiles"] = pygame.sprite.Group()
        self._layer = 10
        self.radius = 80/2

    def shoot(self, target=None):
        if target:
            shoot_direction = pygame.Vector2(target) - self._pos
            shoot_direction = shoot_direction.normalize()
        else:
            shoot_direction = self._direction
        self.groups["projectiles"].add(Projectile(
            self.rect.center, shoot_direction))

    def update(self, dt):
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                # p1.shoot(pygame.mouse.get_pos()) # shoots to mouse pos
                # shoots in player direction
                self.shoot()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(-self._rotation_speed * dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(self._rotation_speed * dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-self._vel * dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(self._vel * dt)

        # Projectile out of bounds logic
        for projectile in self.groups["projectiles"].sprites():
            if projectile.out_of_bounds():
                projectile.kill()

        # Player out of bounds logic
        display_info = pygame.display.Info()
        width = display_info.current_w
        height = display_info.current_h
        if self._pos.x < 0:
            self._pos.x = width
        elif self._pos.x > width:
            self._pos.x = 0
        if self._pos.y < 0:
            self._pos.y = height
        elif self._pos.y > height:
            self._pos.y = 0
