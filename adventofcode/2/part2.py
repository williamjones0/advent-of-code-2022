win = {
    "A": 2,
    "B": 3,
    "C": 1
}

draw = {
    "A": 1,
    "B": 2,
    "C": 3
}

lose = {
    "A": 3,
    "B": 1,
    "C": 2
}

with open("input.txt", "r") as f:
    lines = f.readlines()

score = 0
for line in lines:
    if line[2] == "X":  # lose
        score += lose[line[0]]
    if line[2] == "Y":  # draw
        score += 3
        score += draw[line[0]]
    if line[2] == "Z":  # win
        score += 6
        score += win[line[0]]

print(score)
