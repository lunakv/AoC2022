from common import load_forest

forest = load_forest()

max_vis_score = 0


def visibility_score(forest, i, j):
    score = 1
    tree = forest[i][j]
    distance = 0
    for x in range(i - 1, -1, -1):
        distance += 1
        if forest[x][j] >= tree:
            break
    score *= distance
    distance = 0
    for x in range(i + 1, len(forest)):
        distance += 1
        if forest[x][j] >= tree:
            break
    score *= distance
    distance = 0
    for y in range(j - 1, -1, -1):
        distance += 1
        if forest[i][y] >= tree:
            break
    score *= distance
    distance = 0
    for y in range(j + 1, len(forest[0])):
        distance += 1
        if forest[i][y] >= tree:
            break
    score *= distance
    return score


for i in range(len(forest)):
    row_max = max(visibility_score(forest, i, j) for j in range(len(forest[i])))
    max_vis_score = max(max_vis_score, row_max)

print(max_vis_score)
