# import pygame

# from config import EnemiesConfig
from gameobject import GameObject


class Enemy(GameObject):
    def __init__(self, pos):
        super().__init__(pos, images_path=["assets/big_corona.png", "assets/medium_corona.png", "assets/small_corona.png"],
                         image_size=(100, 100))
        self._layer = 15
        self.radius = 80/2

        self.hit_count = 0

    def destroy(self):
        self.hit_count += 1
        if self.hit_count == 2:
            self.image = self._images[1]
            self.radius = 70/2
        elif self.hit_count == 4:
            self.image = self._images[2]
            self.radius = 60/2
        elif self.hit_count >= 5:
            self.kill()

    def update(self, dt):
        self.move(70*dt)
