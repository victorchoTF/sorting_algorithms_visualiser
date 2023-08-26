from pygame import QUIT, KEYDOWN, K_ESCAPE, K_r


def quit_loop(event):
    if event.type == QUIT:
        return True

    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            return True

    return False


def restart(event):
    if event.type == KEYDOWN:
        if event.key == K_r:
            return True

    return False
