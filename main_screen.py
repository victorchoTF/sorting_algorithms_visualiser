from typing import Tuple, List, Dict
from pygame import font, Surface, Rect
from button import Button
from screen import screen, SCREEN_WIDTH, SCREEN_HEIGHT
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
from app_operations.shuffle_list import shuffle_list
from app_operations.gen_surf_rect_list import gen_surf_rect_list


class MainScreen:
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
        "Shuffle": (SCREEN_WIDTH - 320, SCREEN_HEIGHT - 920)
    }

    def __init__(self) -> None:
        self.title_surf, self.title_rect = self.create_title()

        self.buttons_surf, self.buttons_rect = self.create_buttons_surface_rects()
        self.buttons = self.create_buttons()

        self.sorting_map = self.create_sorting_map()

    @staticmethod
    def create_title() -> Tuple[Surface, Rect]:
        title_font = font.Font(None, 100)
        title_surf = title_font.render("Sorting Algorithms Visualiser", True, "#008080")
        title_rect = title_surf.get_rect(midtop=(SCREEN_WIDTH // 2, 10))
        return title_surf, title_rect

    @staticmethod
    def create_buttons_surface_rects() -> Tuple[Surface, Rect]:
        buttons_surf = Surface((SCREEN_WIDTH, 230))
        buttons_surf.fill("#DEBA69")
        buttons_surf.set_alpha(220)
        buttons_rect = buttons_surf.get_rect(topleft=(0, 0))
        buttons_rect.midtop = SCREEN_WIDTH // 2, 0
        return buttons_surf, buttons_rect

    @staticmethod
    def create_buttons() -> Tuple[Button, ...]:
        buttons = tuple(Button(sort_type, position)
                        for sort_type, position in MainScreen.BUTTONS_TO_CREATE.items())

        return buttons

    def create_sorting_map(self):
        functions = (
            selection_sort, bubble_sort, cocktail_sort, insertion_sort,
            merge_sort, quick_sort, tin_sort, heap_sort, radix_sort, shell_sort,
            shuffle_list
        )
        sorting_map = {
            button: lambda x, func=func: func(x)
            for button, func in zip(self.buttons, functions)
        }
        return sorting_map

    def draw(self, surf_rect_list: List[Tuple[Surface, Rect]]) -> None:
        def buttons_draw() -> None:
            for button in self.buttons:
                button.draw()

        for surf, rect in surf_rect_list:
            screen.blit(surf, rect)

        screen.blit(self.buttons_surf, self.buttons_rect)

        screen.blit(self.title_surf, self.title_rect)

        buttons_draw()

    def buttons_check(self, num_list: List[int],
                      surf_rect_list: List[Tuple[Surface, Rect]]) -> Tuple[List[int], List[Tuple[Surface, Rect]]]:
        for button in self.buttons:
            if button.is_clicked():
                try:
                    num_list = self.sorting_map[button](num_list)
                except StopIteration:
                    num_list = [num for num in range(1, 212)]

                surf_rect_list = gen_surf_rect_list(num_list)

        return num_list, surf_rect_list
