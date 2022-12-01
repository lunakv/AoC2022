#!/usr/bin/env python3


def update_max(max_elfs, curr_elf):
    for i in range(len(max_elfs)):
        if curr_elf > max_elfs[i]:
            return max_elfs[:i] + [curr_elf] + max_elfs[i + 1 :]

    return max_elfs


try:
    max_elfs = [0, 0, 0]
    curr_elf = 0
    while True:
        line = input()
        if line == "":
            max_elfs = update_max(max_elfs, curr_elf)
            curr_elf = 0
        else:
            curr_elf += int(line)
except EOFError:
    print(max_elfs)
    print(sum(max_elfs))
