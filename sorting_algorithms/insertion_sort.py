from typing import List
from app_operations.loop import loop


def insertion_sort(array: List[int]) -> List[int]:  # O(n^2)
    for i in range(1, len(array)):
        loop(array, i)

        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

                loop(array, j - 1)

                continue
            break

    return array
