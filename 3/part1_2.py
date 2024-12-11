import re
res = 0
enabled = True
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
        all = re.findall(pattern, line)
        for item in all:
            if item == "do()":
                enabled = True
            elif item == "don't()":
                enabled = False
            else:
                if enabled:
                    pattern = r'\d{1,3},\d{1,3}'
                    nums = re.findall(pattern, item)
                    num1, num2 = nums[0].split(',')
                    res += int(num1) * int(num2)

    filename.close()

print(res)
   
