import time
import pygame

from gameobject import GameObject
from config import MenuConfig


class Button(GameObject):
    def __init__(self, pos, size, image_path, font_size, text, func):
        super().__init__(pos, image_paths=[
            image_path,
        ], image_size=size)
        self._layer = 20
        self.__callback = func

        self.__color = "#d7fcd4"

        if font_size:
            self.font = pygame.font.Font("assets/menu/font.ttf", font_size)
        self.text = text
        self.__mouse_pressed = False

        self.__mouse_hover = False
        self.mouse_clicked = False
        self.clicked_time = 0

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()

        self.__mouse_hover = False
        if mouse_pos[0] in range(self.rect.left, self.rect.right) \
                and mouse_pos[1] in range(self.rect.top, self.rect.bottom):
            self.__mouse_hover = True
            if self.__mouse_pressed and not pygame.mouse.get_pressed()[0]\
                    and time.time() - self.clicked_time < 0.1:
                self.__callback()
                self.mouse_clicked = True

        if self.text and self.font:
            text_img = self.font.render(
                self.text, True, self.__color)
            text_pos = (self.rect.w/2-text_img.get_rect().w/2,
                        self.rect.h/2-text_img.get_rect().h/2)
            self.image.blit(text_img, text_pos)

        if pygame.mouse.get_pressed()[0]:
            self.clicked_time = time.time()
            self.__mouse_pressed = True

        self.__color = "#d7fcd4"
        if self.mouse_clicked:
            self.__color = MenuConfig.TEXT_COLOR.value
        elif self.__mouse_hover:
            self.__color = "#f0f000"
