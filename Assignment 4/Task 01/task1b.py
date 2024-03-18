input = open("input1b.txt", "r")
output = open("output1b.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]

vertex, e = [int(i) for i in lines[0].split()]
edges = [(int(u), int(v), int(w)) for u, v, w in [i.split() for i in lines[1:]]]


def create_graph_list(vertex, e, edges):
    graph = [None] * (vertex + 1)
    for edge in edges:
        u, v, w = edge
        if not graph[u]:
            graph[u] = []
        graph[u].append((v, w))
    return graph


def write_to_file(output, graph):
    for i in range(len(graph)):
        if graph[i]:
            output.write(f"{i} : {' '.join([f'({x},{y})' for x, y in graph[i]])}\n")
        else:
            output.write(f"{i} : \n")
    output.close()


graph = create_graph_list(vertex, e, edges)
write_to_file(output, graph)
