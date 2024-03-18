input = open("input2.txt", "r")
output = open("output2.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
n = int(lines[0])
arr = [int(i) for i in lines[1].split()]


def find_max(arr, n):
    if n < 2:
        return arr[0]
    m = n // 2
    left = find_max(arr[:m], m)
    right = find_max(arr[m:], n - m)
    return max(right, left)


def write_to_file(out, output):
    out = str(out)
    output.write(out)
    output.close()


out = find_max(arr, n)
write_to_file(out, output)
