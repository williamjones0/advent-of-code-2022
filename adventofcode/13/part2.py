import ast


def bubble(l):
    for i in range(len(l)):
        already_sorted = True
        for j in range(len(l) - i - 1):
            if not compare(l[j], l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
                already_sorted = False

        if already_sorted:
            break

    return l


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

lines = [ast.literal_eval(line.strip()) for line in lines]
lines.append([[2]])
lines.append([[6]])
lines = bubble(lines)

count = 1
for i in range(len(lines)):
    if lines[i] == [[2]]:
        count *= i + 1
    elif lines[i] == [[6]]:
        count *= i + 1

print(count)
