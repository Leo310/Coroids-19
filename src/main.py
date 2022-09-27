import sys
import pygame
import player

# could make them variable if we dynamically need to change them
PLAYER_SPEED = 300
PROJECTILE_SPEED = 900
PLAYER_ROTATION = 120


def main():
    pygame.init()

    clock = pygame.time.Clock()

    width, height = (1300, 750)
    screen = pygame.display.set_mode((width, height))
    p1 = player.Player((500, 500))

    while True:
        dt = clock.tick() / 1000

        if p1.pos.x < 0:
            p1.pos.x = width
        elif p1.pos.x > width:
            p1.pos.x = 0
        if p1.pos.y < 0:
            p1.pos.y = height
        elif p1.pos.y > height:
            p1.pos.y = 0

        screen.fill("#121212")

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # p1.shoot(pygame.mouse.get_pos()) # shoots to mouse pos
                    p1.shoot()  # shoots in player direction
            elif event.type == pygame.QUIT:
                quit_game()

        # State(Key pressed)-handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            p1.rotate(-PLAYER_ROTATION * dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            p1.rotate(PLAYER_ROTATION * dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            p1.move(-PLAYER_SPEED * dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            p1.move(PLAYER_SPEED * dt)

        for projectile in p1.projectiles:
            projectile.move(PROJECTILE_SPEED * dt)
            projectile.draw(screen)

        p1.draw(screen)
        pygame.display.flip()


def quit_game():
    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
