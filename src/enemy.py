import random
# import pygame

# from config import EnemiesConfig
from gameobject import GameObject


class Enemy(GameObject):
    def __init__(self, pos):
        super().__init__(pos, image_path="assets/big_corona.png",
                         image_size=(100, 100))
        self._layer = 15
        self.radius = 80/2

    def update(self, dt):
        self.move(70*dt)
