inputs = open("input3.txt", "r")
output = open("output3.txt", "w")
content = inputs.read()
lines = [i for i in content.split("\n")]
pairs = list(zip(lines[1].split(), lines[2].split()))
n = int(lines[0])


# Does not work
# gives output
# ID: 4 Mark: 50
# ID: 9 Mark: 50
# ID: 7 Mark: 40
# ID: 3 Mark: 20
# ID: 2 Mark: 10
# ID: 1 Mark: 10
# ID: 5 Mark: 10
# def pair_sort(pairs, n):
#     for i in range(n - 1):
#         maxm = -99999
#         maxm_idx = 0
#         for j in range(i + 1, n):
#             if int(pairs[j][1]) > maxm:
#                 maxm = int(pairs[j][1])
#                 maxm_idx = j
#         if maxm > int(pairs[i][1]):
#             pairs[maxm_idx], pairs[i] = pairs[i], pairs[maxm_idx]
#         elif maxm == int(pairs[i][1]) and int(pairs[i][0]) > int(pairs[maxm_idx][0]):
#             pairs[maxm_idx], pairs[i] = pairs[i], pairs[maxm_idx]
#     return pairs


def pair_sort(pairs, n):
    for i in range(n - 1):
        maxm = -99999
        maxm_idx = 0
        for j in range(i + 1, n):
            if int(pairs[j][1]) > maxm:
                maxm = int(pairs[j][1])
                maxm_idx = j
        if maxm > int(pairs[i][1]):
            pairs[maxm_idx], pairs[i] = pairs[i], pairs[maxm_idx]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if pairs[j][1] != pairs[i][1]:
                break
            elif pairs[j][0] < pairs[i][0]:
                pairs[j], pairs[i] = pairs[i], pairs[j]

    return pairs


def write_str(pairs, n):
    out = [f"ID: {pairs[i][0]} Mark: {pairs[i][1]}" for i in range(n)]
    return "\n".join(out)


pairs = pair_sort(pairs, n)
output.write(write_str(pairs, n))
output.close()
