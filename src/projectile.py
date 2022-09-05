import pygame


class Projectile:
    def __init__(self, pos, vel):
        self.vel = vel
        self.pos = pos
        self.image = pygame.image.load("projectile.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rotated_img = self.image
        self.rotated_img = pygame.transform.rotate(
            self.image, vel.angle_to(pygame.Vector2(0, 1)) - 90)

    def move(self):
        self.pos += self.vel

    def draw(self, surface):
        surface.blit(self.rotated_img, self.pos -
                     pygame.Vector2(self.rotated_img.get_size()) / 2)
