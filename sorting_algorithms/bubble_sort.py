from typing import List
from app_operations.loop import loop


def bubble_sort(array: List[int]) -> List[int]:  # O(n^2)
    counter = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(len(array) - 1 - counter):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                is_sorted = False

            loop(array, idx, idx + 1)

        counter += 1

    return array
