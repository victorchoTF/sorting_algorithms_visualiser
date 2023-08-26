from pygame import KEYDOWN, K_r


def restart(event):
    if event.type == KEYDOWN:
        if event.key == K_r:
            return True

    return False
