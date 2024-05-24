fhand = open("romeo.txt")
wlist = list()

for line in fhand :
    line = line.rstrip()
#    print(line)
    words = line.split(" ")
#    print(words)
    for word in words:
        if word not in wlist:
            wlist.append(word)
            wlist.sort()
print(wlist)