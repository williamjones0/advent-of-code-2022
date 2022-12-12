def update_count(cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * x
    else:
        return 0


# Read input file to list
with open("input.txt", "r") as f:
    lines = f.readlines()

count = 0
x = 1
cycle = 1
for line in lines:
    line = line.split()
    if line[0] == "addx":
        cycle += 1
        count = count + update_count(cycle, x)
        x += int(line[1])
        cycle += 1
    elif line[0] == "noop":
        cycle += 1

    count = count + update_count(cycle, x)

print(f"Final count: {count}")
