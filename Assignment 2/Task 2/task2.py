input = open("input2.txt", "r")
output = open("output2.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
len1 = int(lines[0])
arr1 = [int(i) for i in lines[1].split()]
len2 = int(lines[2])
arr2 = [int(i) for i in lines[3].split()]


# nlog(n)
def merge_sort1(arr1, arr2, len1, len2):
    merged = arr1 + arr2
    merged.sort()
    # merged = merged.sort()
    return merged


# n
def merge_sort2(arr1, arr2, len1, len2):
    empty = [0] * (len1 + len2)
    k = i = j = 0
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            empty[k] = arr1[i]
            i += 1
        else:
            empty[k] = arr2[j]
            j += 1
        k += 1
    while i < len1:
        empty[k] = arr1[i]
        i += 1
        k += 1
    while j < len2:
        empty[k] = arr2[j]
        j += 1
        k += 1
    return empty


def write_to_file(out, output):
    out = [str(i) for i in out]
    output.write(" ".join(out))


out1 = merge_sort1(arr1, arr2, len1, len2)
out2 = merge_sort2(arr1, arr2, len1, len2)
write_to_file(out1, output)
output.write("\n")
write_to_file(out2, output)
output.close()
