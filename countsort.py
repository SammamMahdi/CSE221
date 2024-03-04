def count_sort(arr):
    k = find_max(arr)
    out = [0] * len(arr)
    count = [0] * (k + 1)
    for i in arr:
        count[i] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        count[arr[i]] -= 1
        out[count[arr[i]]] = arr[i]
    return out


def find_max(arr):
    if len(arr) < 2:
        return arr[0]
    left = find_max(arr[: len(arr) // 2])
    right = find_max(arr[len(arr) // 2 :])
    return max(left, right)
  
arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(count_sort(arr))
