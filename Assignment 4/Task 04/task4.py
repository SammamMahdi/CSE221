input = open("input4.txt", "r")
output = open("output4.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]

vertex, e = [int(i) for i in lines[0].split()]
edges = [(int(u), int(v)) for u, v in [i.split() for i in lines[1:]]]


def create_graph(v, e, edges):
    graph = [None] * (v + 1)
    for edge in edges:
        u, v = edge
        if not graph[u]:
            graph[u] = []
        graph[u].append(v)
    return graph


def cycle_detect(s):
    state[s] = 1
    if not graph[s]:
        state[s] = 2
        return
    for v in graph[s]:
        if state[v] == 0:
            cycle_detect(v)
            state[s] = 2
        elif state[v] == 2:
            return "YES"
    return "NO"


graph = create_graph(vertex, e, edges)
state = [0] * (len(graph) + 1)
out = cycle_detect(1)
output.write(out)
output.close()
