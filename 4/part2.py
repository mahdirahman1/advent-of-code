array = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        array.append(line.rstrip())
    filename.close()

def check_mas(i,j):
    # check if diagonals are M or S
    diag_set = set(['M', 'S'])
    if i-1 < 0 or j-1 < 0 or j+1 >= len(array[0]) or i+1 >= len(array):
        return False
    
    if array[i-1][j-1] not in diag_set or array[i-1][j+1] not in diag_set or array[i+1][j-1] not in diag_set or array[i+1][j+1] not in diag_set:
        return False
    
    return array[i-1][j-1] != array[i+1][j+1] and array[i-1][j+1] != array[i+1][j-1]

def find_xmas_appearance(array):
    res = 0 
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "A":
                res += check_mas(i,j)
    
    return res

print(find_xmas_appearance(array))
