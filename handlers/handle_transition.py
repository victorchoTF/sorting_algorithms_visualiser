from typing import List, Tuple
from pygame import Surface, Rect
from screens.screen_data import SCREEN_HEIGHT
from screens.title_screen import TitleScreen
from screens.main_screen import MainScreen
from app_operations.transition import transition
from handlers.app_mode import AppMode


def handle_transition(title_screen: TitleScreen, main_screen: MainScreen,
                      surf_rect_list: List[Tuple[Surface, Rect]]) -> Tuple[AppMode, None]:
    transition(title_screen.draw, 1, "+")
    transition(lambda: main_screen.draw(surf_rect_list), SCREEN_HEIGHT, "-")

    return AppMode.MAIN_SCREEN, None
