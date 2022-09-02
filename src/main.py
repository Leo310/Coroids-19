import pygame

import eventhandler

pygame.init()
clock = pygame.time.Clock()

(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


@eventhandler.register(pygame.QUIT)
def quit_game():
    pygame.quit()
    quit(0)


running = True
while running:
    for event in pygame.event.get():
        handler = eventhandler.event_handler_registry.get(event.type)
        if handler:
            handler()
        else:
            print("No handler registered for event: ", event)
