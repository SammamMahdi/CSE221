import random

input = open("input6.txt", "r")
output = open("output6.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
n = int(lines[0].split()[0])
arr = [int(i) for i in lines[1].split()]
m = int(lines[2].split()[0])
ks = [int(i) for i in lines[3:]]


def kth_smallest(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        pivot_index = get_pivot(arr, left, right)
        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index < k - 1:
            left = pivot_index + 1
        else:
            right = pivot_index - 1


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
    output.write("\n".join(out))
    output.close()


out = [kth_smallest(arr, k) for k in ks]
write_to_file(out, output)
