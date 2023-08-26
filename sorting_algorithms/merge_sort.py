from typing import List, Optional

from app_operations.loop import loop


def merge_sort(array: List[int], left: int = 0, right: int = None) -> Optional[List[int]]:  # O(n*log(n))
    def merge(start, end):
        nonlocal mid
        second_start = mid + 1

        if array[mid] <= array[second_start]:
            loop(array, start, second_start)
            return

        while start <= mid and second_start <= end:
            loop(array, start, second_start)

            if array[start] <= array[second_start]:
                start += 1
                continue

            value = array[second_start]
            index = second_start

            while index != start:
                array[index] = array[index - 1]
                index -= 1

            array[start] = value

            start += 1
            mid += 1
            second_start += 1

    right = right if right is not None else len(array) - 1

    if left >= right:
        return

    mid = left + (right - left) // 2

    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)

    merge(left, right)

    return array
