import re


def parse_line(line):
    return parse_list(line, 0, len(line))[1]


def parse_list(list_line, start, end):
    if list_line[start] == ",":
        # starting comma, skip
        start += 1

    if list_line[start] == "[":
        # parsing as list
        i = start + 1
        ret = []
        while i < end:
            if list_line[i] == "]":
                # closing list
                return i + 1, ret
            else:
                # recursing
                i, val = parse_list(list_line, i, end)
                ret.append(val)
    else:
        # parsing as int
        for i in range(start + 1, end):
            if list_line[i] == "," or list_line[i] == "]":
                return i, int(list_line[start:i])


def compare_lists(list_a, list_b):
    if isinstance(list_a, int) and isinstance(list_b, int):
        if list_a < list_b:
            return -1
        elif list_a > list_b:
            return 1
        else:
            return 0
    elif isinstance(list_a, int):
        return compare_lists([list_a], list_b)
    elif isinstance(list_b, int):
        return compare_lists(list_a, [list_b])

    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        cmp = compare_lists(list_a[i], list_b[i])
        if cmp != 0:
            return cmp

    return compare_lists(len(list_a), len(list_b))


try:
    correct = 0
    above_2 = 0
    above_6 = 1  # [[2]] is above [[6]]
    i = 0
    while True:
        a = parse_line(input())
        b = parse_line(input())
        cmp = compare_lists(a, b)
        if cmp != 1:
            correct += i
        for l in [a, b]:
            if compare_lists(l, [[2]]) == -1:
                above_2 += 1
                above_6 += 1
            elif compare_lists(l, [[6]]) == -1:
                above_6 += 1
        input()
        i += 1
except EOFError:
    print(correct)
    print((above_2 + 1) * (above_6 + 1))
