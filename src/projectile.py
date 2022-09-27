import pygame


class Projectile:
    def __init__(self, pos, direction):
        self.__direction = direction
        self.__pos = pos
        self.__image = pygame.image.load("projectile.png")
        self.__image = pygame.transform.scale(self.__image, (100, 100))
        self.__rotated_img = self.__image
        self.__rotated_img = pygame.transform.rotate(
            self.__image, self.__direction.angle_to(pygame.Vector2(0, 1)) - 90)

    def move(self, velocity):
        self.__pos += self.__direction * velocity

    def draw(self, surface):
        surface.blit(self.__rotated_img, self.__pos -
                     pygame.Vector2(self.__rotated_img.get_size()) / 2)
