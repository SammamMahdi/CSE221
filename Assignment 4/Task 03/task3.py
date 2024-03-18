input = open("input3.txt", "r")
output = open("output3.txt", "w")
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
        if not graph[v]:
            graph[v] = []
        graph[v].append(u)
    return graph


def DFS(s):
    state[s] = 1
    output.write(f"{s} ")
    for v in graph[s]:
        if state[v] == 0:
            DFS(v)
            state[s] = 2


graph = create_graph(vertex, e, edges)
state = [0] * (len(graph) + 1)
DFS(1)
output.close()
