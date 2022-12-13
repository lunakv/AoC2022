from typing import Literal


def parse_line(line: str) -> list | int:
    return _parse_line_recursive(line, 0, len(line))[1]


def _parse_line_recursive(
    list_line: str, start: int, end: int
) -> tuple[int, list | int]:
    if list_line[start] == ",":
        # starts at separating comma, skip
        start += 1

    if list_line[start] == "[":
        # parsing list value
        i = start + 1  # current char pointer
        ret = []
        while i < end:
            if list_line[i] == "]":
                # closing list
                return i + 1, ret
            else:
                # recursing to parse list element
                i, val = _parse_line_recursive(list_line, i, end)
                ret.append(val)
        raise ValueError("Unclosed list encountered")
    else:
        # parsing int value
        for i in range(start, end):
            if list_line[i] == "," or list_line[i] == "]":
                return i, int(list_line[start:i])
        raise ValueError("Unterminated int value encountered")


def compare(a: list | int, b: list | int) -> Literal[-1, 0, 1]:
    if isinstance(a, int) and isinstance(b, int):
        # simple integer comparison
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    # int-list comparisons reduce to list-list
    elif isinstance(a, int):
        return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])

    # list-list comparison
    min_len = min(len(a), len(b))
    for i in range(min_len):
        cmp = compare(a[i], b[i])
        if cmp != 0:
            return cmp

    # in case of a tie, the shorter list comes first
    return compare(len(a), len(b))


try:
    correct_pair_sum = 0
    above_2 = 0
    above_6 = 1  # [[2]] is above [[6]]
    i = 0
    while True:
        i += 1
        a = parse_line(input())
        b = parse_line(input())
        cmp = compare(a, b)
        if cmp != 1:
            correct_pair_sum += i
        for l in [a, b]:
            if compare(l, [[2]]) == -1:
                above_2 += 1
                above_6 += 1
            elif compare(l, [[6]]) == -1:
                above_6 += 1
        input()
except EOFError:
    print(correct_pair_sum)
    print((above_2 + 1) * (above_6 + 1))  # one-based indexing
