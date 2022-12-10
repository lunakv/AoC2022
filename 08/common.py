class Visibility:
    def __init__(self):
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False

    def __bool__(self):
        return self.left or self.right or self.top or self.bottom


def crop_stack(stack, value):
    while stack and stack[-1][1] <= value:
        stack.pop()


def load_forest():
    forest = []
    try:
        while True:
            line = input()
            forest.append([int(c) for c in line])
    except EOFError:
        return forest
