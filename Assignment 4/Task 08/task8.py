input = open("input8.txt", "r")
output = open("output8.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]
t = int(lines.pop(0))


def create_graph(v, edges):
    graph = [None] * (v + 2)
    for edge in edges:
        u, v = edge
        if not graph[u]:
            graph[u] = []
        graph[u].append(v)
        if not graph[v]:
            graph[v] = []
        graph[v].append(u)
    return graph


def BFS(graph, s, vertex):
    Q = []
    type = {}
    count = [0, 0]
    state = [0] * (vertex + 2)
    Q.append(s)
    state[s] = 1
    type[s] = 0
    count[type[s]] += 1
    while Q:
        u = Q.pop(0)
        if graph[u]:
            state[u] = 1
            for v in graph[u]:
                if state[v] == 0:
                    type[v] = 1 - type[u]
                    count[type[v]] += 1
                    Q.append(v)
                    state[v] = 1
            state[u] = 2
    return max(count)


for i in range(t):
    vertex = int(lines.pop(0))
    edges = []
    for j in range(vertex):
        u, v = [int(i) for i in lines.pop(0).split()]
        edges.append((u, v))
    maxm = 0
    graph = create_graph(vertex, edges)
    maxm = BFS(graph, 1, vertex)
    output.write(f"Case #{i + 1}: {maxm}\n")
