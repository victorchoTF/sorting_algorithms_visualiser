from pygame import QUIT, KEYDOWN, K_ESCAPE


def quit_loop(event):
    if event.type == QUIT:
        return True

    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            return True

    return False
