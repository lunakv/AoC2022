
def overlaps_fully(r1, r2):
    return r1[0] <= r2[0] and r1[1] >= r2[1] or r1[0] >= r2[0] and r1[1] <= r2[1]

def overlaps_partially(r1, r2):
    return (r1[0] <= r2[0] <= r1[1]) or (r1[0] <= r2[1] <= r1[1])

try:
    overlap = 0
    overlap_f = 0
    while True:
        r1, r2 = [tuple(int(n) for n in r.split('-')) for r in input().split(',')]
        if overlaps_fully(r1, r2):
            overlap_f += 1
            overlap += 1
        elif overlaps_partially(r1, r2):
            overlap += 1
except EOFError:
    print(overlap_f)
    print(overlap)

        
