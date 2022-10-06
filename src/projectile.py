import pygame

from config import ProjectileConfig
from gameobject import GameObject


class Projectile(GameObject):
    def __init__(self, pos, direction):
        self.__size = ProjectileConfig.SIZE.value
        super().__init__(pos, ProjectileConfig.SPEED.value,
                         ["assets/antibody.png"], self.__size)
        self.direction = direction
        self.image = pygame.transform.rotate(
            self._og_image, self.direction.angle_to(pygame.Vector2(0, 1)) - 90)
        self._layer = 5

    def __out_of_bounds(self):
        display_info = pygame.display.Info()
        width = display_info.current_w
        height = display_info.current_h
        bounds = pygame.Vector2(self.__size)/2
        return self.rect.centerx + bounds.x < 0 or self.rect.centerx - bounds.x > width\
            or self.rect.centery + bounds.y < 0 or self.rect.centery - bounds.y > height

    def update(self, dt):
        self.move(self.vel * dt)

        if self.__out_of_bounds():
            self.kill()
