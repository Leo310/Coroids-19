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
                             "assets/small/small_0.png",
                             "assets/medium/medium_2.png",
                             "assets/medium/medium_1.png",
                             "assets/medium/medium_0.png",
                             "assets/big/big_2.png",
                             "assets/big/big_1.png",
                             "assets/big/big_0.png"
                         ],
                         image_size=self.__size)
        self._layer = 15
        self.radius = 80/2

        self.vel = 60
        self.health = 7
        self.image = self._images[self.health-1]

        self.__big_to_medium = Animation(
            400, [
                "assets/big_to_medium/big_to_med.png",
                "assets/big_to_medium/big_to_med_0.png",
                "assets/big_to_medium/big_to_med_1.png",
                "assets/big_to_medium/big_to_med_2.png"
            ], self.__size)
        self.__medium_to_small = Animation(
            400, [
                "assets/medium_to_small/med_to_small.png",
                "assets/medium_to_small/med_to_small_0.png",
                "assets/medium_to_small/med_to_small_1.png",
                "assets/medium_to_small/med_to_small_2.png"
            ], self.__size)
        self.__death_anim = Animation(
            400, ["assets/destroy/destroy_0.png",
                  "assets/destroy/destroy_1.png",
                  "assets/destroy/destroy_2.png"], self.__size)

        self.__animations = [self.__big_to_medium,
                             self.__medium_to_small, self.__death_anim]

    def hit(self):
        self.health -= 1
        self.image = self._images[self.health-1]
        match self.health:
            case 4:
                def medium_stats():
                    self.vel = 90
                    self.image = self._images[self.health-1]
                self.__big_to_medium.start(medium_stats)
            case 1:
                def small_stats():
                    self.vel = 120
                    self.image = self._images[self.health-1]
                self.__medium_to_small.start(small_stats)
            case 0:
                self.__death_anim.start(self.kill)

    def update(self, dt):
        self.move(self.vel*dt)

        for animation in self.__animations:
            if animation.playing:
                self.image = animation.update()
