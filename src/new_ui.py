import sys
import pygame

from gameobject import GameObject
from config import GameConfig
from upgradebutton import Button
from text import Text

from score import Highscore


class UI(GameObject):
    def __init__(self, screen):
        size = GameConfig.SIZE.value
        super().__init__(image_size=size,
                         image_paths=["assets/menu/Main_Background.png"])

        self.__screen = screen
        self._layer = 0
        # setting game to middle pos because image need to be renderd in top right
        middle_pos = (size[0]/2, size[1]/2)
        self.rect.center = middle_pos

        def play_pressed():
            self.__play_pressed = True

        def quit_pressed():
            self.__quit_pressed = True
        play_button = Button((640, 250), (400, 200),
                             "assets/menu/Play Rect.png", 75, "PLAY", play_pressed)
        quit_button = Button((640, 450), (400, 200),
                             "assets/menu/Quit Rect.png", 75, "QUIT", quit_pressed)

        self.groups["buttons"] = pygame.sprite.Group()
        self.groups["buttons"].add(play_button)
        self.groups["buttons"].add(quit_button)

        self.groups["text"] = pygame.sprite.Group()
        self.groups["text"].add(
            Text(self.__screen, (640, 100), 100, "Coroids-19", "#b68f40"))
        self.groups["text"].add(
            Text(self.__screen, (640, 600), 40, "W, A, S, D, Shift, Space", "#b68f40"))

        self.__play_pressed = False
        self.__quit_pressed = False
        self.__back_pressed = False

    def update(self, dt):
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()
            sys.exit()
        if self.__quit_pressed:
            self.__quit_pressed = False
            pygame.quit()
            sys.exit()

    def main_menu_loop(self):
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
                self.__play_pressed = False
                return

            pygame.display.flip()

    def death_screen_loop(self):
        pygame.display.set_caption("Deathscreen")

        def play_pressed():
            print("he")
            self.__play_pressed = True

        def quit_pressed():
            self.__quit_pressed = True
        back_button = Button((640, 250), (400, 200),
                             "assets/menu/Death Rect.png", 75, "Back to Menu", play_pressed)
        quit_button = Button((640, 450), (400, 200),
                             "assets/menu/Quit Rect.png", 75, "QUIT", quit_pressed)

        self.groups["buttons"].add(back_button)
        self.groups["buttons"].add(quit_button)

        death_text = self.__big_font.render(
            "YOU DIED!!!", True, "#b68f40")
        death_rect = death_text.get_rect(center=(640, 100))
        score_text = self.__small_font.render(
            "Your Score: " + str(Highscore.score), True, "#b68f40")
        score_rect = score_text.get_rect(center=(640, 540))
        highscore_text = self.__small_font.render(
            "New Highscore: " + str(Highscore.highscore), True, "#b68f40")
        highscore_rect = highscore_text.get_rect(center=(640, 640))

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
                self.__back_pressed = False
                return

            self.__screen.blit(death_text, death_rect)
            self.__screen.blit(score_text, score_rect)

            if Highscore.new_highscore:
                highscore_text = self.__small_font.render(
                    "New Highscore: " + str(Highscore.highscore), True, "#b68f40")
                highscore_rect = highscore_text.get_rect(center=(640, 640))
            else:
                highscore_text = self.__small_font.render(
                    "Your Highscore: " + str(Highscore.highscore), True, "#b68f40")
                highscore_rect = highscore_text.get_rect(center=(640, 640))

                self.__screen.blit(highscore_text, highscore_rect)

            #     for button in [back_button, quit_button]:
            #         button.change_color(death_mouse_pos)
            #         button.update(self.__screen)
            pygame.display.update()
