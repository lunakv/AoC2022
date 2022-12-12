def score(c):
    if c == "S":
        return 0
    if c == "E":
        return 25
    return ord(c) - ord("a")


def parse_input():
    ret = []
    start, end = None, None
    i = 0
    try:
        while True:
            line = input()
            ret.append([score(c) for c in line])
            if "S" in line:
                start = (i, line.index("S"))
            if "E" in line:
                end = (i, line.index("E"))
            i += 1
    except EOFError:
        return ret, start, end


dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def neighbors(pos, maze):
    bx, by = pos
    for dx, dy in dirs:
        x, y = bx + dx, by + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[x]):
            if maze[x][y] - maze[bx][by] <= 1:
                yield x, y


def bfs(maze, start, end_cond):
    visited = {start}
    queue = [(start, 0)]

    while queue:
        curr, distance = queue.pop(0)
        for neighbor in neighbors(curr, maze):
            if end_cond(neighbor):
                return distance + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))


maze, start, end = parse_input()
dst = bfs(maze, start, lambda pos: pos == end)
print(dst)

maze = [[-score for score in line] for line in maze]
dst = bfs(maze, end, lambda pos: maze[pos[0]][pos[1]] == 0)
print(dst)
