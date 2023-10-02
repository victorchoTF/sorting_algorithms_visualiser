from random import shuffle
from typing import List, Tuple
from pygame import Surface, Rect
from app_operations.gen_surf_rect_list import gen_surf_rect_list
from app_operations.shuffle_list import shuffle_list
from screens.list_data import ListData
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.shell_sort import shell_sort
from sorting_algorithms.tin_sort import tin_sort


class PresentationScreen:
    def __init__(self) -> None:
        self.present_algorithms_queue = [merge_sort, quick_sort, heap_sort, tin_sort, shell_sort]

    def loop(self) -> Tuple[List[int], List[Tuple[Surface, Rect]]]:
        ListData.list_size = ListData().divisors_list[-1]

        num_list = shuffle_list([num for num in range(1, ListData.list_size)])
        surf_rect_list = gen_surf_rect_list(num_list)

        shuffle(self.present_algorithms_queue)

        return self.present_algorithms_queue[0](num_list), surf_rect_list
