# Find character present in both halves of the input string
def repeated(s):
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]

    for c in s1:
        if c in s2:
            return c


with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    priority = ord(repeated(line))
    if priority >= 97:
        total += priority - 96
    else:
        total += priority - 64 + 26

print(total)
