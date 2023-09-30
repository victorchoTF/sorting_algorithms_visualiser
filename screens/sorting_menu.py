from typing import Dict, Tuple, List, Callable

from pygame import Surface, Rect

from app_operations.gen_surf_rect_list import gen_surf_rect_list
from app_operations.shuffle_list import shuffle_list
from screens.list_data import ListData
from screens.button import Button
from screens.menu import Menu
from screens.screen_data import SCREEN_WIDTH, SCREEN_HEIGHT
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.cocktail_sort import cocktail_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.radix_sort import radix_sort
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.shell_sort import shell_sort
from sorting_algorithms.tin_sort import tin_sort


class SortingMenu(Menu):
    BUTTONS_TO_CREATE: Dict[str, Tuple[int, int]] = {
        "Selection Sort": (SCREEN_WIDTH - 1850, SCREEN_HEIGHT - 990),
        "Bubble Sort": (SCREEN_WIDTH - 1480, SCREEN_HEIGHT - 990),
        "Cocktail Sort": (SCREEN_WIDTH - 1130, SCREEN_HEIGHT - 990),
        "Insertion Sort": (SCREEN_WIDTH - 760, SCREEN_HEIGHT - 990),
        "Merge Sort": (SCREEN_WIDTH - 390, SCREEN_HEIGHT - 990),
        "Quick Sort": (SCREEN_WIDTH - 1830, SCREEN_HEIGHT - 920),
        "Tin Sort": (SCREEN_WIDTH - 1510, SCREEN_HEIGHT - 920),
        "Heap Sort": (SCREEN_WIDTH - 1250, SCREEN_HEIGHT - 920),
        "Radix Sort": (SCREEN_WIDTH - 960, SCREEN_HEIGHT - 920),
        "Shell Sort": (SCREEN_WIDTH - 640, SCREEN_HEIGHT - 920),
        "Shuffle": (SCREEN_WIDTH - 320, SCREEN_HEIGHT - 920),
    }

    def __init__(self, title: str, title_pos: Tuple[int, int], button_pos: Tuple[int, int],
                 size: Tuple[int, int]) -> None:
        super().__init__(title, title_pos, button_pos, size)

        self.buttons = SortingMenu.create_buttons(SortingMenu.BUTTONS_TO_CREATE)
        print(self.buttons)

        self.buttons_mapper = self.create_buttons_mapper()

    @staticmethod
    def create_buttons(buttons_to_create: Dict[str, Tuple[int, int]]) -> Tuple[Button, ...]:
        buttons = tuple(Button(text, position)
                        for text, position in buttons_to_create.items())
        print(buttons_to_create)
        return buttons

    def create_buttons_mapper(self) -> Dict[Button, Callable]:
        functions = (selection_sort, bubble_sort, cocktail_sort, insertion_sort,
                     merge_sort, quick_sort, tin_sort, heap_sort, radix_sort,
                     shell_sort, shuffle_list)

        button_mapper = {
            button: lambda x, func=func: func(x)
            for button, func in zip(self.buttons, functions)
        }

        return button_mapper

    def buttons_check(self, num_list: List[int],
                      surf_rect_list: List[Tuple[Surface, Rect]]
                      ) -> Tuple[List[int], List[Tuple[Surface, Rect]]]:
        for button in self.buttons:
            if button.is_clicked():
                try:
                    num_list = self.buttons_mapper[button](num_list)
                except StopIteration:
                    num_list = [num for num in range(1, ListData.list_size)]

                surf_rect_list = gen_surf_rect_list(num_list)

        return num_list, surf_rect_list
