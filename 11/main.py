from collections import defaultdict
from functools import cache

stones = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        for char in line.rstrip().split(" "):
            stones.append(int(char))
            
    filename.close()

def part1(stones):
    blinks = 25
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                stone_str = str(stone)
                new_stones.append(int(stone_str[:mid]))
                new_stones.append(int(stone_str[mid:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    return len(stones)


@cache
def solve(stone, blink_count):
    if blink_count == 0:
        return 1
    
    if stone == "0":
        return solve("1", blink_count-1)
        
    if len(stone) % 2 == 0:
        mid = len(stone)//2
        left, right = str(int(stone[:mid])), str(int(stone[mid:]))
        return solve(left, blink_count-1) + solve(right, blink_count-1)
        
    return solve(str(int(stone)*2024), blink_count-1)

res = 0
for stone in stones:
    res += solve(str(stone), 75)
    
print(res)


