from typing import List
from app_operations.loop import loop


def quick_sort(array: List[int], start: int = 0, end: int = None) -> List[int]:  # O(n^2) {avg_case: O(n*log(n))
    end = end if end is not None else len(array) - 1

    if start >= end:
        return array

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if array[left] > array[pivot] > array[right]:
            array[left], array[right] = array[right], array[left]

        if array[left] <= array[pivot]:
            left += 1

        if array[right] >= array[pivot]:
            right -= 1

        loop(array, left, right, pivot)

    array[pivot], array[right] = array[right], array[pivot]

    loop(array, left, right, pivot)

    array = quick_sort(array, start, right - 1)
    array = quick_sort(array, left, end)

    return array
