import pygame


KEYPRESSED = 'a'

state_handler_registry = {
    KEYPRESSED: []
}


def register(func, state_type, key=None, **kwargs):
    state_handler_registry[state_type].append(
        {"func":  func, "kwargs": kwargs, "key": key})


def update_registered():
    for handler in state_handler_registry[KEYPRESSED]:
        keys = pygame.key.get_pressed()
        if keys[handler["key"]]:
            handler["func"](**handler["kwargs"])
