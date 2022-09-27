import pygame

from projectile import Projectile


class Player:
    def __init__(self, pos, velocity, rotation_speed, projectile_speed):
        self.__pos = pygame.Vector2(pos)
        self.projectiles = []

        self.__vel = velocity
        self.__rotation_speed = rotation_speed
        self.__projectile_speed = projectile_speed
        self.__image = pygame.image.load("tcell.webp")
        self.__image = pygame.transform.scale(self.__image, (200, 200))
        self.__rotated_img = self.__image
        self.__total_angle = 0
        self.__direction = pygame.Vector2(0, 1)

    def move(self, velocity):
        self.__pos += self.__direction * velocity

    def rotate(self, rotation_speed):
        self.__direction = self.__direction.rotate(-rotation_speed)
        self.__total_angle += rotation_speed
        self.__rotated_img = pygame.transform.rotate(
            self.__image, self.__total_angle)

    def shoot(self, velocity, target=None):
        if target:
            shoot_direction = pygame.Vector2(target) - self.__pos
            shoot_direction = shoot_direction.normalize()
        else:
            shoot_direction = self.__direction
        self.projectiles.append(Projectile(
            self.__pos.copy(), velocity, shoot_direction))

    def update(self, dt):
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                # p1.shoot(pygame.mouse.get_pos()) # shoots to mouse pos
                # shoots in player direction
                self.shoot(self.__projectile_speed)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(-self.__rotation_speed * dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(self.__rotation_speed * dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-self.__vel * dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(self.__vel * dt)

        # Player out of bounds logic
        display_info = pygame.display.Info()
        width = display_info.current_w
        height = display_info.current_h
        if self.__pos.x < 0:
            self.__pos.x = width
        elif self.__pos.x > width:
            self.__pos.x = 0
        if self.__pos.y < 0:
            self.__pos.y = height
        elif self.__pos.y > height:
            self.__pos.y = 0

    def draw(self, surface):
        surface.blit(self.__rotated_img, self.__pos -
                     pygame.Vector2(self.__rotated_img.get_size()) / 2)
