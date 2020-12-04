input_location = './input/day3.txt'
with open(input_location) as f:
    G = [line.strip() for line in f.readlines()]

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

ans = 1
for (dc,dr) in slopes:
    r = 0
    c = 0 
    score = 0
    while r < len(G)-1:
        c += dc
        r += dr
        if G[r][c%len(G[r])]=='#':
            score += 1
    ans *= score
    if dc==3 and dr==1:
        print(score)
print(ans)