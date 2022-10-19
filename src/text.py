import pygame

from gameobject import GameObject


class Text(GameObject):
    def __init__(self, dest, pos, font_size, text, color):
        super().__init__(pos)
        self._layer = 20
        self.text = text
        self.__color = color
        self.__font = pygame.font.Font("assets/menu/font.ttf", font_size)
        self.image = self.__font.render(
            self.text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, dt):
        self.image = self.__font.render(
            self.text, True, self.__color)
