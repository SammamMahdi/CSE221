input = open("input1b.txt", "r")
output = open("output1b.txt", "w")
content = input.read()
operations = [i for i in content.split("\n")]
lines = int(operations[0])
for line in range(1, lines + 1):
    n, op, m = operations[line][10:].split()
    n = int(n)
    m = int(m)
    if op == "+":
        out = f"The result of {n} + {m} is {n+m}"
    elif op == "-":
        out = f"The result of {n} - {m} is {n-m}"
    elif op == "/":
        out = f"The result of {n} / {m} is {n/m}"
    elif op == "*":
        out = f"The result of {n} * {m} is {n*m}"
    if line < lines:
        out += "\n"
    output.write(out)
output.close()
