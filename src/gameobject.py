from itertools import chain
import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), velocity=0,
                 image_path="", image_size=(0, 0)):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(
            self.image.convert_alpha(), image_size)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.groups = {}

        self._direction = pygame.Vector2(0, 1)
        self._pos = pygame.Vector2(pos)
        self._vel = velocity
        self._og_image = self.image
        self._total_angle = 0

    def move(self, velocity):
        self._pos += self._direction * velocity
        self.rect.center = self._pos

    def rotate(self, degrees):
        self._direction = self._direction.rotate(-degrees)
        self._total_angle += degrees
        self.image = pygame.transform.rotate(
            self._og_image, self._total_angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def get_groups(self):
        for _, group in self.groups.items():
            yield group
            for game_object in group.sprites():
                yield from game_object.get_groups()
