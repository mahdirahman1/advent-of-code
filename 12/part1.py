from collections import defaultdict


grid = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        row = []
        for char in line.rstrip():
            row.append(char)
        grid.append(row)
    
    filename.close()


perimeter_map = defaultdict(int)
area_map = defaultdict(int)
steps = [[1,0],[-1,0],[0,1],[0,-1]]

def find_cell_perimeter(i,j,letter):
    # check all four sides
    perimeter = 0
    for x,y in steps:
        new_i = x + i
        new_j = y + j
        if not (0 <= new_i < len(grid) and 0 <= new_j < len(grid[0])) or grid[new_i][new_j] != letter:
            perimeter += 1
    return perimeter

def dfs(i,j, visited, id):
    letter = grid[i][j]
    perimeter_map[id] += find_cell_perimeter(i,j, letter)
    area_map[id] += 1
    visited.add((i,j))

    for x,y in steps:
        new_i = x + i
        new_j = y + j
        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == letter and (new_i, new_j) not in visited:
            dfs(new_i, new_j, visited, id)



visited = set()
id = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) not in visited:
            dfs(i,j,visited, id)
            id += 1

res = 0
for id in perimeter_map:
    res += perimeter_map[id] * area_map[id]

print(res)