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

    def out_of_bounds(self):
        display_info = pygame.display.Info()
        width = display_info.current_w
        height = display_info.current_h
        bounds = pygame.Vector2(self._image.get_size())/2
        return self._pos.x + bounds.x < 0 or self._pos.x - bounds.x > width \
            or self._pos.y + bounds.y < 0 or self._pos.y - bounds.y > height

    def update(self, dt):
        self.move(self._vel * dt)
