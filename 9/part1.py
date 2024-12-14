nums = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        for char in line.rstrip():
            nums.append(int(char))
    
    filename.close()

disk_block = []
id = 0
used = 0
for i in range(0, len(nums), 2):
    id_length = nums[i]
    used += id_length
    free = 0
    if i+1 < len(nums):
        free = nums[i+1]
    disk_block += [id] * id_length
    id += 1
    disk_block += [None] * free


end_ptr = len(disk_block)-1

for index in range(used):
    if disk_block[index] != None:
        continue

    while disk_block[end_ptr] == None:
        end_ptr -= 1
    
    disk_block[index] = disk_block[end_ptr]
    disk_block[end_ptr] = None
    end_ptr -= 1

res = 0
for index in range(used):
    res += index * disk_block[index]

print(res)

    
