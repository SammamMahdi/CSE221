input = open("input5.txt", "r")
output = open("output5.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]

vertex, e, destination = [int(i) for i in lines[0].split()]
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


def BFS(graph, s, vertex):
    Q = []
    state = [0] * (vertex + 1)
    distance = [0] * (vertex + 1)
    parent = [0] * (vertex + 1)
    Q.append(s)
    state[s] = 1
    while Q:
        u = Q.pop(0)
        if graph[u]:
            state[u] = 1
            for v in graph[u]:
                if state[v] == 0:
                    Q.append(v)
                    state[v] = 1
                    distance[v] = distance[u] + 1
                    parent[v] = u
            state[u] = 2
    parent[s] = -1
    return parent, distance


def find_path(parent, Destination):
    if parent[Destination] == -1:
        output.write(f"Shortest Path: {Destination} ")
        return
    else:
        find_path(parent, parent[Destination])
        output.write(f"{Destination} ")


graph = create_graph(vertex, e, edges)
parent, distance = BFS(graph, 1, vertex)
output.write(f"Time: {distance[destination]}\n")
find_path(parent, destination)
output.close()
