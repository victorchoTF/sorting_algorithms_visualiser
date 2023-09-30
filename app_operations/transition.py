from typing import Callable
from pygame import draw, display
from screens.screen_data import screen, SCREEN_WIDTH, SCREEN_HEIGHT, clock


def transition(draw_text: Callable, start: int, direction: str) -> None:
    transit = True
    radius = start
    while transit:
        clock.tick(60)
        screen.fill("#DEBA69")
        draw_text()
        draw.circle(screen, "#DEBA69", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), SCREEN_HEIGHT, radius)
        if direction == "+":
            if radius <= SCREEN_HEIGHT:
                radius += 10
            else:
                transit = False
        else:
            if radius >= 1:
                radius -= 10
            else:
                transit = False

        display.flip()
