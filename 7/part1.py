res = 0


def target_possible(nums, target):
    curr_set = set()
    def dfs(i, res, curr_set):
        if i == len(nums):
            curr_set.add(res)
            return
        
        dfs(i+1, res * nums[i], curr_set)
        dfs(i+1, res + nums[i], curr_set)
        dfs(i+1, nums[i], curr_set)

        str_res = str(res)
        remain = str(target)[len(str_res):]
        if remain != '' and int(remain) in curr_set  and int(str_res + remain) == target:
            return True


    res = dfs(1, nums[0], curr_set)
    if res or target in curr_set:
        return True
    return False

with open("input.txt", "r") as filename:
    for line in filename.readlines():
        target = int(line.rstrip().split(":")[0])
        nums = line.rstrip().split(": ")[1].split(" ")
        nums = [int(num) for num in nums]
        res += target_possible(nums, target)
        
    

    filename.close()


print(res)