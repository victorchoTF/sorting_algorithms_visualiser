from typing import List
from app_operations.loop import loop


def shell_sort(array: List[int]) -> List[int]:  # O(n^(3/2))
    gap = len(array) // 2

    while gap > 0:
        j = gap
        while j < len(array):
            i = j - gap

            loop(array, i, j)

            while i >= 0:
                if array[i + gap] > array[i]:
                    break

                array[i + gap], array[i] = array[i], array[i + gap]

                loop(array, j, pivot=i)

                i -= gap

            j += 1
        gap //= 2

    return array
