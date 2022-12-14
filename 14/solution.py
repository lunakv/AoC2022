from typing import Literal, Set, Tuple

Point = Tuple[int, int]
Board = Set[Point]


def direction(a: int, b: int) -> Literal[1, -1]:
    return 1 if a <= b else -1


def add_range(board: Board, point_a: Point, point_b: Point) -> None:
    ax, ay = point_a
    bx, by = point_b
    dx = direction(ax, bx)
    dy = direction(ay, by)
    for i in range(ax, bx + dx, dx):
        for j in range(ay, by + dy, dy):
            board.add((i, j))


def parse_input() -> Board:
    board: Board = set()
    try:
        while True:
            points = [tuple(int(n) for n in x.split(",", 1)) for x in input().split(" -> ")]
            for i in range(len(points) - 1):
                add_range(board, points[i], points[i + 1])
    except EOFError:
        return board


def next_move(board: Board, position: Point) -> Point | None:
    dirs = [(0, 1), (-1, 1), (1, 1)]
    x, y = position
    for dx, dy in dirs:
        if (x + dx, y + dy) not in board:
            return x + dx, y + dy
    return None


def get_stopping_point(board: Board, start: Point, max_y: int) -> Point:
    x, y = start
    while y < max_y:
        new_pos = next_move(board, (x, y))
        if new_pos is None:
            return x, y
        x, y = new_pos
    return x, y


def run(board: Board, floor: int, fall_through: bool) -> int:
    start = (500, 0)
    i = 0
    while True:
        end_pos = get_stopping_point(board, start, floor)
        if end_pos == start:
            return i + 1
        elif fall_through and end_pos[1] == floor:
            return i
        else:
            board.add(end_pos)
            i += 1


board = parse_input()
max_y = max(y for x, y in board)
print(run(set(board), max_y, True))
print(run(board, max_y + 1, False))
