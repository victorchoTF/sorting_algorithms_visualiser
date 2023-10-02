from time import sleep
from typing import List, Tuple
from pygame import Surface, Rect
from app_operations.gen_surf_rect_list import gen_surf_rect_list
from handlers.app_mode import AppMode
from screens.list_data import ListData
from screens.presentation_screen import PresentationScreen


def handle_presentation_screen(presentation_screen: PresentationScreen
                               ) -> Tuple[AppMode, List[int], List[Tuple[Surface, Rect]]]:
    try:
        num_list, surf_rect_list = presentation_screen.loop()
    except StopIteration:
        num_list: List[int] = [num for num in range(1, ListData.list_size)]

        return AppMode.MAIN_SCREEN, num_list, gen_surf_rect_list(num_list)

    return AppMode.PRESENTATION_SCREEN, num_list, surf_rect_list
