from typing import List
from app_operations.loop import loop


def tin_sort(array: List[int]) -> List[int]:  # O(n*log(n))
    MIN_MERGE = 32

    def calc_min_run(n: int) -> int:
        run = 1
        while n >= MIN_MERGE:
            run |= n & 1
            n >>= 1

        return n + run

    def insertion():
        for i in range(start + 1, end + 1):
            j = i

            loop(array, j - 1)

            while j > start and array[j] < array[j - 1]:
                loop(array, j - 1)

                array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1

    def merge():
        left_size, right_size = mid - left + 1, right - mid
        left_arr = [array[left + i] for i in range(left_size)]
        right_arr = [array[mid + i + 1] for i in range(right_size)]

        i, j, k = 0, 0, left

        while i < left_size and j < right_size:
            loop(array, pivot=k)

            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
                k += 1
                continue

            array[k] = right_arr[j]
            j += 1
            k += 1

        while i < left_size:
            array[k] = left_arr[i]
            i += 1
            k += 1

            loop(array, pivot=k)

        while j < right_size:
            array[k] = right_arr[j]
            j += 1
            k += 1

            loop(array, pivot=k)

    N = len(array)
    min_run = calc_min_run(N)

    for start in range(0, N, min_run):
        end = min(start + min_run - 1, N - 1)
        insertion()

    size = min_run
    while size < N:
        for left in range(0, N, 2 * size):
            mid = min(N - 1, left + size - 1)
            right = min(left + 2 * size - 1, N - 1)

            if mid < right:
                merge()

        size *= 2

    return array
