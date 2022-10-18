import pygame

# from config import EnemiesConfig
from gameobject import GameObject
from config import EnemyConfig
from animation import Animation


class Enemy(GameObject):
    def __init__(self, pos):
        self.__size = EnemyConfig.SIZE.value
        self.__image_paths = [
            "assets/small/small_0.png",
            "assets/medium/medium_2.png",
            "assets/medium/medium_1.png",
            "assets/medium/medium_0.png",
            "assets/big/big_2.png",
            "assets/big/big_1.png",
            "assets/big/big_0.png"
        ]
        super().__init__(pos,
                         image_paths=self.__image_paths,
                         image_size=self.__size)
        self._layer = 15
        self.radius = 80/2

        self.vel = 60
        self.health = 7
        self.set_image(self._images[self.health-1])

        self.__hit_image_paths = [
            "assets/small/small_0_red.png",
            "assets/medium/medium_2_red.png",
            "assets/medium/medium_1_red.png",
            "assets/medium/medium_0_red.png",
            "assets/big/big_2_red.png",
            "assets/big/big_1_red.png",
            "assets/big/big_0_red.png"
        ]

        # Sounds
        self.__hit_sound = pygame.mixer.Sound("assets/sounds/hit.wav")
        self.__death_sound = pygame.mixer.Sound(
            "assets/sounds/downgrade_coroid.wav")
        self.__downgrade_sound = pygame.mixer.Sound(
            "assets/sounds/downgrade_coroid.wav")

        # Animations
        self.__big_to_medium = Animation(
            0.4, [
                "assets/big_to_medium/big_to_med.png",
                "assets/big_to_medium/big_to_med_0.png",
                "assets/big_to_medium/big_to_med_1.png",
                "assets/big_to_medium/big_to_med_2.png"
            ], self.__size)
        self.__medium_to_small = Animation(
            0.4, [
                "assets/medium_to_small/med_to_small.png",
                "assets/medium_to_small/med_to_small_0.png",
                "assets/medium_to_small/med_to_small_1.png",
                "assets/medium_to_small/med_to_small_2.png"
            ], self.__size)
        self.__death_anim = Animation(
            0.4, ["assets/destroy/destroy_0.png",
                  "assets/destroy/destroy_1.png",
                  "assets/destroy/destroy_2.png"], self.__size)

        self.__animations = [self.__big_to_medium,
                             self.__medium_to_small, self.__death_anim]

    def hit(self):
        if self.health > 0:
            self.__hit_sound.play()
            self.health -= 1

            if self.health > 1:
                hit_anim = Animation(
                    0.2, [self.__hit_image_paths[self.health-1],
                          self.__image_paths[self.health-1]], self.__size)
                self.__animations.append(hit_anim)
                hit_anim.start()

            match self.health:
                case 4:
                    def medium_stats():
                        self.vel = 100
                        self.set_image(self._images[self.health-1])
                    # self.__downgrade_sound.play()
                    self.__big_to_medium.start(medium_stats)
                case 1:
                    def small_stats():
                        self.vel = 140
                        self.set_image(self._images[self.health-1])
                    # self.__downgrade_sound.play()
                    self.__medium_to_small.start(small_stats)
                case 0:
                    self.__death_sound.play()
                    self.__death_anim.start(self.kill)

    def update(self, dt):
        self.move(self.vel*dt)

        for animation in self.__animations:
            if animation.playing:
                self.set_image(animation.update())
