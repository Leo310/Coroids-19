import pygame

from config import ProjectileConfig
from gameobject import GameObject


class Projectile(GameObject):
    def __init__(self, pos, direction):
        super().__init__(pos, ProjectileConfig.SPEED.value,
                         0, "assets/antibody.png", (60, 38))
        self._direction = direction
        self.image = pygame.transform.rotate(
            self._og_image, self._direction.angle_to(pygame.Vector2(0, 1)) - 90)
        self._layer = 5

    def out_of_bounds(self):
        display_info = pygame.display.Info()
        width = display_info.current_w
        height = display_info.current_h
        bounds = pygame.Vector2(self.image.get_size())/2
        return self.rect.centerx + bounds.x < 0 or self.rect.centerx - bounds.x > width \
            or self.rect.centery + bounds.y < 0 or self.rect.centery - bounds.y > height

    def update(self, dt):
        self.move(self._vel * dt)
