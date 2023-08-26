from typing import List
from app_operations.loop import loop


def heap_sort(array: List[int]) -> List[int]:  # O(n*log(n))
    def heapify(n, index):
        largest = index
        left, right = 2 * index + 1, 2 * index + 2

        if left < n and array[largest] < array[left]:
            largest = left

        if right < n and array[largest] < array[right]:
            largest = right

        if largest != index:
            array[largest], array[index] = array[index], array[largest]

            loop(array, largest, index)

            heapify(n, largest)

    N = len(array)

    for idx in range((N // 2) - 1, -1, -1):
        heapify(N, idx)

    for idx in range(N - 1, 0, -1):
        array[idx], array[0] = array[0], array[idx]
        heapify(idx, 0)

    return array
