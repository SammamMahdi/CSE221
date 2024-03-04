def max(arr):
    return arr[1]


def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(arr, i, length):  # sink algorithm # O(lgn)
    L = left(i)
    R = right(i)
    largest = i
    if L < length:
        if arr[L] > arr[i]:
            largest = L
    if R < length:
        if arr[R] > arr[largest]:
            largest = R
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, length)
    return arr


def min_heapify(arr, i, length):
    L = left(i)
    R = right(i)
    smallest = i
    if L < length:
        if arr[L] < arr[i]:
            smallest = L
    if R < length:
        if arr[R] < arr[smallest]:
            smallest = R
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest, length)
    return arr


def heap_increase_key(arr, i, key):  # Swim algorithm
    if key < arr[i]:
        return  # error new key smaller than current key
    arr[i] = key
    while i > 1 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)


def max_heap_insert(arr, key):
    arr += [key]
    i = len(arr) - 1
    # heap_increase_key(arr,i,key)
    while i > 1 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)


def build_max_heap(arr):
    for i in range(len(arr) // 2, 0, -1):
        max_heapify(arr, i, len(arr))


def build_min_heap(arr):
    for i in range(len(arr) // 2, 0, -1):
        min_heapify(arr, i, len(arr))


def heap_sort(arr, reverse=False):  # O(nlgn)
    if reverse:
        build_min_heap(arr)
        for i in range(len(arr), 1, -1):
            arr[1], arr[i - 1] = arr[i - 1], arr[1]
            arr = min_heapify(arr, 1, i - 1)
        return arr
    build_max_heap(arr)
    for i in range(len(arr), 1, -1):
        arr[1], arr[i - 1] = arr[i - 1], arr[1]
        arr = max_heapify(arr, 1, i - 1)
    return arr
