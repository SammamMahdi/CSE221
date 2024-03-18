input = open("input7.txt", "r")
output = open("output7.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]

vertex = int(lines[0])
edges = [(int(u), int(v)) for u, v in [i.split() for i in lines[1:]]]


def create_graph(v, edges):
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


def DFS(s, max_distance, state, distance=1):
    state[s] = 1
    for v in graph[s]:
        if state[v] == 0:
            if distance > max_distance[1]:
                max_distance[0], max_distance[1], max_distance[2] = max_distance[3], distance, v
            DFS(v, max_distance, state, distance + 1)
            state[s] = 2


# max_distance[0] = [max_start, max_distance, max_end, city]
def find_longest(vertex, graph):
    max_distance = [0, 0, 0, 0]
    for city in range(1, vertex + 1):
        max_distance[3] = city
        state = [0] * (vertex + 1)
        DFS(city, max_distance, state)
    return max_distance[0], max_distance[2]


graph = create_graph(vertex, edges)
result = find_longest(vertex, graph)
output.write(f"{result[0]} {result[1]}")
