from common import Visibility, crop_stack, load_forest

forest = load_forest()
width = len(forest[0])

bottom_visible = []
last_top_visible = []
for _ in range(width):
    bottom_visible.append([])
    last_top_visible.append(-1)

visibility_mask = []
for _ in range(len(forest)):
    visibility_mask.append([])
    for _ in range(width):
        visibility_mask[-1].append(Visibility())

for i, row in enumerate(forest):
    row_stack = []
    last_left_visible = -1
    for j, tree in enumerate(row):
        if tree > last_left_visible:
            visibility_mask[i][j].left = True
            last_left_visible = tree
        if tree > last_top_visible[j]:
            visibility_mask[i][j].top = True
            last_top_visible[j] = tree

        crop_stack(row_stack, tree)
        row_stack.append((j, tree))
        crop_stack(bottom_visible[j], tree)
        bottom_visible[j].append((i, tree))

    for j, tree in row_stack:
        visibility_mask[i][j].right = True

for j, column in enumerate(bottom_visible):
    for i, tree in column:
        visibility_mask[i][j].bottom = True

total_visible = sum(sum(bool(c) for c in row) for row in visibility_mask)
print(total_visible)

exit()

print("Top visible:")
for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        print(tree if visibility_mask[i][j].top else " ", end="")
    print()

print("Bottom visible:")
for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        print(tree if visibility_mask[i][j].bottom else " ", end="")
    print()

print("Left visible:")
for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        print(tree if visibility_mask[i][j].left else " ", end="")
    print()

print("Right visible:")
for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        print(tree if visibility_mask[i][j].right else " ", end="")
    print()

print("Invisible:")
for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        print(tree if not visibility_mask[i][j] else " ", end="")
    print()
