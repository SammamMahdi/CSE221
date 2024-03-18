input = open("input1a.txt", "r")
output = open("output1a.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]

v, e = [int(i) for i in lines[0].split()]
edges = [(int(u), int(v), int(w)) for u, v, w in [i.split() for i in lines[1:]]]


def create_graph_matrix(v, e, edges):
    graph = [[str(0)] * (v + 1) for i in range(v + 1)]
    for edge in edges:
        u, v, w = edge
        graph[u][v] = str(w)
    return graph


def write_to_file(output, graph):
    for i in range(len(graph)):
        output.write("  ".join(graph[i][1:]) + "\n")
    output.close()


graph = create_graph_matrix(v, e, edges)
write_to_file(output, graph)
