def update_crt(cycle, x, crt):
    if cycle % 40 - 1 in [x - 1, x, x + 1]:
        crt[cycle - 1] = "#"


# Read input file to list
with open("input.txt", "r") as f:
    lines = f.readlines()

x = 1
cycle = 1
crt = ["." for i in range(6 * 40)]
for line in lines:
    line = line.split()
    if line[0] == "addx":
        cycle += 1
        update_crt(cycle, x, crt)
        x += int(line[1])
        cycle += 1
        update_crt(cycle, x, crt)
    elif line[0] == "noop":
        cycle += 1
        update_crt(cycle, x, crt)

print(*crt[0:40])
print(*crt[40:80])
print(*crt[80:120])
print(*crt[120:160])
print(*crt[160:200])
print(*crt[200:240])
