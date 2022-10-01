from itertools import chain
import pygame


class GameObject:
    def __init__(self, pos=(0, 0), velocity=0, rotation_speed=0,
                 image_path="", image_size=(0, 0), zindex=0):
        self.zindex = zindex

        self.game_objects = {}
        self._pos = pygame.Vector2(pos)
        self._vel = velocity
        self._rotation_speed = rotation_speed
        self._image = pygame.image.load(image_path)
        self._image = pygame.transform.scale(self._image, image_size)
        self._rotated_img = self._image
        self._total_angle = 0
        self._direction = pygame.Vector2(0, 1)

    def get_rect(self):
        return self._image.get_rect(topleft=self._pos)

    def move(self, velocity):
        self._pos += self._direction * velocity

    def rotate(self, degrees):
        self._direction = self._direction.rotate(-degrees)
        self._total_angle += degrees
        self._rotated_img = pygame.transform.rotate(
            self._image, self._total_angle)

    def is_colliding(self, gameobj):
        return self.get_rect().colliderect(gameobj.get_rect())

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self._rotated_img, self._pos -
                     pygame.Vector2(self._rotated_img.get_size()) / 2)

    def get_all_game_objects(self):
        yield self
        for _, specific_game_objects in self.game_objects.items():
            for game_object in specific_game_objects:
                yield from game_object.get_all_game_objects()
