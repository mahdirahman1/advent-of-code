safe = 0
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        nums = line.rstrip().split(" ")
        is_inc = int(nums[0]) < int(nums[1])
        for i in range(1, len(nums)):
            if not 1 <= abs(int(nums[i]) - int(nums[i-1])) <= 3:
                break

            if int(nums[i-1]) < int(nums[i]) and not is_inc:
                break
            
            if int(nums[i-1]) > int(nums[i]) and is_inc:
                break 
        else:
            safe += 1
    
    filename.close()
    
print(safe)
   
