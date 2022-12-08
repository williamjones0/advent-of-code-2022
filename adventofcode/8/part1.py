# Read input file to list
with open("input.txt", "r") as f:
    lines = f.readlines()

count = 0
# Horizontally L-R
visible = []
for i in range(len(lines)):
    line = lines[i]
    max_height = -1
    for j in range(len(line)):
        tree = line[j]
        if tree == "\n":
            continue
        if int(tree) > max_height:
            max_height = int(tree)
            if (i, j) not in visible:
                visible.append((i, j))
                count += 1

# Horizontally R-L
for i in range(len(lines)):
    line = lines[i]
    max_height = -1
    for j in range(len(line) - 1, -1, -1):
        tree = line[j]
        if tree == "\n":
            continue
        if int(tree) > max_height:
            max_height = int(tree)
            if (i, j) not in visible:
                visible.append((i, j))
                count += 1

# Vertically T-B
vertically = [*zip(*lines)]
for i in range(len(vertically)):
    line = vertically[i]
    max_height = -1
    for j in range(len(line)):
        tree = line[j]
        if tree == "\n":
            continue
        if int(tree) > max_height:
            max_height = int(tree)
            if (j, i) not in visible:
                visible.append((j, i))
                count += 1

# Vertically B-T
for i in range(len(vertically)):
    line = vertically[i]
    max_height = -1
    for j in range(len(line) - 1, -1, -1):
        tree = line[j]
        if tree == "\n":
            continue
        if int(tree) > max_height:
            max_height = int(tree)
            if (j, i) not in visible:
                visible.append((j, i))
                count += 1

print(f"Visible trees: {count}")
