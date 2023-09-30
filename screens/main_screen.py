from typing import Tuple, List
from pygame import Surface, Rect
from screens.menus.list_size_menu import ListSizeMenu
from screens.screen_data import screen, SCREEN_WIDTH, SCREEN_HEIGHT
from screens.menus.sorting_menu import SortingMenu


class MainScreen:
    def __init__(self) -> None:
        self.sorting_menu = SortingMenu("Sorting Algorithms Project", (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, 0),
                                        (SCREEN_WIDTH, 230))

        self.list_size_menu = ListSizeMenu("Choose List Length: ", (SCREEN_WIDTH // 4, SCREEN_HEIGHT - 90),
                                           (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 115), (SCREEN_WIDTH, 115))

    def draw(self, surf_rect_list: List[Tuple[Surface, Rect]]) -> None:
        for surf, rect in surf_rect_list:
            screen.blit(surf, rect)

        self.sorting_menu.draw()
        self.list_size_menu.draw()

        screen.blit(*self.sorting_menu.title)
        screen.blit(*self.list_size_menu.title)
