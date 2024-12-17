import heapq


positions = []
velocities = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        line = line.rstrip()
        position, vel = line.split(" ")
        x = int(position.split("=")[1].split(",")[0])
        y = int(position.split("=")[1].split(",")[1])
        positions.append([x,y])
        vel_x = int(vel.split("=")[1].split(",")[0])
        vel_y = int(vel.split("=")[1].split(",")[1])
        velocities.append([vel_x, vel_y])

    filename.close()

width = 101
height = 103

def findMaxIsland(grid):
    visited = set()
    steps = [[0,-1],[0,1],[1,0],[-1,0]]
    def dfs(i,j, visited):
        if (i,j) in visited:
            return 0
        
        visited.add((i,j))
        count = 1
        for x,y in steps:
            new_i = i + x
            new_j = j + y
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == "#":
                count += dfs(new_i, new_j, visited)
        
        return count
    
    max_size = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in visited and grid[i][j] == "#":
                max_size = max(max_size, dfs(i,j,visited))
    
    return max_size
    

def calc_position(pos_x, pos_y, vel_x, vel_y, time):
    pos_x = (pos_x + (vel_x * time)) % width
    pos_y = (pos_y + (vel_y * time)) % height
    return [pos_x, pos_y]

def populate_grid(grid, time):
    for i in range(len(positions)):
        x,y = positions[i]
        vel_x, vel_y = velocities[i]
        x,y = calc_position(x,y,vel_x,vel_y, time)
        grid[y][x] = "#"


max_islands = []
for time in range(100,10000):  
    grid = [['.' for _ in range(width)] for _ in range(height)]
    populate_grid(grid, time)
    heapq.heappush(max_islands, [-findMaxIsland(grid), time])

print(max_islands[:20])
