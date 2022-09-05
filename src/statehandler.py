import pygame


KEYPRESSED = 'a'

state_handler_registry = {
    KEYPRESSED: []
}


def register(func, state_type, keys=[], **kwargs):
    state_handler_registry[state_type].append(
        {"func":  func, "kwargs": kwargs, "keys": keys})


def update_registered():
    for handler in state_handler_registry[KEYPRESSED]:
        keys = pygame.key.get_pressed()
        for key in handler["keys"]:
            if keys[key]:
                handler["func"](**handler["kwargs"])
