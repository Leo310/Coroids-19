import sys
import pygame

from gameobject import GameObject
from config import GameConfig
from config import MenuConfig
from button import Button
from text import Text

from score import Highscore


class Deathscreen(GameObject):
    def __init__(self, screen):
        size = GameConfig.SIZE.value
        super().__init__(image_size=size,
                         image_paths=["assets/menu/Main_Background.png"])

        self.__screen = screen
        self._layer = 0
        # setting game to middle pos because image need to be renderd in top right
        middle_pos = (size[0]/2, size[1]/2)
        self.rect.center = middle_pos

        self.__back_pressed = False
        self.__quit_pressed = False

        def back_pressed():
            self.__back_pressed = True

        def quit_pressed():
            self.__quit_pressed = True
        back_button = Button((size[0]/2, 250), (400, 170),
                             "assets/menu/Death Rect.png", 75, "Back", back_pressed)
        quit_button = Button((size[0]/2, 450), (400, 170),
                             "assets/menu/Quit Rect.png", 75, "QUIT", quit_pressed)

        text_color = MenuConfig.TEXT_COLOR.value
        death_text = Text(self.__screen, (size[0]/2, 100),
                          100, "YOU DIED!!!", text_color)
        self.__score_text = Text(
            self.__screen, (size[0]/2, 600), 40, "Your Score: " + str(Highscore.score), text_color)
        highscore_text = ""
        if Highscore.new_highscore:
            highscore_text = "New Highscore: " + str(Highscore.highscore)
        else:
            highscore_text = "Your Highscore: " + str(Highscore.highscore)
        self.__highscore_text = Text(
            self.__screen, (size[0]/2, 670), 40, highscore_text, text_color)

        self.groups["buttons"] = pygame.sprite.Group()
        self.groups["buttons"].add(back_button)
        self.groups["buttons"].add(quit_button)

        self.groups["text"] = pygame.sprite.Group()
        self.groups["text"].add(death_text)
        self.groups["text"].add(self.__score_text)
        self.groups["text"].add(self.__highscore_text)

    def update(self, dt):
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()
            sys.exit()
        if self.__quit_pressed:
            pygame.quit()
            sys.exit()

    def loop(self):
        pygame.display.set_caption("Deathscreen")

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

            if self.__back_pressed:
                return

            #     for button in [back_button, quit_button]:
            #         button.change_color(death_mouse_pos)
            #         button.update(self.__screen)
            pygame.display.update()
