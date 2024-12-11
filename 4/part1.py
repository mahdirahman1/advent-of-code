array = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        temp = []
        for char in line:
           temp.append(char)
        array.append(temp)
    filename.close()


def try_all_directions(i,j):
    total = 0
    total += up(i,j) + down(i,j) + left(i,j) + right(i,j) + top_left(i,j) + top_right(i,j) + bottom_left(i,j) + bottom_right(i,j)
    return total 


def up(i,j):
    stack = ['S','A','M','X']
    x,y = j, i
    while stack:
        if y < 0:
            return False
        if stack.pop() == array[y][x]:
            y -= 1
        else:
            return False
    
    return True

def down(i,j):
    stack = ['S','A','M','X']
    x,y = j, i
    while stack:
        if y >= len(array):
            return False
        if stack.pop() == array[y][x]:
            y += 1
        else:
            return False
    return True

def left(i,j):
    stack = ['S','A','M','X']
    x,y = j, i
    while stack:
        if x < 0:
            return False
        
        if stack.pop() == array[y][x]:
            x -= 1
        else:
            return False
    return True

def right(i,j):
    stack = ['S','A','M','X']
    x,y = j, i
    while stack:
        if x >= len(array[0]):
            return False
        
        if stack.pop() == array[y][x]:
            x += 1
        else:
            return False
    return True

def top_right(i,j):
    stack = ['S','A','M','X']
    x,y = j, i
    while stack:
        if x >= len(array[0]) or y < 0:
            return False
        
        if stack.pop() == array[y][x]:
            x += 1
            y -= 1

        else:
            return False
        
    return True

def top_left(i,j):
    stack = ['S','A','M','X']
    x,y = j, i
    while stack:
        if x < 0 or y < 0:
            return False
        
        if stack.pop() == array[y][x]:
            x -= 1
            y -= 1

        else:
            return False
        
    return True

def bottom_left(i,j):
    stack = ['S','A','M','X']
    x,y = j, i
    while stack:
        if x < 0 or y >= len(array):
            return False
        
        if stack.pop() == array[y][x]:
            x -= 1
            y += 1

        else:
            return False
        
    return True

def bottom_right(i,j):
    stack = ['S','A','M','X']
    x,y = j, i
    while stack:
        if x >= len(array[0]) or y >= len(array):
            return False
        if stack.pop() == array[y][x]:
            x += 1
            y += 1
        else:
            return False
        
    return True

def find_xmas_appearance(array):
    res = 0 
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "X":
                res += try_all_directions(i,j)
    
    return res

print(find_xmas_appearance(array))
