def touching(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def move_follower(head, tail):
    x, y = tail
    if head[0] > tail[0]:
        x += 1
    elif head[0] < tail[0]:
        x -= 1

    if head[1] > tail[1]:
        y += 1
    elif head[1] < tail[1]:
        y -= 1

    return (x, y)


def move_head(head, direction):
    x, y = head
    if direction == "U":
        return x - 1, y
    elif direction == "D":
        return x + 1, y
    elif direction == "L":
        return x, y - 1
    elif direction == "R":
        return x, y + 1
    else:
        raise ValueError(f'Invalid direction "{direction}"')


def run(n, lines):
    knots = [(0, 0)] * n
    tail_visited = {(0, 0)}
    for line in lines:
        direction, length = line.split()
        for _ in range(int(length)):
            knots[0] = move_head(knots[0], direction)
            for i in range(1, n):
                if not touching(knots[i - 1], knots[i]):
                    knots[i] = move_follower(knots[i - 1], knots[i])
            tail_visited.add(knots[-1])

    return len(tail_visited)


def get_lines():
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        return lines


lines = get_lines()
print(run(2, lines))
print(run(10, lines))
