import sys
import pygame

from gameobject import GameObject
from config import GameConfig
from config import MenuConfig
from button import Button
from text import Text


class Menu(GameObject):
    def __init__(self, screen):
        size = GameConfig.SIZE.value
        super().__init__(image_size=size,
                         image_paths=["assets/startscreen.png"])

        self.__screen = screen
        self._layer = 0
        # setting game to middle pos because image need to be renderd in top right
        middle_pos = (size[0]/2, size[1]/2)
        self.rect.center = middle_pos

        self.__play_pressed = False
        self.__quit_pressed = False
        self.__difficulty = 2

        def play_pressed():
            self.__play_pressed = True

        def quit_pressed():
            self.__quit_pressed = True
        play_button = Button((size[0]/2, 250), (400, 120),
                             "assets/menu/Play Rect.png", 75, "PLAY", play_pressed)
        quit_button = Button((size[0]/2, 550), (400, 120),
                             "assets/menu/Quit Rect.png", 75, "QUIT", quit_pressed)

        self.groups["buttons"] = pygame.sprite.Group()
        self.groups["text"] = pygame.sprite.Group()

        for i in range(0, 4):
            def difficulty(lvl=i):
                for button in self.groups["buttons"].sprites():
                    button.mouse_clicked = False
                self.__difficulty = lvl
            self.groups["buttons"].add(Button((size[0]/2 - 60 + 160 * i, 400), (150, 100),
                                              "assets/menu/Play Rect.png", 40, str(i) + "x", difficulty))
        self.groups["buttons"].add(play_button)
        self.groups["buttons"].add(quit_button)
        text_color = MenuConfig.TEXT_COLOR.value
        self.groups["text"].add(
            Text(self.__screen, (size[0]/2, 100), 100, "Coroids-19", text_color))
        self.groups["text"].add(
            Text(self.__screen, (270, 400), 40, "Impfstatus: ", text_color))
        self.groups["text"].add(
            Text(self.__screen, (size[0]/2, 700), 40,
                 "W, A, S, D, Shift, Space", text_color))

    def update(self, dt):
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()
            sys.exit()
        if self.__quit_pressed:
            pygame.quit()
            sys.exit()

    def loop(self):
        pygame.display.set_caption("Menu")

        clock = pygame.time.Clock()
        root_group = pygame.sprite.LayeredUpdates()
        root_group.add(self)

        while True:
            dt = clock.tick() / 1000
            self.__screen.fill((0, 0, 0))  # Clear the screen each frame.

            for group in self.get_groups():
                root_group.add(group.sprites())

            root_group.update(dt)
            root_group.draw(self.__screen)

            if self.__play_pressed:
                return self.__difficulty

            pygame.display.flip()
