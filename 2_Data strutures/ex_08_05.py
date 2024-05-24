fhand = open("mbox-short.txt")
count = 0
for line in fhand :
    line = line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
    word = words[1]
    count = count +1
    print(word)
print("There were", count, "lines in the file with From as the first word")