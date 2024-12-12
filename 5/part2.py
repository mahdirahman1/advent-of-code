from collections import defaultdict

def is_good(update, after_pages):
    seen = set()
    for pg in update:
        if pg in after_pages:
            if len(after_pages[pg].intersection(seen)) > 0:
                return False
        seen.add(pg)
    
    return True

def top_sort(nums, after_pages):
    set_nums = set(nums)
    adj_list = after_pages
    in_degree = {num: 0 for num in set_nums}
    for node in set_nums:
        for neighbor in adj_list[node]:
            if neighbor in set_nums:
                in_degree[neighbor] += 1

    visited = set()
    order = []
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor in set_nums:
                dfs(neighbor)
        order.append(node)

    for node in in_degree:
        if in_degree[node] == 0:
            dfs(node)
    
    return int(order[len(order)//2])
    


after_pages= defaultdict(set)
rules = True
res = 0
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        if line.rstrip() == "":
            rules = False
            continue
        if rules:
            pg, pg_after = line.rstrip().split("|")
            after_pages[pg].add(pg_after)
        else:
            update = line.rstrip().split(",")
            if is_good(update, after_pages):
                continue
            # this update is bad, get the correct sorting and return mid
            res += top_sort(update, after_pages)
            
    filename.close()

print(res)