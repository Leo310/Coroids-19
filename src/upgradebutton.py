import pygame

from gameobject import GameObject


class Upgradebutton(GameObject):
    def __init__(self, pos, func):
        super().__init__(pos, image_paths=[
            "assets/menu/Main_Background.png",
        ], image_size=(100, 100))
        self._layer = 20
        self.__callback = func

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] in range(self.rect.left, self.rect.right) \
                and mouse_pos[1] in range(self.rect.top, self.rect.bottom):
            if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                self.__callback()
                self.kill()
