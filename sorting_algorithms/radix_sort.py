from typing import List
from app_operations.loop import loop


def radix_sort(array: List[int]) -> List[int]:  # O(max_num_digits * (n + base(10))
    def counting_sort():
        n = len(array)

        result = [0] * n
        count = [0] * 10

        for i in range(n):
            index = array[i] // digit
            count[index % 10] += 1

            loop(array, i)

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = array[i] // digit
            result[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1

            loop(array, i)

        for i in range(n):
            array[i] = result[i]

            loop(array, i)

    max_num = max(array)

    digit = 1
    while max_num / digit >= 1:
        counting_sort()
        digit *= 10

    return array
