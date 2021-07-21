import sys

import rendering as rd


def swap(a: list[int], i: int, j: int) -> None:
    """Swaps the elements of `a` at indices `i` and `j`."""
    a[i], a[j] = a[j], a[i]


def insertion_sort(array: list[int]) -> None:
    """Continually sorts in-place as more numbers are looked at."""
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j - 1, j)
            j -= 1
            rd.render(array, j)
    rd.render(array)


def bubble_sort(array: list[int]) -> None:
    """"""
    is_sorted = False
    last_unsorted = len(array) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(last_unsorted):
            if (array[i] > array[i + 1]):
                swap(array, i, i + 1)
                is_sorted = False
            rd.render(array, i + 1)
        last_unsorted -= 1
    rd.render(array)


def merge(array: list[int], p: int, q: int, r: int) -> list[int]:
    n1 = q - p + 1
    n2 = r - q

    left = [None] * (n1 + 1)
    right = [None] * (n2 + 1)

    for i in range(n1):
        left[i] = array[p + i]

    for j in range(n2):
        right[j] = array[q + 1 + j]

    left[n1] = sys.maxsize
    right[n2] = sys.maxsize

    i = 0
    j = 0
    for k in range(r + 1):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        rd.render(array, highlight=k)
    return array


def merge_sort(array: list[int], p: int, r: int) -> None:
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)


def counting_sort(array: list[int]) -> None:
    b = [0] * len(array)
    k = max(array)

    c = [0] * (k + 1)
    n = len(array)

    for j in range(n):
        c[array[j]] += 1
        rd.render(array, j)

    for i in range(1, k + 1):
        c[i] = c[i - 1] + c[i]

    for j in range(n - 1, -1, -1):
        b[c[array[j]] - 1] = array[j]
        c[array[j]] -= 1
        rd.render(b, c[array[j]] - 1)

    return b
