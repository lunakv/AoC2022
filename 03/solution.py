def prio(c):
    if c.islower():
        return ord(c)-ord('a') + 1
    else:
        return ord(c)-ord('A') + 27

try:
    item_prio_sum = 0
    group_prio_sum = 0
    current_group = []
    while True:
        line = input()
        middle = len(line)//2
        first, second = line[:middle], line[middle:]
        common = next(c for c in first if c in second)
        item_prio_sum += prio(common)

        current_group.append(line)
        if len(current_group) == 3:
            x, y, z = current_group
            common = next(c for c in x if c in y and c in z)
            group_prio_sum += prio(common)
            current_group = []
except EOFError:
    print(item_prio_sum)
    print(group_prio_sum)
