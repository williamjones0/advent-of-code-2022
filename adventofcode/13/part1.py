import ast
from math import floor


def compare(a, b):
    for i in range(max(len(a), len(b))):
        try:
            a[i]
        except IndexError:
            return True

        try:
            b[i]
        except IndexError:
            return False

        if isinstance(a[i], int) and isinstance(b[i], int):
            if a[i] < b[i]:
                return True
            elif a[i] > b[i]:
                return False
        elif isinstance(a[i], list) and isinstance(b[i], list):
            if compare(a[i], b[i]):
                return True
            elif compare(b[i], a[i]):
                return False
        elif isinstance(a[i], int) and isinstance(b[i], list):
            if compare([a[i]], b[i]):
                return True
            elif compare(b[i], [a[i]]):
                return False
        elif isinstance(a[i], list) and isinstance(b[i], int):
            if compare(a[i], [b[i]]):
                return True
            elif compare([b[i]], a[i]):
                return False


# Read input file to list
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if line == "\n":
        lines.remove(line)

count = 0
index = 0
for i in range(floor((len(lines) + 1) / 2)):
    index += 1
    if compare(ast.literal_eval(lines[i*2].strip()), ast.literal_eval(lines[i*2+1].strip())):
        count += index

print(count)
