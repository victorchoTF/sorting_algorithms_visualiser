from pygame import QUIT, KEYDOWN, K_ESCAPE, event as pg_event


def quit_loop(event: pg_event) -> bool:
    if event.type == QUIT:
        return True

    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            return True

    return False
