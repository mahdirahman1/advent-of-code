l1 = []
l2 = []
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        line = line.rstrip().split("   ")
        l1.append(int(line[0]))
        l2.append(int(line[1]))
    
    filename.close()
    
res = 0
l1.sort()
l2.sort()
for i in range(len(l1)):
    res += abs(l1[i] - l2[i])
    
print(res)
   
