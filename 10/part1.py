grid = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        row = []
        for char in line.rstrip():
            if char == ".":
                row.append(-1)
            else:
                row.append(int(char))
        grid.append(row)
    
    filename.close()

steps = [
    [-1,0],
    [1,0],
    [0,-1],
    [0,1]
]

def dfs(i,j, visited):
    if grid[i][j] == 9:
        if (i,j) not in visited:
            visited.add((i,j))
            return 1
        else:
            return 0
    
    total = 0
    for x,y in steps:
        new_i = i + x
        new_j = j + y
        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == grid[i][j] + 1:
            total += dfs(new_i, new_j, visited)

    return total

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            visited = set()
            res += dfs(i,j,visited)

print(res)