input = open("input3.txt", "r")
output = open("output3.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
n = int(lines[0])


def max_tasks(lines, n):
    tasks = [tuple(k.split()) for k in lines[1:]]
    tasks.sort(key=lambda x: int(x[1]))
    endtime = 0
    max_tasks = []
    count = 0
    for i in range(n):
        if int(tasks[i][0]) >= endtime:
            max_tasks.append(tasks[i])
            count += 1
            endtime = int(tasks[i][1])
    return str(count), max_tasks


def write_to_file(out, output):
    output.write(f"{out[0]}\n")
    out1 = "\n".join([f"{i[0]} {i[1]}" for i in out[1]])
    output.write(out1)
    output.close()


out = max_tasks(lines, n)
write_to_file(out, output)
