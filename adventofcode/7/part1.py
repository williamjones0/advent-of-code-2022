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


def all_subfolder_sizes(d, dirs):
    # Iterate through dictionary and print folder sizes.
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"{k}: {sum_dict(v)}")
            dirs.append((k, sum_dict(v)))
            all_subfolder_sizes(v, dirs)


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

files = {"/": {}}
current_dir = []
for i in range(len(lines)):
    line = lines[i]
    line = line.split()
    print(line)
    if line[0] == "$":  # line is a command
        if line[1] == "cd":
            if line[2] == "..":
                current_dir.pop()
            else:
                current_dir.append(line[2])
                print(f"current_dir: {current_dir}")
        if line[1] == "ls":
            # Scan next lines until another command appears
            print("====== ls ======")
            print(f"Current dir: {current_dir}")
            for j in range(i + 1, len(lines)):
                next_line = lines[j].split()
                print(next_line)
                if next_line[0] == "$":
                    break
                else:
                    location = files
                    for dir_ in current_dir:
                        location = location[dir_]

                    if next_line[0] == "dir":
                        location[next_line[1]] = {}
                        print(f"files at current_dir:")
                        pretty_print(files[current_dir[0]])
                    elif next_line[0].isdigit():
                        location[next_line[1]] = int(next_line[0])
                        print(f"files at current_dir:")
                        pretty_print(files[current_dir[0]])

            print("====== END ls ======")
            print("files:")
            pretty_print(files)
            print()

print(files)
print(sum_dict(files))
folders = []
all_subfolder_sizes(files, folders)
total_size = 0
for folder in folders:
    if folder[1] < 100000:
        total_size += folder[1]

print(total_size)
