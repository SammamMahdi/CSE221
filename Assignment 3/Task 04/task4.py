input = open("input4.txt", "r")
output = open("output4.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
n = int(lines[0])
arr = [int(i) for i in lines[1].split()]


def max_square_sum(arr, n):
    if n == 2:
        return arr[0] + arr[1] ** 2
    if n == 1:
        return -999
    mid = n // 2
    lm = max_square_sum(arr[:mid], mid)
    rm = max_square_sum(arr[mid:], n - mid)
    cm = cross_max(arr, mid, n)
    return max(lm, rm, cm)


def cross_max(arr, m, n):
    i = j = m
    maxj = maxi = -999
    while i >= 0:
        if arr[i] > maxi:
            maxi = arr[i]
        i -= 1
    while j <= n - 1:
        if abs(arr[j]) > maxj:
            maxj = abs(arr[j])
        j += 1
    return maxi + maxj**2


def write_to_file(out, output):
    out = str(out)
    output.write(out)
    output.close()


out = max_square_sum(arr, n)
write_to_file(out, output)
