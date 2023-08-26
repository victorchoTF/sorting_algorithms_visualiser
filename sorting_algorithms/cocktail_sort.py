from typing import List
from app_operations.loop import loop


def cocktail_sort(array: List[int]) -> List[int]:  # O(n^2)
    swapped = True
    start = 0
    end = len(array) - 1
    while swapped:
        swapped = False
        for idx in range(start, end):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                swapped = True

            loop(array, idx, idx + 1)

        if not swapped:
            break

        swapped = False
        end = end - 1
        for idx in range(end - 1, start - 1, -1):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                swapped = True

            loop(array, idx, idx + 1)

        start = start + 1

    return array
