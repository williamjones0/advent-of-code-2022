# Read input file to list
with open("input.txt", "r") as f:
    lines = f.readlines()

max_score = 0
for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        if y == 0 or y == len(lines) - 1 or x == 0 or x == len(lines[0]) - 1:
            continue

        t = line[x]
        if t == "\n":
            continue

        print(f"x: {x}, y: {y}, t: {t}")

        # Check if all trees to the left are shorter
        print("Checking left")
        visible = True
        left_score = 0
        for tree in range(x - 1, -1, -1):
            if line[tree] == "\n":
                continue
            print(f"t: {t}, line[tree]: {line[tree]}")

            if line[tree] < t:
                print("score += 1")
                left_score += 1
            else:
                print("score += 1")
                left_score += 1
                visible = False
                break

        # Check if all trees to the right are shorter
        print("Checking right")
        visible = True
        right_score = 0
        for tree in range(x + 1, len(line)):
            if line[tree] == "\n":
                continue
            print(f"t: {t}, line[tree]: {line[tree]}")

            if line[tree] < t:
                print("score += 1")
                right_score += 1
            else:
                print("score += 1")
                right_score += 1
                visible = False
                break

        # Check if all trees above are shorter
        print("Checking above")
        visible = True
        above_score = 0
        for tree in range(y - 1, -1, -1):
            check_tree = lines[tree][x]
            if check_tree == "\n":
                continue
            print(f"t: {t}, check_tree: {check_tree}")

            if check_tree < t:
                print("score += 1")
                above_score += 1
            else:
                print("score += 1")
                above_score += 1
                visible = False
                break

        # Check if all trees below are shorter
        print("Checking below")
        visible = True
        below_score = 0
        for tree in range(y + 1, len(lines)):
            check_tree = lines[tree][x]
            if check_tree == "\n":
                continue
            print(f"t: {t}, check_tree: {check_tree}")

            if check_tree < t:
                print("score += 1")
                below_score += 1
            else:
                print("score += 1")
                below_score += 1
                visible = False
                break

        print()

        if left_score * right_score * above_score * below_score > max_score:
            max_score = left_score * right_score * above_score * below_score

print(max_score)
