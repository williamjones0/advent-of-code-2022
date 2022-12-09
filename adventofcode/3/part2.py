def repeated(s1, s2, s3):
    for c in s1:
        if c in s2 and c in s3:
            return c
    return None


with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0
for i in range(int(len(lines) / 3)):
    c = repeated(lines[i*3], lines[i*3 + 1], lines[i*3 + 2])
    if c is not None:
        priority = ord(c)
        if priority >= 97:
            total += priority - 96
        else:
            total += priority - 64 + 26

print(total)
