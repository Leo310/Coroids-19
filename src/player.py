import pygame


class Player:

    def __init__(self):
        self.dir = pygame.Vector2(0, 1)
        self.pos = pygame.Vector2(0, 0)
        self.image = pygame.image.load("tcell.webp")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rotated_img = self.image
        self.angle = 0

    def move(self, vel):
        self.pos += self.dir * vel

    def rotate(self, angle):
        self.dir = self.dir.rotate(-angle)
        self.angle += angle
        self.rotated_img = pygame.transform.rotate(self.image, self.angle)

    def draw(self, surface):
        surface.blit(self.rotated_img, self.pos -
                     pygame.Vector2(self.rotated_img.get_size()) / 2)
