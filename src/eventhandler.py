event_handler_registry = {}


def register(type):
    def decorator(fn):
        event_handler_registry[type] = fn
        return fn
    return decorator
