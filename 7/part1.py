res = 0


def target_possible(nums, target):

    def dfs(i, res):
        if i == len(nums):
            return res == target
        
        return dfs(i+1, res * nums[i]) or dfs(i+1, res + nums[i]) or dfs(i+1, int(str(res)+str(nums[i])))
    
         
      
    return dfs(1, nums[0])

with open("input.txt", "r") as filename:
    for line in filename.readlines():
        target = int(line.rstrip().split(":")[0])
        nums = line.rstrip().split(": ")[1].split(" ")
        nums = [int(num) for num in nums]
        if target_possible(nums, target):
            res += target
        
    

    filename.close()


print(res)