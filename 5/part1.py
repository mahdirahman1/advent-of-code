from collections import defaultdict

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
            seen = set()
            for pg in update:
                if pg in after_pages:
                    if len(after_pages[pg].intersection(seen)) > 0:
                        break
                seen.add(pg)
            else:
                res += int(update[len(update)//2])
        

    filename.close()

print(res)