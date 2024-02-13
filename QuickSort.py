def qsort(arr, left, right):
    if left < right:
        p = get_pivot(arr, left, right)
        qsort(arr, left, p - 1)
        qsort(arr, p + 1, right)


def get_pivot(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


arr = [111, 22, 11, 88, 66, 55, 77, 33, 44, 99]
qsort(arr, 0, len(arr) - 1)
print(arr)
