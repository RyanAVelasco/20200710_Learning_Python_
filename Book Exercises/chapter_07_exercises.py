fhand = open("mbox.txt")
count = 0
for line in fhand:
    print(count, "-", line)
    count += 1