def update_tail(h, t):
    # If in the same row/column
    if h[0] == t[0] or h[1] == t[1]:
        # If the head is more than 1 step away, the tail must move one step in the same direction
        if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
            if h[0] == t[0]:
                if h[1] > t[1]:
                    t[1] += 1
                else:
                    t[1] -= 1
            else:
                if h[0] > t[0]:
                    t[0] += 1
                else:
                    t[0] -= 1

    # If in different rows and columns, move the tail one step diagonally
    else:
        if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
            if h[0] > t[0]:
                t[0] += 1
            else:
                t[0] -= 1

            if h[1] > t[1]:
                t[1] += 1
            else:
                t[1] -= 1


# Read input file to list
with open("input.txt", "r") as f:
    lines = f.readlines()

rope = [[0, 0] for i in range(10)]

visited = []
for line in lines:
    direction = line.split()[0]
    distance = int(line.split()[1])
    if direction == "R":
        for i in range(distance):
            rope[0] = [rope[0][0] + 1, rope[0][1]]
            for j in range(len(rope) - 1):
                update_tail(rope[j], rope[j + 1])

            if (rope[9][0], rope[9][1]) not in visited:
                visited.append((rope[9][0], rope[9][1]))

    elif direction == "L":
        for i in range(distance):
            rope[0] = [rope[0][0] - 1, rope[0][1]]
            for j in range(len(rope) - 1):
                update_tail(rope[j], rope[j + 1])

            if (rope[9][0], rope[9][1]) not in visited:
                visited.append((rope[9][0], rope[9][1]))

    elif direction == "U":
        for i in range(distance):
            rope[0] = [rope[0][0], rope[0][1] + 1]
            for j in range(len(rope) - 1):
                update_tail(rope[j], rope[j + 1])

            if (rope[9][0], rope[9][1]) not in visited:
                visited.append((rope[9][0], rope[9][1]))

    elif direction == "D":
        for i in range(distance):
            rope[0] = [rope[0][0], rope[0][1] - 1]
            for j in range(len(rope) - 1):
                update_tail(rope[j], rope[j + 1])

            if (rope[9][0], rope[9][1]) not in visited:
                visited.append((rope[9][0], rope[9][1]))

print(len(visited))
