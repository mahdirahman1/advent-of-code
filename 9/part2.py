from collections import defaultdict

nums = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        for char in line.rstrip():
            nums.append(int(char))
    
    filename.close()

disk_block = []
id = 0
free_space = defaultdict(int) #start_idx: length
ids_length = defaultdict(int) #id: (start_idx, length)

for i in range(0, len(nums), 2):
    id_length = nums[i]
    free = 0
    if i+1 < len(nums):
        free = nums[i+1]
    
    ids_length[id] = [len(disk_block), id_length]
    disk_block += [id] * id_length
    id += 1
    if free:
        free_space[len(disk_block)] = free
    disk_block += [None] * free

"""
Now we need to move large id files in decreasing order to leftmost free spaces
To do this lets store free_space, index: length
lets store: ids: length
then we can loop over large to small ids and look for smallest index that will fit the file, and update if any remaining space left

"""

for id in sorted(ids_length.keys(), reverse=True):
    id_start_index = ids_length[id][0]
    id_length = ids_length[id][1]
    index_found = -1
    for idx in sorted(free_space.keys()):
        if idx > id_start_index:
            break
        if free_space[idx] >= id_length:
            index_found = idx
            # update free_space
            still_free = free_space[idx] - id_length
            if still_free > 0:
                free_space[idx + id_length] = still_free
            del free_space[idx]
            # set the previous positions of this id to None
            for i in range(id_start_index, id_start_index + id_length):
                disk_block[i] = None
            break
    
    if index_found != -1:
        for i in range(index_found, index_found + id_length):
            disk_block[i] = id
        

res = 0
for idx in range(len(disk_block)):
    if disk_block[idx] != None:
        res += disk_block[idx] * idx

print(res)
    
