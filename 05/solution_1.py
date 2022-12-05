import common
import re

stack = common.parse_stack()

try:
    while True:
        n, src, dst = common.parse_move_line()
        for _ in range(n):
            item = stack[src - 1].pop()
            stack[dst - 1].append(item)
except EOFError:
    for column in stack:
        print(column[-1], end="")
    print()
