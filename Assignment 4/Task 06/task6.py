input = open("input6.txt", "r")
output = open("output6.txt", "w")
content = input.read()
lines = [i for i in content.split("\n")]

rows, columns = [int(i) for i in lines[0].split()]
G = [list(i) for i in lines[1:rows + 1]]


def count_diamonds(G, x, y, D, rows, columns, flag):
    if x < 0 or y < 0 or x >= rows or y >= columns:
        return D
    if G[x][y] == "#":
        flag[x][y] = 1
        return D[0]
    if flag[x][y] == 1:
        return D[0]
    if G[x][y] == "D":
        D[0] += 1
    flag[x][y] = 1
    count_diamonds(G, x + 1, y, D, rows, columns, flag)
    count_diamonds(G, x - 1, y, D, rows, columns, flag)
    count_diamonds(G, x, y + 1, D, rows, columns, flag)
    count_diamonds(G, x, y - 1, D, rows, columns, flag)
    return D[0]


def find_max_diamonds(G, rows, columns):
    max_diamonds = 0
    for i in range(rows):
        for j in range(columns):
            if G[i][j] != "#":
                flag = [[0] * columns for i in range(rows)]
                max_diamonds = max(max_diamonds, count_diamonds(G, i, j, [0], rows, columns, flag))
    return max_diamonds


diamonds = find_max_diamonds(G, rows, columns)
output.write(str(diamonds))
input.close()
output.close()
