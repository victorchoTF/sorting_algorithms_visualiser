from typing import List, Tuple
from pygame import Surface, Rect
from app_mode import AppMode
from main_screen import MainScreen


def handle_main_screen(main_screen: MainScreen, num_list: List[int],
                       surf_rect_list: List[Tuple[Surface, Rect]]) -> Tuple[AppMode, List[int],
                                                                            List[Tuple[Surface, Rect]]]:
    main_screen.draw(surf_rect_list)
    num_list, surf_rect_list = main_screen.buttons_check(num_list, surf_rect_list)

    return AppMode.MAIN_SCREEN, num_list, surf_rect_list
