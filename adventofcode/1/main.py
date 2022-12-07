# Read input file to list
with open("input.txt", "r") as f:
    lines = f.readlines()

elves = []
index = 0
for line in lines:
    # if line is empty
    if line == "\n":
        index += 1
    else:
        if index < len(elves):
            elves[index] += int(line)
        else:
            elves.append(int(line))

print(elves)

max_calories = 0
max_index = 0
for i in range(len(elves)):
    if elves[i] > max_calories:
        max_calories = elves[i]
        max_index = i

print(max_calories)

elves.sort(reverse=True)
print(elves)

print(elves[0] + elves[1] + elves[2])
