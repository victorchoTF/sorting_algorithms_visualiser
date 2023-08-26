from random import shuffle
from typing import List, Optional
from pygame import event, display, quit as pg_quit
from app_operations.restart import restart
from app_operations.quit_loop import quit_loop
from screen import screen
from app_operations.gen_surf_rect_list import gen_surf_rect_list


def selection_sort(array: List[int]) -> List[int]:  # O(n^2)
    for i, num in enumerate(array):
        min_num = num
        min_idx = i
        for j in range(i + 1, len(array)):

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            if min_num > array[j]:
                min_num = array[j]
                min_idx = j

            surf_rect_array = gen_surf_rect_list(array, j, pivot=min_idx)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

        array[i], array[min_idx] = array[min_idx], array[i]

        surf_rect_array = gen_surf_rect_list(array, min_idx)
        for surf, rect in surf_rect_array:
            screen.blit(surf, rect)

        display.update()

    return array


def bubble_sort(array: List[int]) -> List[int]:  # O(n^2)
    counter = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(len(array) - 1 - counter):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                is_sorted = False

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, idx, idx + 1)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

        counter += 1

    return array


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

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, idx, idx + 1)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

        if not swapped:
            break

        swapped = False
        end = end - 1
        for idx in range(end - 1, start - 1, -1):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                swapped = True

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, idx, idx + 1)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

        start = start + 1

    return array


def insertion_sort(array: List[int]) -> List[int]:  # O(n^2)
    for i in range(1, len(array)):
        for e in event.get():
            if quit_loop(e):
                pg_quit()
                exit()
            if restart(e):
                raise StopIteration

        screen.fill("#DEBA69")
        surf_rect_array = gen_surf_rect_list(array, i)
        for surf, rect in surf_rect_array:
            screen.blit(surf, rect)

        display.update()
        for j in range(i, 0, -1):
            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

                screen.fill("#DEBA69")
                surf_rect_array = gen_surf_rect_list(array, j - 1)
                for surf, rect in surf_rect_array:
                    screen.blit(surf, rect)

                display.update()
                continue
            break

    return array


def quick_sort(array: List[int], start: int = 0, end: int = -1) -> List[int]:  # O(n^2) {avg_case: O(n*log(n))
    end = end if end != -1 else len(array) - 1

    if start >= end:
        return array

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        for e in event.get():
            if quit_loop(e):
                pg_quit()
                exit()
            if restart(e):
                raise StopIteration

        screen.fill("#DEBA69")
        if array[left] > array[pivot] > array[right]:
            array[left], array[right] = array[right], array[left]

        if array[left] <= array[pivot]:
            left += 1

        if array[right] >= array[pivot]:
            right -= 1

        surf_rect_array = gen_surf_rect_list(array, left, right, pivot)
        for surf, rect in surf_rect_array:
            screen.blit(surf, rect)

        display.update()

    array[pivot], array[right] = array[right], array[pivot]

    for e in event.get():
        if quit_loop(e):
            pg_quit()
            exit()
        if restart(e):
            raise StopIteration

    screen.fill("#DEBA69")
    surf_rect_array = gen_surf_rect_list(array, left, right, pivot)
    for surf, rect in surf_rect_array:
        screen.blit(surf, rect)

    display.update()

    array = quick_sort(array, start, right - 1)
    array = quick_sort(array, left, end)

    return array


def merge_sort(array: List[int], left: int = 0, right: int = -1) -> Optional[List[int]]:  # O(n*log(n))
    def merge(start, end):
        nonlocal mid
        second_start = mid + 1

        if array[mid] <= array[second_start]:
            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, start, second_start)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()
            return

        while start <= mid and second_start <= end:
            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, start, second_start)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

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

    right = right if right != -1 else len(array) - 1

    if left >= right:
        return

    mid = left + (right - left) // 2

    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)

    merge(left, right)

    return array


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

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, j - 1)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()
            while j > start and array[j] < array[j - 1]:
                for e in event.get():
                    if quit_loop(e):
                        pg_quit()
                        exit()
                    if restart(e):
                        raise StopIteration
                screen.fill("#DEBA69")
                surf_rect_array = gen_surf_rect_list(array, j - 1)
                for surf, rect in surf_rect_array:
                    screen.blit(surf, rect)

                display.update()
                array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1

    def merge():
        left_size, right_size = mid - left + 1, right - mid
        left_arr = [array[left + i] for i in range(left_size)]
        right_arr = [array[mid + i + 1] for i in range(right_size)]

        i, j, k = 0, 0, left

        while i < left_size and j < right_size:
            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, pivot=k)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

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

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, pivot=k)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

        while j < right_size:
            array[k] = right_arr[j]
            j += 1
            k += 1

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, pivot=k)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

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

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, largest, index)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

            heapify(n, largest)

    N = len(array)

    for idx in range((N // 2) - 1, -1, -1):
        heapify(N, idx)

        for e in event.get():
            if quit_loop(e):
                pg_quit()
                exit()
            if restart(e):
                raise StopIteration

    for idx in range(N - 1, 0, -1):
        array[idx], array[0] = array[0], array[idx]
        heapify(idx, 0)

        for e in event.get():
            if quit_loop(e):
                pg_quit()
                exit()
            if restart(e):
                raise StopIteration

    return array


def radix_sort(array: List[int]) -> List[int]:  # O(max_num_digits * (n + base(10))
    def counting_sort():
        n = len(array)

        result = [0] * n
        count = [0] * 10

        for i in range(n):
            index = array[i] // digit
            count[index % 10] += 1

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, i)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = array[i] // digit
            result[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, i)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

        for i in range(n):
            array[i] = result[i]

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, i)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()

    max_num = max(array)

    digit = 1
    while max_num / digit >= 1:
        counting_sort()
        digit *= 10

    return array


def shell_sort(array: List[int]) -> List[int]:  # O(n^(3/2))
    gap = len(array) // 2

    while gap > 0:
        j = gap
        while j < len(array):
            i = j - gap

            for e in event.get():
                if quit_loop(e):
                    pg_quit()
                    exit()
                if restart(e):
                    raise StopIteration

            screen.fill("#DEBA69")
            surf_rect_array = gen_surf_rect_list(array, i, j)
            for surf, rect in surf_rect_array:
                screen.blit(surf, rect)

            display.update()
            while i >= 0:
                if array[i + gap] > array[i]:
                    break

                array[i + gap], array[i] = array[i], array[i + gap]

                for e in event.get():
                    if quit_loop(e):
                        pg_quit()
                        exit()
                    if restart(e):
                        raise StopIteration

                screen.fill("#DEBA69")
                surf_rect_array = gen_surf_rect_list(array, j, pivot=i)
                for surf, rect in surf_rect_array:
                    screen.blit(surf, rect)

                display.update()

                i -= gap

            j += 1
        gap //= 2

    return array


def shuffle_list(array: List[int]) -> List[int]:
    shuffle(array)

    return array
