import random

input = open("input5.txt", "r")
output = open("output5.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
n = int(lines[0])
arr = [int(i) for i in lines[1].split()]


def qsort(arr, left, right):
    if left < right:
        p = get_pivot(arr, left, right)
        qsort(arr, left, p - 1)
        qsort(arr, p + 1, right)


def get_pivot(arr, left, right):
    i = left
    j = right - 1
    p = random.randint(left, right)
    arr[p], arr[right] = arr[right], arr[p]
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


def write_to_file(out, output):
    out = [str(i) for i in out]
    output.write(" ".join(out))
    output.close()


qsort(arr, 0, n - 1)
write_to_file(arr, output)
