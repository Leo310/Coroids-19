import sys
import pygame

from config import GameConfig
from button import Button

from score import Highscore


class UI:
    def __init__(self, screen):
        image = pygame.image.load(
            "assets/menu/Main_Background.png")
        image = pygame.transform.smoothscale(
            image.convert_alpha(), GameConfig.SIZE.value)
        self.__background_img = image
        self.__screen = screen

        self.__small_font = pygame.font.Font("assets/menu/font.ttf", 40)
        self.__med_font = pygame.font.Font("assets/menu/font.ttf", 75)
        self.__big_font = pygame.font.Font("assets/menu/font.ttf", 100)

    def main_menu_loop(self):
        pygame.display.set_caption("Menu")

        play_button = Button(image=pygame.image.load("assets/menu/Play Rect.png"),
                             pos=(640, 250),
                             text_input="PLAY", font=self.__med_font, base_color="#d7fcd4",
                             hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/menu/Quit Rect.png"),
                             pos=(640, 400),
                             text_input="QUIT", font=self.__med_font, base_color="#d7fcd4",
                             hovering_color="White")

        menu_text = self.__big_font.render("Coroids-19", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        instructions_text = self.__small_font.render(
            "W, A, S, D, Shift, Space", True, "#b68f40")
        instructions_rect = menu_text.get_rect(center=(640, 600))

        while True:
            self.__screen.blit(self.__background_img, (0, 0))
            self.__screen.blit(menu_text, menu_rect)
            self.__screen.blit(instructions_text, instructions_rect)

            mouse_pos = pygame.mouse.get_pos()

            for button in [play_button, quit_button]:
                button.change_color(mouse_pos)
                button.update(self.__screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.check_for_input(mouse_pos):
                        return
                    if quit_button.check_for_input(mouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

    def death_screen_loop(self):
        pygame.display.set_caption("Deathscreen")

        back_button = Button(image=pygame.image.load("assets/menu/Death Rect.png"),
                             pos=(640, 250),
                             text_input="Back to Menu", font=self.__med_font,
                             base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/menu/Quit Rect.png"),
                             pos=(640, 400),
                             text_input="QUIT", font=self.__med_font,
                             base_color="#d7fcd4", hovering_color="White")

        death_text = self.__big_font.render(
            "YOU DIED!!!", True, "#b68f40")
        death_rect = death_text.get_rect(center=(640, 100))
        score_text = self.__small_font.render(
            "Your Score: " + str(Highscore.score), True, "#b68f40")
        score_rect = score_text.get_rect(center=(640, 540))
        highscore_text = self.__small_font.render(
            "New Highscore: " + str(Highscore.highscore), True, "#b68f40")
        highscore_rect = highscore_text.get_rect(center=(640, 640))

        while True:
            self.__screen.blit(self.__background_img, (0, 0))
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
            death_mouse_pos = pygame.mouse.get_pos()

            for button in [back_button, quit_button]:
                button.change_color(death_mouse_pos)
                button.update(self.__screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.check_for_input(death_mouse_pos):
                        pygame.display.set_caption("Menu")
                        return
                    if quit_button.check_for_input(death_mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()