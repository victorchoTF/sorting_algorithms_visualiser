from typing import Tuple, List
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
    def __init__(self) -> None:
        title_font = font.Font(None, 100)
        self.title_surf = title_font.render("Sorting Algorithms Visualiser", True, "#008080")
        self.title_rect = self.title_surf.get_rect(midtop=(SCREEN_WIDTH // 2, 10))

        self.buttons_surf = Surface((SCREEN_WIDTH, 230))
        self.buttons_surf.fill("#DEBA69")
        self.buttons_surf.set_alpha(220)
        self.buttons_rect = self.buttons_surf.get_rect(topleft=(0, 0))
        self.buttons_rect.midtop = SCREEN_WIDTH // 2, 0

        functions = tuple((selection_sort, bubble_sort, cocktail_sort, insertion_sort, merge_sort, quick_sort,
                           tin_sort, heap_sort, radix_sort, shell_sort, shuffle_list))

        self.buttons = MainScreen.create_buttons()

        self.sorting_map = {button: lambda x, func=func: func(x)
                            for button, func in zip(self.buttons, functions)}

    @staticmethod
    def create_buttons() -> Tuple[Button, ...]:
        selection_sort_button = Button("Selection Sort", (SCREEN_WIDTH - 1850, SCREEN_HEIGHT - 990))
        bubble_sort_button = Button("Bubble Sort", (SCREEN_WIDTH - 1480, SCREEN_HEIGHT - 990))
        cocktail_sort_button = Button("Cocktail Sort", (SCREEN_WIDTH - 1130, SCREEN_HEIGHT - 990))
        insertion_sort_button = Button("Insertion Sort", (SCREEN_WIDTH - 760, SCREEN_HEIGHT - 990))
        merge_sort_button = Button("Merge Sort", (SCREEN_WIDTH - 390, SCREEN_HEIGHT - 990))

        quick_sort_button = Button("Quick Sort", (SCREEN_WIDTH - 1830, SCREEN_HEIGHT - 920))
        tin_sort_button = Button("Tin Sort", (SCREEN_WIDTH - 1510, SCREEN_HEIGHT - 920))
        heap_sort_button = Button("Heap Sort", (SCREEN_WIDTH - 1250, SCREEN_HEIGHT - 920))
        radix_sort_button = Button("Radix Sort", (SCREEN_WIDTH - 960, SCREEN_HEIGHT - 920))
        shell_sort_button = Button("Shell Sort", (SCREEN_WIDTH - 640, SCREEN_HEIGHT - 920))
        shuffle_button = Button("Shuffle", (SCREEN_WIDTH - 320, SCREEN_HEIGHT - 920))

        buttons = tuple((selection_sort_button, bubble_sort_button, cocktail_sort_button,
                         insertion_sort_button, merge_sort_button, quick_sort_button,
                         tin_sort_button, heap_sort_button, radix_sort_button,
                         shell_sort_button, shuffle_button))

        return buttons

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
