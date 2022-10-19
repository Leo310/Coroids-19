import pygame

from gameobject import GameObject


class Text(GameObject):
    def __init__(self, dest, pos, font_size, text, color):
        super().__init__(pos)
        self._layer = 20
        font = pygame.font.Font("assets/menu/font.ttf", font_size)
        self.image = font.render(
            text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
