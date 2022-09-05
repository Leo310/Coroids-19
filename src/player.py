import pygame

from projectile import Projectile


class Player:

    def __init__(self):
        self.direction = pygame.Vector2(0, 1)
        self.pos = pygame.Vector2(500, 500)
        self.image = pygame.image.load("tcell.webp")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rotated_img = self.image
        self.angle = 0
        self.projectiles = []

    def move(self, vel):
        self.pos += self.direction * vel

    def rotate(self, angle):
        self.direction = self.direction.rotate(-angle)
        self.angle += angle
        self.rotated_img = pygame.transform.rotate(self.image, self.angle)

    def shoot(self, mousepos, vel):
        shootvec = pygame.Vector2(mousepos) - self.pos
        shootvec = shootvec.normalize() * vel
        self.projectiles.append(Projectile(self.pos.copy(), shootvec))

    def draw(self, surface):
        surface.blit(self.rotated_img, self.pos -
                     pygame.Vector2(self.rotated_img.get_size()) / 2)
