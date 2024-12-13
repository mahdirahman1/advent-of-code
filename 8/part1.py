from collections import defaultdict

antennas = defaultdict(set)
grid = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        temp = []
        for char in line.rstrip():
            temp.append(char)
        grid.append(temp)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            antennas[grid[i][j]].add((i, j))


def in_bound_and_valid(coords):
    i = coords[0]
    j = coords[1]
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        if grid[i][j] == "#":
            return False
        grid[i][j] = "#"
        return True
        
    return False
        

def place_antinodes(antennas):
    res = 0
    for arr in antennas.values():
        arr = list(arr)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                diff = [arr[i][0] - arr[j][0], arr[i][1] - arr[j][1]]
                first = [arr[i][0] + diff[0], arr[i][1] + diff[1]]
                second = [arr[j][0] - diff[0], arr[j][1] - diff[1] ]
                res += in_bound_and_valid(first) 
                res += in_bound_and_valid(second)
    
    print(res)
    
place_antinodes(antennas)

        