import re

stack_row_re = r"(.{3})(?: |$)"
move_re = r"move (\d+) from (\d+) to (\d+)"


def parse_stack():
    stack = None
    while True:
        matches = re.findall(stack_row_re, input())
        if stack is None:
            stack = [[] for _ in range(len(matches))]
        if matches[0] == " 1 ":
            input()
            for col in stack:
                col.reverse()
            return stack
        else:
            for i, (_, l, _) in enumerate(matches):
                if l != " ":
                    stack[i].append(l)


def parse_move_line():
    m = re.match(move_re, input())
    return [int(m.group(i)) for i in range(1, 4)]


def print_stack(stack):
    for col in stack:
        print(col[-1], end="")
    print()
