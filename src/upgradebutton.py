import pygame

from gameobject import GameObject


class Button(GameObject):
    def __init__(self, pos, size, image_path, font_size, text, func):
        super().__init__(pos, image_paths=[
            image_path,
        ], image_size=size)
        self._layer = 20
        self.__callback = func

        if font_size:
            self.font = pygame.font.Font("assets/menu/font.ttf", font_size)
        self.text = text

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] in range(self.rect.left, self.rect.right) \
                and mouse_pos[1] in range(self.rect.top, self.rect.bottom):
            # if pygame.event.get(pygame.MOUSEBUTTONUP):
            self.__callback()
            self.kill()

        if self.text and self.font:
            text_img = self.font.render(
                self.text, True, "#d7fcd4")
            text_pos = (self.rect.w/2-text_img.get_rect().w/2,
                        self.rect.h/2-text_img.get_rect().h/2)
            self.image.blit(text_img, text_pos)
