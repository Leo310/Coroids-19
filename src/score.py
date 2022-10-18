import pygame

from gameobject import GameObject
from config import GameConfig


class Score(GameObject):
    def __init__(self):
        super().__init__()
        self._layer = 20
        self.score = 0
        self.__font = pygame.font.Font("assets/menu/font.ttf", 50)
        self.image = self.__font.render(str(self.score), True, "#d7fcd4")
        self.rect = self.image.get_rect()
        size = GameConfig.SIZE.value
        self.rect.center = (size[0]/2-self.rect.x/2, 80)

    def update(self, dt):
        self.image = self.__font.render(str(self.score), True, "#d7fcd4")


class Highscore:
    highscore = 0
    score = 0
    new_highscore = False

    @staticmethod
    def set(score):
        Highscore.score = score
        if score > Highscore.highscore:
            Highscore.highscore = score
            Highscore.new_highscore = True
            return
        Highscore.new_highscore = False
