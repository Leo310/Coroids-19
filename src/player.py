import pygame


class Player:

    def __init__(self, position, size):
        self.pos = pygame.Vector2(position)
        self.size = size

    def move(self, vel):
        self.pos += pygame.Vector2(vel)

    def draw(self, surface):
        pygame.draw.rect(
            surface, pygame.Color("#673AB7"),
            pygame.Rect(self.pos, self.size))
