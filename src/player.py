import pygame

from projectile import Projectile


class Player:
    def __init__(self, pos, vel, projectile_speed):
        self.pos = pygame.Vector2(pos)
        self.vel = vel
        self.projectile_speed = projectile_speed
        self.projectiles = []

        self.__image = pygame.image.load("tcell.webp")
        self.__image = pygame.transform.scale(self.__image, (200, 200))
        self.__rotated_img = self.__image
        self.__total_angle = 0
        self.__direction = pygame.Vector2(0, 1)

    def move(self, velocity):
        self.pos += self.__direction * velocity

    def rotate(self, rotation_speed):
        self.__direction = self.__direction.rotate(-rotation_speed)
        self.__total_angle += rotation_speed
        self.__rotated_img = pygame.transform.rotate(
            self.__image, self.__total_angle)

    def shoot(self, target=None):
        if target:
            shoot_direction = pygame.Vector2(target) - self.pos
            shoot_direction = shoot_direction.normalize()
        else:
            shoot_direction = self.__direction
        self.projectiles.append(Projectile(
            self.pos.copy(), shoot_direction, self.projectile_speed))

    def draw(self, surface):
        surface.blit(self.__rotated_img, self.pos -
                     pygame.Vector2(self.__rotated_img.get_size()) / 2)
