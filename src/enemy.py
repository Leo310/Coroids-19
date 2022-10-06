# import pygame

# from config import EnemiesConfig
from gameobject import GameObject
from config import EnemyConfig
from animation import Animation


class Enemy(GameObject):
    def __init__(self, pos):
        self.__size = EnemyConfig.SIZE.value
        super().__init__(pos,
                         images_path=[
                             "assets/big_corona.png",
                             "assets/medium_corona.png",
                             "assets/small_corona.png"],
                         image_size=self.__size)
        self._layer = 15
        self.radius = 80/2

        self.hit_count = 0
        self.__death_anim = Animation(
            500, ["assets/big_corona.png",
                  "assets/medium_corona.png",
                  "assets/small_corona.png"], self.__size)

    def hit(self):
        self.hit_count += 1
        if self.hit_count == 1:
            self.image = self._images[1]
            self.radius = 70/2
        elif self.hit_count == 2:
            self.image = self._images[2]
            self.radius = 60/2
        elif self.hit_count >= 3:
            self.__death_anim.start(self.kill)

    def update(self, dt):
        self.move(70*dt)

        if self.__death_anim.playing:
            self.image = self.__death_anim.update()
