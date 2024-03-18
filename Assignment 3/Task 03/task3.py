input = open("input3.txt", "r")
output = open("output3.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
n = int(lines[0])
arr = [int(i) for i in lines[1].split()]


def mergesort(arr, count=0):
    if len(arr) <= 1:
        return arr, count
    else:
        mid = len(arr) // 2
        a1, count1 = mergesort(arr[:mid])
        a2, count2 = mergesort(arr[mid:])
        return merge(a1, a2, count1 + count2)


def merge(a1, a2, count):
    merged = [0] * (len(a1) + len(a2))
    i = j = k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            merged[k] = a1[i]
            i += 1
        else:
            merged[k] = a2[j]
            j += 1
            count += len(a1) - i
        k += 1
    while i < len(a1):
        merged[k] = a1[i]
        i += 1
        k += 1

    while j < len(a2):
        merged[k] = a2[j]
        j += 1
        k += 1
    return merged, count


def alien_apocalypse(arr, n):
    arr, count = mergesort(arr)
    return count


def write_to_file(out, output):
    out = str(out)
    output.write(out)
    output.close()


out = alien_apocalypse(arr, n)
write_to_file(out, output)
