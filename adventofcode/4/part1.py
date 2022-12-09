with open("input.txt", "r") as f:
    lines = f.read().splitlines()

count = 0
for line in lines:
    line = line.split(",")
    line[1] = line[1].split("-")
    line[0] = line[0].split("-")
    a = [int(x) for x in line[0] + line[1]]

    if a[0] <= a[2] and a[1] >= a[3]:
        count += 1
    elif a[2] <= a[0] and a[3] >= a[1]:
        count += 1

print(count)
