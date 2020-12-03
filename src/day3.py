input_location = './input/day3.txt'
forest = []
with open(input_location) as f:
    for line in f:
        forest.append([char for char in line.strip()])
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
total = 1
for slope in slopes:
    sledding = True
    trees = 0
    x,y = (0,0)
    while (y < len(forest)-1):
        x += slope[0]
        y += slope[1]
        if x >= len(forest[0]):
            x -= len(forest[0])
        trees += forest[y][x] == '#'
    total*=trees
print(total)