from collections import defaultdict

after_pages= defaultdict(str)
rules = True
with open("input.txt", "r") as filename:
    for line in filename.readlines():
        if line.rstrip() == "":
            rules = False
        if rules:
            pg, pg_after = line.rstrip().split("|")
            after_pages[pg] = pg_after
        else:
            pass
    filename.close()

print(after_pages)