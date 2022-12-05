import common

stack = common.parse_stack()
try:
    while True:
        n, src, dst = common.parse_move_line()
        move = stack[src - 1][-n:]
        stack[src - 1] = stack[src - 1][:-n]
        stack[dst - 1] += move
except EOFError:
    common.print_stack(stack)
