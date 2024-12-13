from collections import defaultdict
grid = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        row = []
        for char in line.rstrip():
            row.append(char)
        grid.append(row)

    filename.close()


"""
Idea: get the path from part 1
for each cell in the path, add a blocker and see if it creates a cycle
ie if it hits some obstacle from the same direction, then it's a cycle

"""

def get_start_position():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return (i,j)
            
def get_visited(start_i, start_j):
        visited = set()
        directions = [[-1,0], [0,1], [1,0], [0,-1]]
        dir = 0
        i,j = start_i, start_j
        while True:
            visited.add((i, j))
            direction = directions[dir]
            new_i = i + direction[0]
            new_j = j + direction[1]

            if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
                break
            
            if grid[new_i][new_j] == "#":
                dir = (dir + 1) % 4
            else:
                i = new_i
                j = new_j
        
        return visited
        

    

def is_cycle(start_i, start_j, x,y):
    visited = set()
    directions = [[-1,0], [0,1], [1,0], [0,-1]]
    dir = 0
    i = start_i
    j = start_j
    while True:
        direction = directions[dir]
        new_i = i + direction[0]
        new_j = j + direction[1]

        if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
            return False
            
        if grid[new_i][new_j] == "#":
            if (i,j, dir) in visited:
                return True
            visited.add((i, j, dir))
            dir = (dir + 1) % 4
        else:
            i = new_i
            j = new_j
    


start_i, start_j = get_start_position()
visited = get_visited(start_i, start_j)
res = 0
for x,y in visited:
    if x == start_i and y == start_j:
        continue
    grid[x][y] = "#"
    res += is_cycle(start_i, start_j, x,y)
    grid[x][y] = "."

print(res)




