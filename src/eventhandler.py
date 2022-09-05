from enum import Enum
import pygame


class State(Enum):
    KEYPRESSED = 'a'


event_handler_registry = {
    pygame.QUIT: [],
    pygame.KEYDOWN: [],
    pygame.KEYUP: [],
    pygame.MOUSEMOTION: [],
}


def register(func, event_type, key=None, **kwargs):
    event_handler_registry[event_type].append(
        {"func":  func, "kwargs": kwargs, "key": key})


def call_registered(event):
    if event.type == pygame.KEYDOWN:
        for handler in event_handler_registry[pygame.KEYDOWN]:
            if handler["key"] == event.key:
                handler["func"](**handler["kwargs"])

    if event.type == pygame.QUIT:
        for handler in event_handler_registry[pygame.QUIT]:
            handler["func"](**handler["kwargs"])
