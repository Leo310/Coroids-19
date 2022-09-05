event_handler_registry = {}


def register(event_type, *args):
    def decorator(fn):
        event_handler_registry[event_type] = {"func": fn, "args": args}
        return fn
    return decorator


def call_registered(event_type):
    handler = event_handler_registry.get(event_type)
    if handler:
        handler["func"](*handler["args"])
    # else:
        # print("No handler registered for event: ", event_type)
