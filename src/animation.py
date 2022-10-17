import time
import pygame


class Animation():
    def __init__(self, duration, image_paths, image_size):
        self.playing = False

        self.__images = []
        self.__duration = duration
        self.__img_index = 0
        self.__on_finish = None
        self.__image = None

        for image_path in image_paths:
            image = pygame.image.load(image_path)
            image = pygame.transform.smoothscale(
                image.convert_alpha(), image_size)
            self.__images.append(image)

        # so that Animation directly starts at 0 and not after first time fraction
        self.__last_time = -self.__duration / len(self.__images)

    def start(self, on_finish=None):
        self.playing = True
        self.__on_finish = on_finish

    def update(self):
        if self.playing and\
                time.time() - self.__last_time > self.__duration / len(self.__images):
            self.__image = self.__images[self.__img_index]
            self.__img_index += 1
            if self.__img_index == len(self.__images):
                self.__img_index = 0
                self.playing = False
                if self.__on_finish:
                    self.__on_finish()
            self.__last_time = time.time()
        return self.__image
