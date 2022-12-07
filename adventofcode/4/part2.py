with open("input.txt", "r") as f:
    lines = f.read().splitlines()

count = 0
for line in lines:
    line = line.split(",")
    line[1] = line[1].split("-")
    line[0] = line[0].split("-")
    a = [int(x) for x in line[0] + line[1]]

    overlap = True
    if a[1] < a[2] or a[0] > a[3]:
        overlap = False

    if overlap:
        count += 1

print(count)
