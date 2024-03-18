input = open("input1a.txt", "r")
out = open("output1a.txt", "w")
n = input.readline()
for i in range(int(n)):
    content = input.readline()
    if int(content) % 2 == 0:
        write = f"{int(content)} is an Even number"
    else:
        write = f"{int(content)} is an Odd number"
    if i != int(n) - 1:
        write += "\n"
    out.write(write)
out.close()
