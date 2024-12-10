from collections import defaultdict
l2_freq = defaultdict(int)
l1 = []

with open("input.txt", "r") as filename:
    for line in filename.readlines():
        line = line.rstrip().split("   ")
        l2_freq[int(line[1])] += 1
        l1.append(int(line[0]))
    
    filename.close()
    
similarity_score = 0

for num in l1:
    similarity_score += num * l2_freq[num]

print(similarity_score)
   
