grid = [list(x) for x in open("input.txt").read().strip().splitlines()]

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "S":
            start = (y, x)
            grid[y][x] = "a"
        elif cell == "E":
            end = (y, x)
            grid[y][x] = "z"

queue = [(0, start[0], start[1])]
visited = {start}

while queue:
    d, y, x = queue.pop(0)
    for ny, nx in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]:
        if ny < 0 or ny >= len(grid) or nx < 0 or nx >= len(grid[0]):
            continue
        if ord(grid[ny][nx]) - ord(grid[y][x]) > 1:
            continue
        if (ny, nx) in visited:
            continue
        if (ny, nx) == end:
            print(d + 1)
            break
        visited.add((ny, nx))
        queue.append((d + 1, ny, nx))
