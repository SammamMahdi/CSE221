input = open("input1.txt", "r")
output = open("output1.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
n = int(lines[0])
arr = [int(i) for i in lines[1].split()]


def mergesort(arr, n):
    if n <= 1:
        return arr
    else:
        mid = n // 2
        a1 = mergesort(arr[:mid], mid)
        a2 = mergesort(arr[mid:], n - mid)
        return merge(a1, a2)


def merge(a1, a2):
    merged = [0] * (len(a1) + len(a2))
    i = j = k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            merged[k] = a1[i]
            i += 1
        else:
            merged[k] = a2[j]
            j += 1
        k += 1
    while i < len(a1):
        merged[k] = a1[i]
        i += 1
        k += 1

    while j < len(a2):
        merged[k] = a2[j]
        j += 1
        k += 1
    return merged


def write_to_file(out, output):
    out = [str(i) for i in out]
    output.write(" ".join(out))
    output.close()


out = mergesort(arr, n)
write_to_file(out, output)
