grid = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        row = []
        for char in line.rstrip():
            row.append(char)
        grid.append(row)

    filename.close()

visited = set()
directions = [[-1,0], [0,1], [1,0], [0,-1]]
def dfs(i,j, dir, visited):
    visited.add((i, j))
    direction = directions[dir]
    new_i = i + direction[0]
    new_j = j + direction[1]

    if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
        return
    
    if grid[new_i][new_j] == "#":
        dfs(i,j, (dir + 1) % 4, visited)
    else:
        dfs(new_i, new_j, dir, visited)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            dfs(i, j, 0, visited)


print(len(visited))


