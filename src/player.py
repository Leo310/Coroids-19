import pygame

from projectile import Projectile


class Player:
    def __init__(self, pos, vel, angle, projectile_speed):
        self.pos = pygame.Vector2(pos)
        self.vel = vel
        self.rotation_speed = angle
        self.projectile_speed = projectile_speed
        self.projectiles = []

        self.__image = pygame.image.load("tcell.webp")
        self.__image = pygame.transform.scale(self.__image, (200, 200))
        self.__rotated_img = self.__image
        self.__total_angle = 0
        self.__direction = pygame.Vector2(0, 1)

    def __move(self, direction):
        self.pos += self.__direction * self.vel * direction

    def move_up(self):
        self.__move(1)

    def move_down(self):
        self.__move(-1)

    def __rotate(self, direction):
        self.__direction = self.__direction.rotate(
            -self.rotation_speed * direction)
        self.__total_angle += self.rotation_speed * direction
        self.__rotated_img = pygame.transform.rotate(
            self.__image, self.__total_angle)

    def rotate_left(self):
        self.__rotate(-1)

    def rotate_right(self):
        self.__rotate(1)

    def shoot(self, mousepos):
        shoot_direction = pygame.Vector2(mousepos) - self.pos
        shoot_direction = shoot_direction.normalize()
        self.projectiles.append(Projectile(
            self.pos.copy(), shoot_direction, self.projectile_speed))

    def draw(self, surface):
        surface.blit(self.__rotated_img, self.pos -
                     pygame.Vector2(self.__rotated_img.get_size()) / 2)
