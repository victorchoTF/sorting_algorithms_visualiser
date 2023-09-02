from typing import Tuple
from app_mode import AppMode
from title_screen import TitleScreen


def handle_title_screen(title_screen: TitleScreen) -> Tuple[AppMode, None]:
    title_screen.draw()

    if title_screen.button.is_clicked():
        return AppMode.TRANSITION, None

    return AppMode.TITLE_SCREEN, None
