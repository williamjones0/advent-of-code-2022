def pretty_print(d):
    import json
    print(json.dumps(d, indent=4))


def sum_dict(d):
    total = 0
    for k, v in d.items():
        if isinstance(v, dict):
            total += sum_dict(v)
        elif isinstance(v, list):
            total += sum(v)
        else:
            total += v
    return total


def all_subdir_sizes(d, dirs):
    # Iterate through dictionary and print dir sizes.
    for k, v in d.items():
        if isinstance(v, dict):
            dirs.append((k, sum_dict(v)))
            all_subdir_sizes(v, dirs)


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

files = {"/": {}}
current_dir = []
for i in range(len(lines)):
    line = lines[i]
    line = line.split()
    if line[0] == "$":  # line is a command
        if line[1] == "cd":
            if line[2] == "..":
                current_dir.pop()
            else:
                current_dir.append(line[2])
        if line[1] == "ls":
            # Scan next lines until another command appears
            for j in range(i + 1, len(lines)):
                next_line = lines[j].split()
                if next_line[0] == "$":
                    break
                else:
                    location = files
                    for dir_ in current_dir:
                        location = location[dir_]

                    if next_line[0] == "dir":
                        location[next_line[1]] = {}
                    elif next_line[0].isdigit():
                        location[next_line[1]] = int(next_line[0])


pretty_print(files)
dirs = []
all_subdir_sizes(files, dirs)

total_disk_space = 70000000
total_disk_space -= sum_dict(files)
target = 30000000 - total_disk_space

smallest = 99999999999
smallest_dir = ""
for dir_ in dirs:
    if target < dir_[1] < smallest:
        smallest = dir_[1]
        smallest_dir = dir_[0]

print(f"Smallest dir: {smallest_dir}")
print(f"Smallest dir size: {smallest}")
