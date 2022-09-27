import sys
import pygame
import player

# could make them variable if we dynamically need to change them
PLAYER_SPEED = 300
PROJECTILE_SPEED = 900
PLAYER_ROTATION_SPEED = 120


def main():
    pygame.init()

    clock = pygame.time.Clock()

    width, height = (1300, 750)
    screen = pygame.display.set_mode((width, height))
    p1 = player.Player((500, 500), PLAYER_SPEED,
                       PLAYER_ROTATION_SPEED, PROJECTILE_SPEED)

    while True:
        dt = clock.tick() / 1000

        # Event handling
        if pygame.event.get(pygame.QUIT):
            quit_game()

        screen.fill("#121212")

        for gameobject in (*p1.projectiles, p1):
            gameobject.update(dt)
            gameobject.draw(screen)

        pygame.display.flip()


def quit_game():
    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
