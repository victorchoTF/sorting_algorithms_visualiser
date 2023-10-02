from pygame import KEYDOWN, K_p, event as pg_event


def presentation_mode(event: pg_event) -> bool:
    if event.type == KEYDOWN:
        if event.key == K_p:
            return True

    return False
