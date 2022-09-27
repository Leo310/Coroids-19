import pygame

from config import ProjectileConfig
from gameobject import GameObject


class Projectile(GameObject):
    def __init__(self, pos, direction):
        super().__init__(pos, ProjectileConfig.SPEED.value,
                         0, "projectile.png", (100, 100), zindex=5)
        self._direction = direction
        self._rotated_img = pygame.transform.rotate(
            self._image, self._direction.angle_to(pygame.Vector2(0, 1)) - 90)

    def update(self, dt):
        self.move(self._vel * dt)
