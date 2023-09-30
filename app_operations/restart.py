from pygame import KEYDOWN, K_r, event as pg_event


def restart(event: pg_event):
    if event.type == KEYDOWN:
        if event.key == K_r:
            return True

    return False
