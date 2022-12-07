with open("input.txt", "r") as f:
    lines = f.read().splitlines()

for i in range(len(lines[0]) - 14):
    s = lines[0][i:i+14]
    print(s)
    if len(set(s)) == len(s):
        print(i + 14)
        break
