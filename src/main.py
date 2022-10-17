import os
import sys
import pygame
from config import GameConfig
from game import Game
from button import Button

pygame.init()
BG = pygame.image.load("src/assets/menu/Main_Background.png")
SCREEN = pygame.display.set_mode((1280, 720))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("src/assets/menu/font.ttf", size)

def main():
    os.chdir(os.path.dirname(sys.argv[0]))

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(GameConfig.SIZE.value)
    
    game = Game()
    root_group = pygame.sprite.LayeredUpdates()
    root_group.add(game)

    while True:
        dt = clock.tick() / 1000
        screen.fill((0, 0, 0))  # Clear the screen each frame.

        for group in game.get_groups():
            root_group.add(group.sprites())

        root_group.update(dt)
        root_group.draw(screen)

        pygame.display.flip()


def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("src/assets/menu/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("src/assets/menu/Quit Rect.png"), pos=(640, 400), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.display.set_caption("Game")
                    main()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def death_screen():
    pygame.display.set_caption("Deathscreen")

    while True:    
        SCREEN.blit(BG, (0, 0))

        DEATH_MOUSE_POS = pygame.mouse.get_pos()

        DEATH_TEXT = get_font(100).render("YOU DIED!!!", True, "#b68f40")
        DEATH_RECT = DEATH_TEXT.get_rect(center=(640, 100))

        BACK_MENU_BUTTON = Button(image=pygame.image.load("src/assets/menu/Death Rect.png"), pos=(640, 250), 
                                text_input="Back to Menu", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("src/assets/menu/Quit Rect.png"), pos=(640, 400), 
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(DEATH_TEXT, DEATH_RECT)

        for button in [BACK_MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(DEATH_MOUSE_POS)
            button.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_MENU_BUTTON.checkForInput(DEATH_MOUSE_POS):
                    pygame.display.set_caption("Menu")
                    main_menu()
                if QUIT_BUTTON.checkForInput(DEATH_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
