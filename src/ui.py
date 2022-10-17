import sys
import pygame

from config import GameConfig
from button import Button


class UI:
    def __init__(self, screen):
        image = pygame.image.load(
            "assets/menu/Main_Background.png")
        image = pygame.transform.smoothscale(
            image.convert_alpha(), GameConfig.SIZE.value)
        self.__background_img = image
        self.__screen = screen

    @ staticmethod
    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/menu/font.ttf", size)

    def main_menu_loop(self):
        pygame.display.set_caption("Menu")

        play_button = Button(image=pygame.image.load("assets/menu/Play Rect.png"),
                             pos=(640, 250),
                             text_input="PLAY", font=UI.get_font(75), base_color="#d7fcd4",
                             hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/menu/Quit Rect.png"),
                             pos=(640, 400),
                             text_input="QUIT", font=UI.get_font(75), base_color="#d7fcd4",
                             hovering_color="White")

        menu_text = UI.get_font(100).render("Coroids-19", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        while True:
            self.__screen.blit(self.__background_img, (0, 0))
            self.__screen.blit(menu_text, menu_rect)

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
                             text_input="Back to Menu", font=UI.get_font(75),
                             base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/menu/Quit Rect.png"),
                             pos=(640, 400),
                             text_input="QUIT", font=UI.get_font(75),
                             base_color="#d7fcd4", hovering_color="White")

        death_text = UI.get_font(100).render(
            "YOU DIED!!!", True, "#b68f40")
        death_rect = death_text.get_rect(center=(640, 100))

        while True:
            self.__screen.blit(self.__background_img, (0, 0))
            self.__screen.blit(death_text, death_rect)
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
