import sys

import rendering as rd


def swap(a: list[int], i: int, j: int) -> None:
    """Swaps the elements of `a` at indices `i` and `j`."""
    a[i], a[j] = a[j], a[i]


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


def insertion_sort(array: list[int]) -> None:
    """Continually sorts in-place as more numbers are looked at."""
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j - 1, j)
            j -= 1
            rd.render(array, j)
    rd.render(array)

def heapify(array, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and array[largest] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        swap(array, i, largest)
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        rd.render(array, i)
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        swap(array, i, 0)
        rd.render(array, i)
        heapify(array, i, 0)
    rd.render(array)

def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        rd.render(array, j)
        if array[j] <= x:
            i += 1
            rd.render(array, i)
            swap(array, i, j)
            rd.render(array, j)
    rd.render(array, i + 1)
    swap(array, i + 1, r)
    rd.render(array, r)
    return i + 1

def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)

def partition2(array, left, right):
    x = array[left]
    while left < right:
        rd.render(array, right)
        while left < right and array[right] > array[left]:
            right -= 1
            rd.render(array, right)
        array[left] = array[right]
        rd.render(array, left)
        while left < right and array[left] < array[right]:
            left += 1
            rd.render(array, left)
        array[right] = array[left]
    array[left] = x
    return left

def quicksort2(array, left, right):
    if left < right:
        p = partition2(array, left, right)
        quicksort2(array, left, p - 1)
        quicksort2(array, p + 1, right)
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
    for k in range(p, r + 1):
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
    rd.render(array)


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
        rd.render(b, c[array[j]] - 1)
        c[array[j]] -= 1

    rd.render(b)
    return b

def selection_sort(array: list[int]):
    """"""
    n = len(array)
    for i in range(n - 1):
        min_index = i
        rd.render(array, i)
        for j in range(i + 1, n):
            rd.render(array, j)
            if array[j] < array[min_index]:
                min_index = j
        rd.render(array, min_index)
        swap(array, i, min_index)
        rd.render(array, i)
    rd.render(array)
