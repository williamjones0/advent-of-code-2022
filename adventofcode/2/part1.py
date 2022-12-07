win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

with open("input.txt", "r") as f:
    lines = f.readlines()

score = 0
for line in lines:
    if line[2] == "X":
        score += 1
    if line[2] == "Y":
        score += 2
    if line[2] == "Z":
        score += 3

    if line[2] == win[line[0]]:
        score += 6
    elif ord(line[2]) == ord(line[0]) + 23:
        score += 3

print(score)
