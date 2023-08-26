from typing import List
from app_operations.loop import loop


def selection_sort(array: List[int]) -> List[int]:  # O(n^2)
    for i, num in enumerate(array):
        min_num = num
        min_idx = i
        for j in range(i + 1, len(array)):

            if min_num > array[j]:
                min_num = array[j]
                min_idx = j

            loop(array, j, pivot=min_idx)

        array[i], array[min_idx] = array[min_idx], array[i]

        loop(array, min_idx)

    return array
