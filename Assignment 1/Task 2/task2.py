input = open("input2.txt", "r")
output = open("output2.txt", "w")
content = input.read()
inputs = [i for i in content.split("\n")]
length = int(inputs[0])
arr = [i for i in inputs[1].split()]


def bubble_sort(arr, len):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len - 1):
            if int(arr[i]) > int(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return " ".join(arr)


output.write(bubble_sort(arr, length))
output.close()
