grid = []
commands = []
g = True
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        line = line.rstrip()
        if line == "":
            g = False
        
        if g:
            row = []
            for char in line:
                if char == "#" or char == ".":
                    row.append(char)
                    row.append(char)
                elif char == "O":
                    row.append("[")
                    row.append("]")
                elif char == "@":
                    row.append(char)
                    row.append(".")
            grid.append(row)
        else:
            for char in line:
                commands.append(char)

    filename.close()

def get_start_pos():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return [i,j]
            
def move_one(x,y,directions):
    dx,dy = directions
    i,j = x,y
    # check if next position is empty
    if grid[i+dx][j+dy] == ".":
        grid[i][j] = "."
        grid[i+dx][j+dy] = "@"
        return [i+dx,j+dy]
    
    elif grid[i+dx][j+dy] == "#":
        return [i,j]
    
    else:
        block_i, block_j = i+dx, j+dy
        assert grid[block_i][block_j] == "[" or grid[block_i][block_j] == "]"
        
        # there is a blocker here, find longest end of block chain
        while grid[block_i][block_j] == "[" or grid[block_i][block_j] == "]":
            block_i += dx
            block_j += dy
        
        if grid[block_i][block_j] == "#":
            return [x,y]
        
        # we must have reached a "." so we can move everyone up by one space
        assert(grid[block_i][block_j] == ".")
        while block_i != i or block_j != j:
            grid[block_i][block_j] = grid[block_i-dx][block_j-dy]
            block_i -= dx
            block_j -= dy
        
        grid[block_i][block_j] = "."
            
        return [block_i+dx, block_j+dy]
        

def update_grid(x,y,command):
    if command == "<":
        return move_one(x,y,[0,-1])
    elif command == ">":
        return move_one(x,y,[0,1])
    elif command == "^":
        return move_one(x,y,[-1,0])
    else:
        return move_one(x,y,[1,0])


x,y = get_start_pos()

for command in commands:
    x,y = update_grid(x,y,command)

print(grid)
# res = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == "O":
#             res += 100*i + j

# print(res)