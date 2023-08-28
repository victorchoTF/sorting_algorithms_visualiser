from pygame import init, display, FULLSCREEN, time

CAPTION = "SortingAlgorithmsVisualiser"

init()

info = display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN)
display.set_caption(CAPTION)
clock = time.Clock()
