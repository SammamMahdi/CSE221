inputs = open("input4.txt", "r")
output = open("output4.txt", "w")
content = inputs.read()
lines = [i for i in content.split("\n")]
n = int(lines[0])
lines = lines[1:]
data = []
for i in range(n):
    data.append(
        (
            i,
            lines[i].split(" will departure for ")[0],
            *lines[i].split(" will departure for ")[1].split(" at "),
        )
    )


def sort(data, n):
    data = name_sort(data, n)
    data = departure_sort(data, n)
    return data


def name_sort(data, n):
    for i in range(n - 1):
        minm = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
        minm_idx = 0
        for j in range(i + 1, n):
            if data[j][1] < minm:
                minm = data[j][1]
                minm_idx = j
        if data[i][1] > minm:
            data[i], data[minm_idx] = data[minm_idx], data[i]
    return data


def departure_sort(data, n):
    for i in range(n - 1):
        maxm = "00:00"
        maxm_idx = 0
        for j in range(i + 1, n):
            if data[i][1] != data[j][1]:
                break
            elif data[j][3] > maxm:
                maxm = data[j][3]
                maxm_idx = j
        if data[i][3] < maxm:
            data[i], data[maxm_idx] = data[maxm_idx], data[i]
    return data


def write_str(data, n):
    out = [
        f"{data[i][1]} will departure for {data[i][2]} at {data[i][3]}"
        for i in range(n)
    ]
    return "\n".join(out)


output.write(write_str(sort(data, n), n))
output.close()
