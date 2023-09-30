from typing import List, Tuple
from pygame import Surface, Rect
from handlers.app_mode import AppMode
from screens.main_screen import MainScreen


def handle_main_screen(main_screen: MainScreen, num_list: List[int],
                       surf_rect_list: List[Tuple[Surface, Rect]]) -> Tuple[AppMode, List[int],
                                                                            List[Tuple[Surface, Rect]]]:
    main_screen.draw(surf_rect_list)
    num_list, surf_rect_list = main_screen.sorting_menu.buttons_check(num_list, surf_rect_list)
    num_list, surf_rect_list = main_screen.list_size_menu.buttons_check(num_list, surf_rect_list)

    return AppMode.MAIN_SCREEN, num_list, surf_rect_list
