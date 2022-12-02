#!/usr/bin/env python

# Rock = 0, Paper = 1, Scissors = 2
# Lose = 0, Draw = 1, Win = 2
def translate(char):
    if char == "A" or char == "X":
        return 0
    if char == "B" or char == "Y":
        return 1
    if char == "C" or char == "Z":
        return 2

    raise ValueError(f"invalid character {char} ({ord(char)})")


# 1 if I win, 0 if draw, -1 if they win
def cmp(them, me):
    if me == them:
        return 0
    elif (them + 1) % 3 == me:
        return 1
    else:
        return -1


def my_play(them, strategy):
    return (them + strategy - 1) % 3


def round_score(them, me):
    return (cmp(them, me) + 1) * 3 + me + 1


def main():
    part_1_score = 0
    part_2_score = 0
    try:
        while True:
            them, me = [translate(c) for c in input().split()]
            part_1_score += round_score(them, me)
            me = my_play(them, me)
            part_2_score += round_score(them, me)
    except EOFError:
        print("P1:", part_1_score)
        print("P2:", part_2_score)


if __name__ == "__main__":
    main()
