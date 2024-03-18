input = open("input4.txt", "r")
output = open("output4.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
n, workers = (int(i) for i in lines[0].split())


def max_tasks(lines, n, workers):
    workers = [0] * workers
    tasks = [tuple(k.split()) for k in lines[1:]]
    tasks.sort(key=lambda x: int(x[1]))
    count = 0
    for i in range(n):
        count += select_champion(int(tasks[i][0]), int(tasks[i][1]), workers)
    return str(count)


def select_champion(start, end, workers):
    minm = 9999999
    minm_idx = -1
    for t in range(len(workers)):
        if start - workers[t] >= 0 and start - workers[t] < minm:
            minm = start - workers[t]
            minm_idx = t
    if minm_idx != -1:
        workers[minm_idx] = end
        return 1
    else:
        return 0


out = max_tasks(lines, n, workers)
output.write(out)
output.close()
