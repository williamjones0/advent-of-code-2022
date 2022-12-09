with open("input.txt", "r") as f:
    lines = f.read().splitlines()

for i in range(len(lines[0]) - 4):
    s = lines[0][i:i+4]
    print(s)
    if len(set(s)) == len(s):
        print(i + 4)
        break
