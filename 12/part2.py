from collections import defaultdict


grid = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        row = []
        for char in line.rstrip():
            row.append(char)
        grid.append(row)
    
    filename.close()


perimeter_map = defaultdict(set)
# store (region id): (i,j, direction of edge (left, right, up, down))
# if a cell has two edges store both seperately
area_map = defaultdict(int)
steps = [[1,0],[-1,0],[0,1],[0,-1]]

def store_perimeter(id, i,j,letter):
    # check all four sides, if it has an edge store it
    for dir in range(len(steps)):
        x, y  = steps[dir]
        new_i = x + i
        new_j = y + j
        if not (0 <= new_i < len(grid) and 0 <= new_j < len(grid[0])) or grid[new_i][new_j] != letter:
            perimeter_map[id].add((i,j,dir))
    

def dfs(i,j, visited, id):
    letter = grid[i][j]
    store_perimeter(id, i,j, letter)
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

def find_perimeter():

    for region in perimeter_map:
        left = perimeter_map[region]
        region_sides = 0
        while left:
            i,j,dir = left.pop()
            region_sides += 1
            # check and remove continous up down left right
            # check up
            if (i+1,j,dir) in left:
                curr = i+1
                while (curr, j, dir) in left:
                    left.remove((curr, j, dir))
                    curr += 1
            
            if (i-1, j, dir) in left:
                curr = i-1
                while (curr, j, dir) in left:
                    left.remove((curr, j, dir))
                    curr -= 1
            
            if (i,j+1, dir) in left:
                curr = j+1
                while (i, curr, dir) in left:
                    left.remove((i, curr, dir))
                    curr += 1
            
            if (i, j-1, dir) in left:
                curr = j-1
                while (i, curr, dir) in left:
                    left.remove((i, curr, dir))
                    curr -= 1

        perimeter_map[region] = region_sides

find_perimeter()

res = 0
for id in perimeter_map:
    res += perimeter_map[id] * area_map[id]

print(res)