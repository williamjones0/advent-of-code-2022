with open("input.txt", "r") as f:
    lines = f.read().splitlines()

# Find the line that corresponds to the bottom of the stacks
bottom_line = 0
for i in range(len(lines)):
    if lines[i][1] == "1":
        bottom_line = i
        break

stacks = [[] for i in range(int(lines[bottom_line][-1]))]

stacks_input = lines[0:bottom_line]
for i in range(len(stacks_input)):
    line = stacks_input[i]
    for j in range(len(line)):
        c = line[j]
        if c not in [" ", "[", "]"]:  # character is a crate
            stacks[j // 4].append(c)

for stack in stacks:
    stack.reverse()

instructions = []
lines = lines[bottom_line + 2:]
for line in lines:
    instruction = line.split(" ")
    instructions.append([int(instruction[1]), int(instruction[3]) - 1, int(instruction[5]) - 1])

for instruction in instructions:
    crates = stacks[instruction[1]][-instruction[0]:]
    del stacks[instruction[1]][-instruction[0]:]
    stacks[instruction[2]] += crates

o = ""
for stack in stacks:
    o += stack[-1]

print(o)
